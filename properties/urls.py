from django.urls import path
from .views import ListProperties, image_upload_view

urlpatterns = [
    path('', ListProperties.as_view(), name='properties'),
    path('<pk>/upload',image_upload_view, name='upload')
]
