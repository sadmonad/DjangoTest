from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from DjangoTest.models import Blogger


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    redirect_field_name = ''


class Blogger(PermissionRequiredMixin, ListView):
    permission_required = 'view_blogger'
    template_name = 'bloggers.html'
    queryset = Blogger.objects.all()
    context_object_name = 'bloggers'

