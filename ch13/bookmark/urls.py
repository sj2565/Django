from django.urls import path
# from bookmark.views import BookmarkLV, BookmarkDV
from bookmark import views

# 이 파일은 ch03에서 신규 생성되었다.
# blog를 위한 App Url 파일이다.

app_name = 'bookmark'

urlpatterns = [
    path('', views.BookmarkLV.as_view(), name='index'),     # ch11에 수정됨

    # <int:pk>는 정수형 primary key를 의미할 것 같다고(-같다! 고 말하심)
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'), # ch11에 수정됨

    # ch11에 신규 추가됨
    path('add/', views.BookmarkCreateView.as_view(), name='add'),
    path('change/', views.BookmarkChangeLV.as_view(), name='change'),
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name='delete'),]