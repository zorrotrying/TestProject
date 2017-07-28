from django.conf.urls import url
from django import forms

from forms import ContactForm1
from preview import ModelPreviewDemo

urlpatterns = [
    url(r'^post/$', ModelPreviewDemo(ContactForm1)),
]