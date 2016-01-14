from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', TestView.as_view(), name='index'),
    url(r'^sendemail$', TestView.as_view(), name='sendemail'),
]
