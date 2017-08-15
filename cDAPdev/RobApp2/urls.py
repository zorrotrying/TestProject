
from django.conf.urls import url
import views

urlpatterns = [
    url(r'RobApp2-run/', views.RunService, name='RobApp2_run'),
]
