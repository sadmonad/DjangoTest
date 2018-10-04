from django.views.generic import TemplateView
from django_registration.backends.activation.views import ActivationView
from django.urls import reverse_lazy


class AccountActivatedView(TemplateView):
    template_name = 'activation/templates/account_activated.html'


class MyActivationView(ActivationView):
    success_url = reverse_lazy('activation_complete')
