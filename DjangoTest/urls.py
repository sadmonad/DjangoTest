from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from DjangoTest.accounts.registration import views as registration_views
from DjangoTest.accounts.activation import views as activation_views
from DjangoTest.accounts.profile import views as profile_views
from DjangoTest.bloggers import views as bloggers_views
from DjangoTest.videos import views as videos_views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='profile/templates/login.html'), name='login'),
    path('accounts/profile/', profile_views.Profile.as_view()),

    path('accounts/register/', registration_views.MyRegistrationView.as_view(), name='register'),
    path('accounts/register/complete', registration_views.RegistrationCompleteView.as_view(), name='registration_complete'),

    url(r'^accounts/activate/(?P<activation_key>[-:\w]+)/$', activation_views.MyActivationView.as_view(), name='activate'),
    path('accounts/activate/complete', activation_views.AccountActivatedView.as_view(), name='activation_complete'),

    path('bloggers/', bloggers_views.Blogger.as_view(), name='bloggers'),
    path('videos/', videos_views.Video.as_view(), name='videos'),
    path('admin/', admin.site.urls),
]
