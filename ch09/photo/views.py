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
