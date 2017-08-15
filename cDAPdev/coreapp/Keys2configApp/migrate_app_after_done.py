from django.conf import settings
import subprocess


managepath = settings.BASE_DIR + '\\' + 'manage.py'
child = subprocess.Popen(['python', managepath, 'makemigrations', appname])
child.wait()
child2 = subprocess.Popen(['python', managepath, 'migrate'])
child2.wait()