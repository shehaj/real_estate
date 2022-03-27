from django.urls import path
from .views import ListProperties

urlpatterns = [
    path('', ListProperties.as_view(), name='properties')
]
