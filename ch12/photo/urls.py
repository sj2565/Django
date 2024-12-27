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

    # 호출 예시: /album/add/
    path('album/add/', views.AlbumPhotoCV.as_view(), name='album_add'),

    # 호출 예시: /album/change/
    path('album/change/', views.AlbumChangeLV.as_view(), name='album_change'),

    # 호출 예시: /album/<int:pk>/update/
    path('album/<int:pk>/update/', views.AlbumPhotoUV.as_view(), name='album_update'),

    # 호출 예시: /album/<int:pk>/delete/
    path('album/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album_delete'),

    # 호출 예시: /photo/add/
    path('photo/add/', views.PhotoCreateView.as_view(), name='photo_add'),

    # 호출 예시: /photo/change/
    path('photo/change/', views.PhotoChangeLV.as_view(), name='photo_change'),

    # 호출 예시: /photo/<int:pk>/update/
    path('photo/<int:pk>/update/', views.PhotoUpdateView.as_view(), name='photo_update'),

    # 호출 예시: /photo/<int:pk>/delete/
    path('photo/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name='photo_delete'),
]