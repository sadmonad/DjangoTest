from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'profile/templates/profile.html'
    redirect_field_name = ''
