from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from formtools.wizard.views import SessionWizardView
from forms import Model_cdap_form1, Model_cdap_form2, Model_cdap_form3
import forms2
from models import Model_cdap

from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import subprocess


FORMS = [
    ('form_basic', Model_cdap_form1 ),
    ('form_2', Model_cdap_form2),
    ('form_3', Model_cdap_form3),
]


FORMS2 = [
    ('form_basic', forms2.Model_cdap_form1),
    ('form_2', forms2.Model_cdap_form2),
    ('form_3', forms2.Model_cdap_form3),
]





TEMPLATES = {'form_basic': 'coreapp2/form_basic.html',
             'form_2': 'coreapp2/form_2.html',
             'form_3': 'coreapp2/form_3.html'}


TEMPLATES2 = {'form_basic': 'coreapp2/form_basic_2.html',
             'form_2': 'coreapp2/form_2_2.html',
             'form_3': 'coreapp2/form_3_2.html'}






class RegistModelWizard2(SessionWizardView):

    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'tempscript'))

    def dispatch(self, request, *args, **kwargs):
        self.instance = Model_cdap()
        return super(RegistModelWizard2, self).dispatch(request, *args, **kwargs)

    def get_form_initial(self, step):
        return self.initial_dict.get('0', {'author': self.request.user})

    def get_form_instance(self, step):
        return self.instance


    def get_template_names(self):
        return [TEMPLATES2[self.steps.current]]

    def done(self, form_list, **kwargs):
        self.instance.save()
        return HttpResponseRedirect(reverse('home'))
        #return HttpResponseRedirect('home')


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

    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'tempscript'))

    def dispatch(self, request, *args, **kwargs):
        self.instance = Model_cdap()
        return super(RegistModelWizard, self).dispatch(request, *args, **kwargs)

    def get_form_initial(self, step):
        return self.initial_dict.get('0', {'author': self.request.user})

    def get_form_instance(self, step):
        return self.instance


    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        self.instance.save()
        return HttpResponseRedirect(reverse('home'))
        #return HttpResponseRedirect('/home/')

