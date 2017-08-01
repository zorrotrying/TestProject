from django.shortcuts import render, render_to_response , HttpResponse, redirect

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

        #settings.INSTALLED_APPS += appname


        return render_to_response('coreapp/regist_app_wizard.html', {
                                  'form_data': [form.cleaned_data for form in form_list],
        })



# def registerModel(request):
#     if request.method == 'POST':
#         formdata = Model_cdap_form(request.POST)
#         if formdata.is_valid():
#             formdata.save()
#             return redirect('registscript')
#     else:
#         formdata = Model_cdap_form()
#     return render(request, 'coreapp/regist_app_new.html', {'form':formdata})
#
#
#
#
# def registerModel_S2(request):
#     if request.method == 'POST':
#         form = Model_cdap_form2(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return render(request, 'coreapp/regist_app_new_S3.html', {'form':form})
#     else:
#         form = Model_cdap_form2()
#     return render(request, 'coreapp/regist_app_new_S2.html', {'form':form})
#
#
#

