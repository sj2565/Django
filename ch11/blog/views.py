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

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

# reverse_lazy() 함수는 reverse() 함수와 동일한 개념이지만
# urls.py 파일이 먼저 실행되고, 이후에 조금 늦게 view.py파일이 동작하도록 하는 함수이다.
from django.urls import reverse_lazy

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tags']
    # initial 속성은 폼 양식에 들어갈 기본 값을 지정한다.
    initial = {'slug':'auto-filling-do-not-input'}
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)

from mysite.views import OwnerOnlyMixin
from django.views.generic import UpdateView
from django.views.generic import DeleteView

class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tags']
    success_url = reverse_lazy('blog:index')

class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')