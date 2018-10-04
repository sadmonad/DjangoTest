from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
from DjangoTest.videos.models import Video


class VideoView(PermissionRequiredMixin, ListView):
    permission_required = 'view_video'
    template_name = 'templates/videos.html'
    queryset = Video.objects.all()
    context_object_name = 'videos'
