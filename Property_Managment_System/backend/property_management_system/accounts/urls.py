from django.urls import path
from .views import SignUpView, MyTokenObtainPairView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='user_signup'),
    path('signin/', MyTokenObtainPairView.as_view(), name='signin'),
]
