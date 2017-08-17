
from django.conf.urls import url
import views

urlpatterns = [
    url(r'RobApp01-run/', views.RunService, name='RobApp01_run'),
]
