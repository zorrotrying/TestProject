from django.shortcuts import render, render_to_response , HttpResponse, redirect

from formtools.wizard.views import SessionWizardView

from django.core.files.storage import FileSystemStorage

from models import Model_cdap

from django.conf import settings
import os

from coreapp.forms import Model_cdap_form1, Model_cdap_form2, Model_cdap_form3


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

    def dispatch(self, request, *args, **kwargs):
        self.instance = Model_cdap()
        return super(RegistModelWizard, self).dispatch(request, *args, **kwargs)

    def get_form_instance(self, step):
        return self.instance


    def done(self, form_list, **kwargs):
        self.instance.save()
        appname = form_list[0].cleaned_data.get('name')
        newappdir = os.path.join(settings.BASE_DIR, appname)
        os.makedirs(newappdir)

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

