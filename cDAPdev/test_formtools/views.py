from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from forms import ContactForm1, ContactForm2


# Create your views here.

class ContactWizard(SessionWizardView):

    def done(self, form_list, **kwargs):
        return render_to_response('test_formtools/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


FORMS = [('0', ContactForm1),
         ('1', ContactForm2)]

TEMPLATES = {'0': 'test_formtools/step-1.html',
             '1': 'test_formtools/step-2.html'}


class ContactWizard2(SessionWizardView):

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        return HttpResponseRedirect('home')
