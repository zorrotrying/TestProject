from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions



class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        super(ContactForm1, self).__init__(*args, **kwargs)
        #self.fields['author'].widget = HiddenInput()

        self.helper = FormHelper(self)

        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                                href="{% url "home" %}">Cancel</a>"""),
                Submit('save', 'Submit'),
            ))



class ContactForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea)

