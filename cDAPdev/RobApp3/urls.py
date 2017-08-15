
from django.conf.urls import url
import views

urlpatterns = [
    url(r'RobApp3-run/', views.RunService, name='RobApp3_run'),
]
