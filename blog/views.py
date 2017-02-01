from django.views import generic
from django.shortcuts import render
from blog import models

class BlogIndex(generic.ListView):
    template_name = "home.html"
    context_object_name = 'blogs_list'
    paginate_by = 2

    def get_queryset(self):
        return models.Entry.objects.published()

