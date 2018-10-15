from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from DjangoTest.accounts.registration import views as registration_views
from DjangoTest.accounts.activation import views as activation_views
from DjangoTest.accounts.profile import views as profile_views
from DjangoTest.bloggers import views as bloggers_views
from DjangoTest.videos import views as videos_views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='profile/templates/login.html'), name='login'),
    path('accounts/profile/', profile_views.Profile.as_view(), name='profile'),

    path('accounts/register/', registration_views.MyRegistrationView.as_view(), name='register'),
    path('accounts/register/complete', registration_views.RegistrationCompleteView.as_view(), name='registration_complete'),

    url(r'^accounts/activate/(?P<activation_key>[-:\w]+)/$', activation_views.MyActivationView.as_view(), name='activate'),
    path('accounts/activate/complete', activation_views.AccountActivatedView.as_view(), name='activation_complete'),

    path('bloggers/', bloggers_views.BloggerView.as_view(), name='bloggers'),
    path('bloggers/add', bloggers_views.BloggerCreateView.as_view(), name='create_blogger'),
    path('bloggers/<slug:nick>', bloggers_views.BloggerDetailView.as_view(), name='blogger_detail'),
    path('bloggers/<slug:nick>/videos', bloggers_views.BloggerVideos.as_view(), name='blogger_videos'),
    path('bloggers/<slug:nick>/update', bloggers_views.BloggerUpdateView.as_view(), name='update_blogger'),
    path('bloggers/<slug:nick>/delete', bloggers_views.BloggerDeleteView.as_view(), name='delete_blogger'),

    path('videos/', videos_views.VideoView.as_view(), name='videos'),
    path('videos/add', videos_views.VideoCreateView.as_view(), name='create_video'),
    path('videos/<int:pk>', videos_views.VideoDetailView.as_view(), name='video_detail'),
    path('videos/<int:pk>/update', videos_views.VideoUpdateView.as_view(), name='update_video'),
    path('videos/<int:pk>/delete', videos_views.VideoDeleteView.as_view(), name='delete_video'),

    path('admin/', admin.site.urls),
]
