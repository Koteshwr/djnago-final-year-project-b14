from django.urls import path
from . import views

urlpatterns = [
    path("",views.Audio_store,name = ""),
    path("result/",views.getResult,name = "result"),
]


