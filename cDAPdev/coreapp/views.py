from django.shortcuts import render, HttpResponseRedirect , HttpResponse, redirect
from django.core.urlresolvers import reverse

from formtools.wizard.views import SessionWizardView

from django.core.files.storage import FileSystemStorage

from models import Model_cdap

from django.conf import settings
import os
import subprocess
#import importlib

# Create your views here.

def home(request):
    return render(request, 'home.html')


def some_condition(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
    if cleaned_data.get('type') == 'python':
        return True
    else:
        return False


def some_condition2(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
    if cleaned_data.get('type') == 'python':
        return False
    else:
        return True


class RegistModelWizard(SessionWizardView):
    #file_storage = FileSystemStorage(location='/coreapp/rawtemp')
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'tempscript'))
    template_name = 'coreapp/form_wizard_base.html'

    def dispatch(self, request, *args, **kwargs):
        self.instance = Model_cdap()
        return super(RegistModelWizard, self).dispatch(request, *args, **kwargs)

    def get_form_initial(self, step):
        return self.initial_dict.get('0', {'author': self.request.user})

    def get_form_instance(self, step):
        return self.instance

    def done(self, form_list, **kwargs):
        self.instance.save()
        appname = form_list[0].cleaned_data.get('name')
        managepath = settings.BASE_DIR+'\\'+'manage.py'

        child = subprocess.Popen(['python', managepath, 'startapp', appname])
        child.wait()

        add_set_path = settings.SITE_ROOT +'\\'+'add_settings.py'

        with open(add_set_path, 'r') as rawAppFile:
            rawApp = rawAppFile.readlines()[0]
        Add_AppList = r"%s,'%s%s" % (rawApp[:-1],appname,rawApp[-2:])

        f = open(add_set_path, 'w')
        f.write(Add_AppList)
        f.close()

        return HttpResponseRedirect(reverse('home'))
