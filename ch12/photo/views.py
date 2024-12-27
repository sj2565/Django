from django.shortcuts import render
from django.views.generic import ListView, DetailView

from photo.models import Album, Photo

# Create your views here.
class AlbumLV(ListView):    # 앨범 목록 보기
    model = Album

class AlbumDV(DetailView):  # 앨범 상세 보기
    model = Album

class PhotoDV(DetailView):  # 사진 상세 보기
    model = Photo
    
# ch12에서 신규로 추가된 항목들
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

class PhotoCreateView(LoginRequiredMixin, CreateView):  # 사진을 생성/수정 하기 위한 클래스
    model = Photo
    fields = ['album', 'title', 'image', 'description']
    # success_url 속성은 요청 성공시 이동할 페이지를 지정하는 옵션이다.
    success_url = reverse_lazy('photo:index')

    def form_valid(self, form):     # 유효성 검사 통과 시 이동할 곳 지정
        form.instance.owner = self.request.user    # 소유자 지정 owner = user
        return super().form_valid(form)

class PhotoChangeLV(LoginRequiredMixin, ListView):  # 내가 소유한 사진 목록 페이지
    model = Photo
    template_name = 'photo/photo_change_list.html'

    def get_queryset(self):     # 전체 목록에서 해당 소유권이 있는 목록만 필터링
        return Photo.objects.filter(owner=self.request.user)

from mysite.views import OwnerOnlyMixin
from django.views.generic import UpdateView, DeleteView

class PhotoUpdateView(OwnerOnlyMixin, UpdateView):  # 사진 업데이트 기능, PhotoCreateView 클래스와 같은 데 메소드를 구현했냐 안했냐 차이
    model = Photo
    fields = ['album', 'title', 'image', 'description']
    success_url = reverse_lazy('photo:index')

class PhotoDeleteView(OwnerOnlyMixin, DeleteView):  # 사진 삭제 기능
    model = Photo
    success_url = reverse_lazy('photo:index')

class AlbumChangeLV(LoginRequiredMixin, ListView):  # 앨범 목록 보여주기
    model = Album
    template_name = 'photo/album_change_list.html'

    def get_queryset(self):
        return Album.objects.filter(owner = self.request.user)  # 내가 소유한 소유자와 요청한 유저가 동일한지 판단

class AlbumDeleteView(OwnerOnlyMixin, DeleteView):  # 앨범 삭제 기능
    model = Album
    success_url = reverse_lazy('photo:index')

from photo.forms import PhotoInlineFormSet
from django.shortcuts import redirect

class AlbumPhotoCV(LoginRequiredMixin, CreateView): # 앨범 생성 기능
    model = Album
    fields = ['name', 'description']
    success_url = reverse_lazy('photo:index')

    # context는 업무 로직에서 처리하는 데이터 모음/집합채
    # ** kwargs는 keyword arguments (xx은 aa이다.)를 의미하는 사전
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 업로드가 크면 post방식으로만 가능하기에 post 선호
        if self.request.POST:   # 전송 방식이 post이면
            # context에 'formset'이라는 속성을 바인딩한다.  (setter)
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES)
        else :                  # get 방식이면
            context['formset'] = PhotoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']    # getter
        for photoform in formset:   # 각 사진마다 가지는 폼들의 소유자 셋팅
            photoform.instance.owner = self.request.user    # 소유자 지정 owner = user

        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class AlbumPhotoUV(OwnerOnlyMixin, UpdateView): # 앨범 수정 기능
    model = Album
    fields = ['name', 'description']
    success_url = reverse_lazy('photo:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
                                                                            # 생성과 다르게 instance=self.object 추가
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:  # get 방식이면                   # 생성과 다르게 instance=self.object 추가
            context['formset'] = PhotoInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        for photoform in formset:  # 각 사진마다 가지는 폼들의 소유자 셋팅
            photoform.instance.owner = self.request.user  # 소유자 지정 owner = user

        if formset.is_valid():
            form.instance.owner = self.request.user #수정에서는 삭제
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))