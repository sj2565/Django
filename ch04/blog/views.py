from django.shortcuts import render
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView \
    ,DayArchiveView, TodayArchiveView

from blog.models import Post

# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2     # 한 페이지에 두 개씩 보여줘라, pageSize

class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    model_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    model_format = '%m'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'
    model_format = '%m'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'