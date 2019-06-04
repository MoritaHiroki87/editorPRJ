from django.urls import path
from . import views
from .views import *

app_name = 'editor'
urlpatterns = [
    path('', EditView.as_view(), name='edit'),
]