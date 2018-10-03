from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from DjangoTest.models import Blogger, Video
#from django_registration.backends.activation.urls import
from django_registration.backends.activation.views import RegistrationView, ActivationView
from django.urls import reverse_lazy


class MyRegistrationView(RegistrationView):
    template_name = 'accounts/login.html'
    email_subject_template = 'accounts/registration/activation_email_subject.txt'
    email_body_template = 'accounts/registration/activation_email.txt'
    success_url = reverse_lazy('registration_complete')


class AccountActivatedView(TemplateView):
    template_name = 'accounts/registration/account_activated.html'


class RegistrationCompleteView(TemplateView):
    template_name = 'accounts/registration/registration_complete.html'


class ActivationCompleteView(TemplateView):
    template_name = 'accounts/registration/account_activated.html'


class MyActivationView(ActivationView):
    success_url = reverse_lazy('activation_complete')


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    redirect_field_name = ''


class Blogger(PermissionRequiredMixin, ListView):
    permission_required = 'view_blogger'
    template_name = 'bloggers.html'
    queryset = Blogger.objects.all()
    context_object_name = 'bloggers'


class Video(PermissionRequiredMixin, ListView):
    permission_required = 'view_video'
    template_name = 'videos.html'
    queryset = Video.objects.all()
    context_object_name = 'videos'
