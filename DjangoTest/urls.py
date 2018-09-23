from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django_registration import views as register_views
from DjangoTest.views import Blogger, Profile

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/profile/', Profile.as_view()),
    path('accounts/register/', register_views.RegistrationView.as_view(template_name='accounts/login.html'), name='register'),
    path('bloggers/', Blogger.as_view()),
    path('admin/', admin.site.urls),
]
