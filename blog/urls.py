from django.conf.urls import urls
from blog import views
from django.urls import path


urlpatterns=[
    path('/',views.PostListView.as_view(),name="post_list"),
    path('/about', views.AboutView.as_view(),name="about"),
]
