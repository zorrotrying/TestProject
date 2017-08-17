"""cDAPdev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from coreapp import views
from coreapp.forms import Model_cdap_form1, Model_cdap_form2, Model_cdap_form3

from test_formtools.forms import ContactForm1, ContactForm2
from test_formtools.views import ContactWizard

formlist = [Model_cdap_form1, Model_cdap_form2, Model_cdap_form3]

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^newapp/$', views.RegistModelWizard.as_view(formlist,
                                                      condition_dict={'1': views.some_condition,
                                                                      '2': views.some_condition2})),
    url(r'^appconf/(?P<appname>[^/]+)/$', views.configApp, name='app_config'),
    url(r'^contact/$', ContactWizard.as_view([ContactForm1,ContactForm2])),
    url(r'^admin/', admin.site.urls),
]
