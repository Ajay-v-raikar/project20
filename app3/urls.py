from django.urls import path 
from app3 import views

urlpatterns = [
    path('<input>',views.display,name='display'),
]