from django.contrib import admin
from django.urls import path
from django.urls import include # ch03에서 추가됨
from mysite.views import HomeView # ch04에서 추가됨

from django.conf.urls.static import static # ch09에서 추가됨
from django.conf import settings    # ch09에서 추가됨

from mysite.views import UserCreateView, UserCreateDoneTV

urlpatterns = [
    # 관리자를 위한 페이지
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'), # ch04에서 추가됨

    path('bookmark/', include('bookmark.urls')),    # ch03에서 추가됨
    path('blog/', include('blog.urls')),    # ch03에서 추가됨

    path('photo/', include('photo.urls')),  # ch09에서 추가됨

    # acoounts 항목들을 인증 기능(ch10)에서 추가됨
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register')

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  # ch09에서 추가됨
    # Django의 보안상의 문제로 인해 새롭게 업로드 되는 이미지나 css, js파일과 같은 정적
    # 파일들의 경로를 실시간으로 읽어오지 못하기 때문에 뒤로 경로를 따로 설정해 주었다.

    # 기존 소스 주석 처리
    # # 사용자를 위한 페이지 - 사용자가 지정한 views
    # path('bookmark/', BookmarkLV.as_view(), name='index'),
    #
    # # <int:pk>는 정수형 primary key를 의미할 것 같다고(-같다! 고 말하심)
    # path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),]