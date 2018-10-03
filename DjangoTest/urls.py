from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from DjangoTest.views import Blogger, Profile, Video, \
    MyRegistrationView, MyActivationView, AccountActivatedView, RegistrationCompleteView


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/profile/', Profile.as_view()),

    path('accounts/register/', MyRegistrationView.as_view(), name='register'),
    path('accounts/register/complete', RegistrationCompleteView.as_view(), name='registration_complete'),

    url(r'^accounts/activate/(?P<activation_key>[-:\w]+)/$', MyActivationView.as_view(), name='activate'),
    path('accounts/activate/complete', AccountActivatedView.as_view(), name='activation_complete'),

    path('bloggers/', Blogger.as_view(), name='bloggers'),
    path('videos/', Video.as_view(), name='videos'),
    path('admin/', admin.site.urls),
]
