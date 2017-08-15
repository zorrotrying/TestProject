from django.shortcuts import render, render_to_response , HttpResponse, redirect

from formtools.wizard.views import SessionWizardView

from django.core.files.storage import FileSystemStorage

from models import Model_cdap
from forms import cdap_form4, cdap_form5

from django.conf import settings
import os
import subprocess
from shutil import copy2

from Keys2configApp.Python_Config_S1 import generateForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


def some_condition(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
    if cleaned_data.get('type') in ('python', 'r'):
        return True
    else:
        return False


def some_condition2(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
    if cleaned_data.get('type') in ('python', 'r'):
        return False
    else:
        return True


class RegistModelWizard(SessionWizardView):
    #file_storage = FileSystemStorage(location='/coreapp/rawtemp')
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'tempscript'))

    def dispatch(self, request, *args, **kwargs):
        self.instance = Model_cdap()
        return super(RegistModelWizard, self).dispatch(request, *args, **kwargs)



    # def get_form_kwargs(self, step=None):
    #     if step == 0:
    #         return {'author': self.request.user}
    #     else:
    #         return {}

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

        script_name = form_list[1].cleaned_data['modelpath'].name
        from_script_path = os.path.join(settings.MEDIA_ROOT, 'script4apps', appname, script_name)
        to_script_path = os.path.join(settings.BASE_DIR, appname, 'service_core')

        if not os.path.exists(to_script_path):
            os.makedirs(to_script_path)

        copy2(from_script_path, to_script_path)


        return redirect('app_config', appname=appname)

        # # from_script_path = form_list[1].cleaned_data['modelpath']
        # return render_to_response('coreapp/regist_app_wizard_done.html', {'testTag': script_name,
        #                                                                   'testTag1': from_script_path,
        #                                                                   'testTag2': to_script_path})


def configApp(request, appname):
    Dir2Add = os.path.join(settings.BASE_DIR, appname, 'service_core')
    ScriptName = 'cDAP_Fun_V2'

    TempResult = generateForm(Dir2Add, ScriptName)[0]
    FunName = TempResult['Fun_Name']

    if request.method == 'POST':
        Forms = cdap_form5(request.POST, ArgList=TempResult['Arg_Name'])
        if Forms.is_valid():
            field_tuple = ()
            Textpath = ''
            TextField = ''
            TextViewList = []

            for key, value in Forms.cleaned_data.items():
                if value == 'FileField':
                    Textpath = """
def upload_to_path(instance, filename):
    upload_to_path = r'%s/%%s/%%s/%%s' %% (instance.user.username, datetime.today().strftime("%%Y/%%m/%%d"), filename)
    return upload_to_path
""" % appname
                    texttemp = '    %s = models.%s(upload_to=upload_to_path)\n' % (key, value)
                    texttemp_view = '%s=initial_obj.InputFile.path' % key
                elif value == 'CharField':
                    texttemp = '    %s = models.%s(default="%s", max_length=255)\n' % (key, value, 'TestDefault')
                    texttemp_view = "%s=formdata.cleaned_data['%s']" % (key, key)
                elif value == 'FloatField':
                    texttemp = '    %s = models.%s(default=%s)\n' % (key, value, 11)
                    texttemp_view = "%s=formdata.cleaned_data['%s']" % (key, key)
                elif value == 'DateField':
                    texttemp = '    %s = models.%s()\n' % (key, value)
                    texttemp_view = "%s=formdata.cleaned_data['%s']" % (key, key)
                elif value == 'BooleanField':
                    texttemp = '    %s = models.%s()\n' % (key, value)
                    texttemp_view = "%s=formdata.cleaned_data['%s']" % (key, key)
                TextField += texttemp
                TextViewList.append(texttemp_view)
                field_tuple += tuple([key])
# Create app models.py
            Text = """
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
%s
class Services(models.Model):
    user = models.ForeignKey(User, related_name='%s')
%s
""" % (Textpath, appname, TextField)
            model_path = os.path.join(settings.BASE_DIR, appname, 'models.py')
            with open(model_path, 'w+') as mf:
                mf.write(Text)
                mf.close()

# Create app forms.py based on models.py
            TextForm = """
from django import forms
from models import Services
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = %s

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML('''<a role="button" class="btn btn-default"
                        href="{%% url "home" %%}">Cancel</a>'''),
                Submit('save', 'Submit'),
        ))
""" % (field_tuple,)
            form_path = os.path.join(settings.BASE_DIR, appname, 'forms.py')
            with open(form_path, 'w+') as ff:
                ff.write(TextForm)
                ff.close()

# Create app views.py
            TextView = """
from django.shortcuts import render
from service_core import %s
from forms import ServiceForm
from modelcore.models import cdap_model
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def RunService(request, modelId, username=None):
    ModelName = cdap_model.objects.filter(id=modelId).values_list('name', flat=True)[0]
    if not username:
        username = request.user.username

    if request.method == 'POST':
        formdata = ServiceForm(request.POST, request.FILES)
        if formdata.is_valid():
            initial_obj = formdata.save(commit=False)
            initial_obj.user = request.user
            initial_obj.save()
            formdata.save()

            outfilepath = %s.%s(%s)
            context = {'modelId': modelId, 'username': username,'file2down':outfilepath, 'Inputfile':initial_obj.InputFile.url}
            return render(request, 'result/file_result.html', context)
    else:
        context = {'modelId': modelId, 'username': username, 'form': ServiceForm}
    return render(request, '%s/model_start_form.html',context)
""" % (ScriptName, ScriptName, FunName, ','.join(TextViewList), appname)

            views_path = os.path.join(settings.BASE_DIR, appname, 'views.py')
            with open(views_path, 'w+') as vf:
                vf.write(TextView)
                vf.close()

# Create app template folder
            template_dir_app = os.path.join(settings.BASE_DIR, appname, 'templates', appname)
            if not os.path.exists(template_dir_app):
                os.makedirs(template_dir_app)
            source_path = os.path.join(os.path.dirname(__file__), 'base_files')

            copy2(os.path.join(source_path, 'model_start_form.html'), template_dir_app)
            copy2(os.path.join(source_path, 'model_tutorial.html'), template_dir_app)

# Create app urls
            Texturls = """
from django.conf.urls import url
import views

urlpatterns = [
    url(r'%s-run/', views.RunService, name='%s_run'),
]
""" % (appname, appname)
            urls_path = os.path.join(settings.BASE_DIR, appname, 'urls.py')
            with open(urls_path, 'w+') as uf:
                uf.write(Texturls)
                uf.close()

            form_dir = Forms.cleaned_data
            return render(request, 'coreapp/config_app_done.html', {'form_dir': form_dir})
    else:
        Forms = cdap_form5(ArgList=TempResult['Arg_Name'])
    return render(request, 'coreapp/config_app_start.html', {'form': Forms, 'funname': FunName})

