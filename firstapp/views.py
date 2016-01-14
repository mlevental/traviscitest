import boto3
from django.http import JsonResponse
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
