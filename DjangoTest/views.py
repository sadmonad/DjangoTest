from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from DjangoTest.models import Blogger

def login(request):
    pass


class Login(TemplateView):
    template_name = 'login.html'


class Blogger(ListView):
    template_name = 'bloggers.html'
    queryset = Blogger.objects.all()
    context_object_name = 'bloggers'


