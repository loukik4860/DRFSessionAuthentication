from django.urls import path, include
from .views import RegistrationView,ActivateView,Activation_Confirm,getCSRFToken

urlpatterns = [
    path("account/csrf_cookies/", getCSRFToken.as_view(), name="csrf_cookies"),
    path("account/registration/", RegistrationView.as_view(), name="register"),
    path("account/active/<str:uid>/<str:token>/", ActivateView.as_view(), name="activate"),
    path("account/active/", Activation_Confirm.as_view(), name="activateConfirm")
]
