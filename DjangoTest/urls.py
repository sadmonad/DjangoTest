from django.urls import path
from django.conf.urls import url
from DjangoTest.views import Login, Blogger

urlpatterns = [
    path('login/', Login.as_view()),
    path('bloggers/', Blogger.as_view()),
]
