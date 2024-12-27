from django.urls import path
from photo import views

app_name = 'photo'
urlpatterns = [
    # 호출 예시: /photo/
    path('', views.AlbumLV.as_view(), name='index'),

    # 호출 예시: /photo/album/, same as /photo/
    path('album', views.AlbumLV.as_view(), name='album_list'),

    # 호출 예시: /photo/album/99/
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),

    # 호출 예시: /photo/photo/99/
    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),
]