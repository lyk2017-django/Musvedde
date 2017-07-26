from django.views import generic
from .models import Post, Category
from datetime import datetime, timedelta

# Create your views here.


class HomeView(generic.ListView):
    def get_queryset(self):
        one_week_ago = datetime.today() - timedelta(days=7)
        return Post.objects.filter(created_at__lte=one_week_ago)


class CategoryView(generic.DetailView):
    def get_queryset(self):
        return Category.objects.all()


class NewsView(generic.DetailView):
    def get_queryset(self):
        return Post.objects.filter()

