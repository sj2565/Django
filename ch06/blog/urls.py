from django.urls import path, re_path
from blog import views

# 이 파일은 ch03에서 신규 생성된다.
# blog를 위한 App Url파일이다.

app_name = 'blog'

urlpatterns = [
    # 호출 예시) /blog/
    path('', views.PostLV.as_view(), name='index'),

    # 호출 예시) /blog/post/
    path('post/', views.PostLV.as_view(), name='post_list'),

    # 호출 예시) /blog/post/xxx/    정규식
    # r'정규표현식'의 r은 raw string의 줄인 말
    # cf) '\d'는 숫자 1개를 의미하고, r'\d'는 역슬래시 1개와 d를 찾아준다.
    re_path(r'^post/(?P<slug>[-\w]+)$', views.PostDV.as_view(), name='post_detail'),

    # 호출 예시) /blog/archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),

    # 호출 예시) /blog/archive/2021/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),

    # 호출 예시) /blog/archive/2021/nov/
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),

    # 호출 예시) /blog/archive/2021/nov/10/
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),

    # 호출 예시) /blog/archive/today/
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),

    # 호출 예시) /blog/tag/
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),

    # 호출 예시) /blog/tag/tagname/
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
]