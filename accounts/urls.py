from django.urls import path
from .views import CustomPasswordChangeView, signup, CustomLoginView, CustomLogoutView, PasswordChangeView


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='change-password'),
]
