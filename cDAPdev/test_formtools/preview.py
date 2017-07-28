from django.http import HttpResponseRedirect

from formtools.preview import FormPreview

class ModelPreviewDemo(FormPreview):

    def done(self, request, cleaned_data):
        return HttpResponseRedirect('form/success')