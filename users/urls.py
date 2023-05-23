from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from users.views import (
    RegisterView,
    SendEmailVerificationCodeView,
    CheckEmailVerificationCodeView,
    CheckEmailVerificationCodeWithParams,
    FacebookLogin,
    GoogleLogin
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/google/', GoogleLogin.as_view(), name='google_auth'),
    path('token/facebook/', FacebookLogin.as_view(), name='facebook_auth'),
    path('email/verification/', SendEmailVerificationCodeView.as_view(), name="send-email-code"),
    path('email/check-verification/', CheckEmailVerificationCodeView.as_view(), name="check-email-code"),
    path('email/check-verification-code/', CheckEmailVerificationCodeWithParams.as_view(), name="check-email")
]
