from django.urls import path
from . import views

urlpatterns = [
    path("registration/", views.user_registration, name="registration"),
    path("sign-in/", views.user_login, name="sign-in"),
    path("test/", views.test_token, name="test"),
]
