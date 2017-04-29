# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HowdyPageView.as_view()),
    url(r'^about/$', views.AboutHowdyView.as_view()),
]
