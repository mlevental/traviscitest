# -*- coding: utf-8 -*-


from thread import start_new_thread

import boto3
import time
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

EMAIL_ADDRESS_SOURCE = 'si_email1@web.de'
EMAIL_ADDRESS_TARGET = 'si_email2@web.de'

REGION_NAME = 'us-east-1'


class TestView(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if request.is_ajax():
            self.send_email('Test Email', 'Test Message')
            return JsonResponse({'testKey': 'testValue'})

        else:
            return render(request, self.template_name)

    def send_email(self, subject, message):
        client = boto3.client('ses', REGION_NAME)
        client.send_email(
                Source=EMAIL_ADDRESS_SOURCE,
                Destination={
                    'ToAddresses': [EMAIL_ADDRESS_TARGET]
                },
                Message={
                    'Subject': {
                        'Data': subject,
                        'Charset': 'UTF8'
                    },
                    'Body': {
                        'Text': {
                            'Data': message,
                            'Charset': 'UTF8'
                        }
                    }
                },
                ReturnPath=EMAIL_ADDRESS_SOURCE
        )


long_process_progress = 0
long_process_completed = False


class LongProcessView(View):
    def post(self, request):
        print 'POST request received'

        # Es läuft nur ein Thread zur gleichen Zeit
        if long_process_progress == 0:
            print "start thread"
            global long_process_completed
            long_process_completed = False
            start_new_thread(process, ())

        if request.is_ajax:
            print "it's an AJAX request"
            return JsonResponse({'progress': long_process_progress})
        else:
            print "it's not an AJAX request"
            return HttpResponse("This wasn't an AJAX request")


def update_long_process(request):
    if long_process_completed:
        return JsonResponse({'processCompleted': long_process_completed})
    else:
        return JsonResponse({'progress': long_process_progress})


def process():
    for i in range(0, 100):
        global long_process_progress
        long_process_progress += 1
        time.sleep(0.25)

        print long_process_progress

    # Variablen zurücksetzen bzw. aktualisieren wenn Prozess vorbei
    long_process_progress = 0
    global long_process_completed
    long_process_completed = True

    print "stop thread"