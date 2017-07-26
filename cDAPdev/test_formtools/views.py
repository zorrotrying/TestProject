from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView

# Create your views here.

class ContactWizard(SessionWizardView):

    def done(self, form_list, **kwargs):
        return render_to_response('test_formtools/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
