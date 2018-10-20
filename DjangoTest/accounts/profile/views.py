from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...bloggers.models import Blogger
from ..profile.models import Profile


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/templates/profile.html'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_id = Profile.objects.get(pk=self.request.user.id)
        context['user_nick'] = Blogger.objects.get(profile_id=profile_id).nick
        return context
