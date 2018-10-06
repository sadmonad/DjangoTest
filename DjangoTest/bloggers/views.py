from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from DjangoTest.bloggers.models import Blogger

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BloggerView(PermissionRequiredMixin, ListView):
    permission_required = 'DjangoTest.view_blogger'
    template_name = 'templates/bloggers.html'
    queryset = Blogger.objects.all()
    context_object_name = 'bloggers'
    redirect_field_name = ''


class BloggerDetailView(DetailView):
    template_name_suffix = ''
    template_name = 'templates/detail_blogger.html'
    model = Blogger
    context_object_name = 'blogger'
    slug_url_kwarg = 'nick'
    slug_field = 'nick'


class BloggerCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'DjangoTest.add_blogger'
    template_name = 'templates/add_blogger.html'
    template_name_suffix = ''
    model = Blogger
    fields = ['nick', 'reputation', 'registration_date', 'subscribers_count', 'profit']
    success_url = reverse_lazy('bloggers')


class BloggerUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'DjangoTest.change_blogger'
    template_name = 'templates/update_blogger.html'
    template_name_suffix = ''
    model = Blogger
    fields = ['nick', 'reputation', 'registration_date', 'subscribers_count', 'profit']
    slug_url_kwarg = 'nick'
    slug_field = 'nick'
    success_url = reverse_lazy('bloggers')


class BloggerDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'DjangoTest.delete_blogger'
    template_name = 'templates/delete_blogger.html'
    template_name_suffix = ''
    model = Blogger
    slug_url_kwarg = 'nick'
    slug_field = 'nick'
    success_url = reverse_lazy('bloggers')