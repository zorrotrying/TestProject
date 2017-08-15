
from django.shortcuts import render
from service_core import cDAP_Fun_V2
from forms import ServiceForm
from modelcore.models import cdap_model
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def RunService(request, modelId, username=None):
    ModelName = cdap_model.objects.filter(id=modelId).values_list('name', flat=True)[0]
    if not username:
        username = request.user.username

    if request.method == 'POST':
        formdata = ServiceForm(request.POST, request.FILES)
        if formdata.is_valid():
            initial_obj = formdata.save(commit=False)
            initial_obj.user = request.user
            initial_obj.save()
            formdata.save()

            outfilepath = cDAP_Fun_V2.Fileprocess(SheetName=formdata.cleaned_data['SheetName'],StartLine=formdata.cleaned_data['StartLine'],EmptyLineNum=formdata.cleaned_data['EmptyLineNum'],filepath=initial_obj.InputFile.path)
            context = {'modelId': modelId, 'username': username,'file2down':outfilepath, 'Inputfile':initial_obj.InputFile.url}
            return render(request, 'result/file_result.html', context)
    else:
        context = {'modelId': modelId, 'username': username, 'form': ServiceForm}
    return render(request, 'robapp5/model_start_form.html',context)
