from django.conf.urls import url
from coreapp2 import views

urlpatterns = [
    url(r'newapp2/$', views.RegistModelWizard.as_view(views.FORMS,
                                                       condition_dict={'form_2': views.some_condition,
                                                                       'form_3': views.some_condition2})),
]