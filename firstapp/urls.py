from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'^$', TestView.as_view(), name='index'),
    url(r'^sendemail$', TestView.as_view(), name='sendemail'),
    url(r'^longprocess$', LongProcessView.as_view(), name='long-process'),
    url(r'^updatelongprocess$', update_long_process, name='update-long-process'),
]
