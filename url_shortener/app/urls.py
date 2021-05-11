from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app-index'),
    path('<id>/', views.show, name='app-show')
]