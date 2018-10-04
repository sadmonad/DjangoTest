from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
from DjangoTest.bloggers.models import Blogger


class Blogger(PermissionRequiredMixin, ListView):
    permission_required = 'view_blogger'
    template_name = 'templates/bloggers.html'
    queryset = Blogger.objects.all()
    context_object_name = 'bloggers'
