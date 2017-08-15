from django import forms
from models import Model_cdap



class Model_cdap_form1(forms.ModelForm):

    class Meta:
        model = Model_cdap
        exclude = ('pub_date','slug','modelpath','modelcmd',)

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        super(Model_cdap_form1, self).__init__(*args, **kwargs)
        self.fields['author'].widget = HiddenInput()



class Model_cdap_form2(forms.ModelForm):

    class Meta:
        model = Model_cdap
        fields = ('modelpath',)

class Model_cdap_form3(forms.ModelForm):

    class Meta:
        model = Model_cdap
        fields = ('modelcmd',)

class cdap_form4(forms.Form):
    #app_name = forms.CharField(max_length=255)
    Arg_Type_Choices = (
        ('FileField', 'File'),
        ('CharField', 'String'),
        ('FloatField', 'Number'),
        ('DateField', 'Date'),
        ('BooleanField', 'Boolean'),
    )
    Arg_Type = forms.ChoiceField(
        choices=Arg_Type_Choices,
        required=True,
    )


class cdap_form5(forms.Form):
    def __init__(self, *args, **kwargs):
        ArgList = kwargs.pop('ArgList')
        super(cdap_form5, self).__init__(*args, **kwargs)

        Arg_Type_Choices = (
            ('FileField', 'File'),
            ('CharField', 'String'),
            ('FloatField', 'Number'),
            ('DateField', 'Date'),
            ('BooleanField', 'Boolean'),
        )

        for x in xrange(len(ArgList)):
            self.fields[ArgList[x]] = forms.ChoiceField(
                label=ArgList[x],
                choices=Arg_Type_Choices,
                required=True,
            )

