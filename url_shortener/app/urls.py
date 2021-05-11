from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app-index'),
    path('<str:id>/', views.show, name='app-show')
]