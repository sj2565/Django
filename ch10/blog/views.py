from django.shortcuts import render
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView \
    ,DayArchiveView, TodayArchiveView

from blog.models import Post

from django.views.generic import TemplateView

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

class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        # 모델 매니저를 이용한 데이터 필터링
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 템플릿 문서에서 {{tagname}}라는 코드로 참조될 수 있다.
        context['tagname'] = self.kwargs['tag']
        return context

# pdf 143page
from django.views.generic import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

class SearchFormView(FormView):

    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):     # 유효성 검사를 통과한 다음 호출이 되는 메소드, callback 함수

        # cleaned_data 메소드는 유효성 검사를 통과한 다음 해당 필드들의 정보를 보여준다.
        searchWord = form.cleaned_data['search_word']
        # JSP형식 : String searchWord = request.getParameter("Search_Word");
        
        # objects는 모델 매니저 이름
        post_list = Post.objects.filter(Q(title__icontains=searchWord) |
Q(description__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()
        context = {}    # 템플릿에서 참조될 컨택스트 정보
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list
        return render(self.request, self.template_name, context) # No Redirection
