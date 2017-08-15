
from django.conf.urls import url
import views

urlpatterns = [
    url(r'RobApp1-run/', views.RunService, name='RobApp1_run'),
]
