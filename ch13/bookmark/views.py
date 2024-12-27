from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

# Create your views here.
class BookmarkLV(ListView): # Bookmark 목록 보기 용도
    model = Bookmark

class BookmarkDV(DetailView): # Bookmark 항목 중 1개 보기
    model = Bookmark

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from django.urls import reverse_lazy

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    # fields는 폼을 만들 때 사용할 필드를 지정한다.
    fields = ['title', 'url']
    # success_url는 처리 성공 시 이동할 곳을 저장해 준다.
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form): # 유효성 검사 시 호출이 된다.
        # 요청 객체의 사용자 정보를 폼 객체 소유자로 지정한다.
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookmarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self): # 출력되는 목록을 오버라이딩하고자 할 때 사용된다.
        # 소유자와 요청 사용자 정보가 동일한 내용만 추출한다.
        return Bookmark.objects.filter(owner=self.request.user)

from mysite.views import OwnerOnlyMixin
from django.views.generic import UpdateView
from django.views.generic import DeleteView

class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')