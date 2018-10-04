from django.views.generic import TemplateView
from django_registration.backends.activation.views import RegistrationView
from django.urls import reverse_lazy


class MyRegistrationView(RegistrationView):
    template_name = 'profile/templates/login.html'
    email_subject_template = 'activation/templates/activation_email_subject.txt'
    email_body_template = 'activation/templates/activation_email.txt'
    success_url = reverse_lazy('registration_complete')


class RegistrationCompleteView(TemplateView):
    template_name = 'registration/templates/registration_complete.html'
