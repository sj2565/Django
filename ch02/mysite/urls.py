from django.contrib import admin
from django.urls import path
from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    # 관리자를 위한 페이지
    path('admin/', admin.site.urls),
    # 사용자를 위한 페이지 - 사용자가 지정한 views
    path('bookmark/', BookmarkLV.as_view(), name='index'),

    # <int:pk>는 정수형 primary key를 의미할 것 같다고(-같다! 고 말하심)
    path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),]