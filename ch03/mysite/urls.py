from django.contrib import admin
from django.urls import path
from django.urls import include # cho03에서 추가됨

urlpatterns = [
    # 관리자를 위한 페이지
    path('admin/', admin.site.urls),

    path('bookmark/', include('bookmark.urls')),    # ch03에서 추가됨
    path('blog/', include('blog.urls')),]    # ch03에서 추가됨

    # 기존 소스 주석 처리
    # # 사용자를 위한 페이지 - 사용자가 지정한 views
    # path('bookmark/', BookmarkLV.as_view(), name='index'),
    #
    # # <int:pk>는 정수형 primary key를 의미할 것 같다고(-같다! 고 말하심)
    # path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),]