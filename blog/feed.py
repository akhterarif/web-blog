from django.contrib.syndication.views import Feed
from blog.models import Entry

class LatestPosts(Feed):
    title  = "Simple blog"
    link = "/feed/"
    description = "A simple Blog by Django"

    def items(self):
        return Entry.objects.published()[:5]
