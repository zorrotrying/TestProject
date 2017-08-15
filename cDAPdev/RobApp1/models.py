
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

def upload_to_path(instance, filename):
    upload_to_path = r'RobApp1/%s/%s/%s' % (instance.user.username, datetime.today().strftime("%Y/%m/%d"), filename)
    return upload_to_path

class Services(models.Model):
    user = models.ForeignKey(User, related_name='RobApp1')
    SheetName = models.CharField(default="TestDefault", max_length=255)
    StartLine = models.FloatField(default=11)
    EmptyLineNum = models.FloatField(default=11)
    filepath = models.FileField(upload_to=upload_to_path)

