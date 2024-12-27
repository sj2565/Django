from django.urls import path
from bookmark.views import BookmarkLV, BookmarkDV

# 이 파일은 ch03에서 신규 생성되었다.
# blog를 위한 App Url 파일이다.

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),

    # <int:pk>는 정수형 primary key를 의미할 것 같다고(-같다! 고 말하심)
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),]