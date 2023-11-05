from django.urls import path
from . import views

urlpatterns = [
    path('create', views.new_view.as_view(), name='create-view'),
]
