
from django.conf.urls import url
import views

urlpatterns = [
    url(r'robapp5-run/', views.RunService, name='robapp5_run'),
]
