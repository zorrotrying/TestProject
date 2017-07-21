from django import forms
from models import Model_cdap
class Model_cdap_form(forms.ModelForm):

    class Meta:
        model = Model_cdap
        exclude = ('pub_date',)