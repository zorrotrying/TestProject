from django import forms
from models import Model_cdap
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions



class Model_cdap_form1(forms.ModelForm):

    class Meta:
        model = Model_cdap
        exclude = ('pub_date','slug','modelpath','modelcmd',)

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        super(Model_cdap_form1, self).__init__(*args, **kwargs)
        self.fields['author'].widget = HiddenInput()

        self.helper = FormHelper(self)

        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                                href="{% url "home" %}">Cancel</a>"""),
                Submit('save', 'Submit'),
            ))



class Model_cdap_form2(forms.ModelForm):

    class Meta:
        model = Model_cdap
        fields = ('modelpath',)

    def __init__(self, *args, **kwargs):
        super(Model_cdap_form2, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url "home" %}">Cancel</a>"""),
                Submit('save', 'Submit'),
        ))





class Model_cdap_form3(forms.ModelForm):

    class Meta:
        model = Model_cdap
        fields = ('modelcmd',)

    def __init__(self, *args, **kwargs):
        super(Model_cdap_form3, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url "home" %}">Cancel</a>"""),
                Submit('save', 'Submit'),
            ))

