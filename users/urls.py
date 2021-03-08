from django.urls import path

from users.views import RegistrationView

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration')
]