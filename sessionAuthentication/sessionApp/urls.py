from django.urls import path, include
from .views import RegistrationView, ActivateView, Activation_Confirm, getCSRFToken,\
    loginView,LogoutView,UserDetailsView,ChangePassword,DeleteAccountView


urlpatterns = [
    path("account/csrf_cookies/", getCSRFToken.as_view(), name="csrf_cookies"),
    path("account/registration/", RegistrationView.as_view(), name="register"),
    path("account/active/<str:uid>/<str:token>/", ActivateView.as_view(), name="activate"),
    path("account/active/", Activation_Confirm.as_view(), name="activateConfirm"),
    path("account/login/", loginView.as_view(), name="loginView"),
    path("account/user/", UserDetailsView.as_view(), name="userDetails"),
    path("account/changePassword/",ChangePassword.as_view(),name="changepassword"),
    path("account/logout/", LogoutView.as_view(), name="Logout"),
    path("account/delete/", DeleteAccountView.as_view(), name="deleteAccount"),
]
