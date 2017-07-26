from django import forms
from models import Model_cdap



class Model_cdap_form1(forms.ModelForm):

    class Meta:
        model = Model_cdap
        exclude = ('pub_date','slug','modelpath','modelcmd',)


class Model_cdap_form2(forms.ModelForm):

    class Meta:
        model = Model_cdap
        fields = ('modelpath',)

class Model_cdap_form3(forms.ModelForm):

    class Meta:
        model = Model_cdap
        fields = ('modelcmd',)