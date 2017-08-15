
from django import forms
from models import Services
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ('SheetName', 'StartLine', 'EmptyLineNum', 'filepath')

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML('''<a role="button" class="btn btn-default"
                        href="{% url "home" %}">Cancel</a>'''),
                Submit('save', 'Submit'),
        ))
