from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from DjangoTest.videos.models import Video


class VideoView(PermissionRequiredMixin, ListView):
    permission_required = 'view_video'
    template_name = 'templates/videos.html'
    queryset = Video.objects.all()
    context_object_name = 'videos'


class VideoDetailView(DetailView):
    template_name_suffix = ''
    template_name = 'templates/detail_video.html'
    model = Video
    context_object_name = 'video'
    slug_url_kwarg = 'video'
    slug_field = 'video'


class VideoCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'DjangoTest.add_video'
    template_name_suffix = ''
    template_name = 'templates/add_video.html'
    model = Video
    fields = ['caption', 'uploading_date', 'duration_min', 'genre',
              'views_count', 'likes_count', 'comments_count', 'is_private']
    success_url = reverse_lazy('videos')
    redirect_field_name = ''


class VideoUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'DjangoTest.change_video'
    template_name_suffix = ''
    template_name = 'templates/update_video.html'
    model = Video
    fields = ['caption', 'genre', 'is_private']
    slug_url_kwarg = 'video'
    slug_field = 'video'
    success_url = reverse_lazy('videos')


class VideoDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'DjangoTest.delete_video'
    template_name_suffix = ''
    template_name = 'templates/delete_video.html'
    model = Video
    slug_url_kwarg = 'video'
    slug_field = 'video'
    success_url = reverse_lazy('videos')