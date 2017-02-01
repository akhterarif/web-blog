from django.conf.urls import url
from blog import views, feed

app_name="blog"

urlpatterns = [
    url(r'^blog/feed/$', feed.LatestPosts(), name="feed"),
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name="blog_detail"),
]
