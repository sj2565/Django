from django.contrib import admin

# Register your models here.
from django.contrib import admin
# bookmark 폴더의 models 파일(모듈)에 들어있는 Bookmark 클래스를 사용할 것
from bookmark.models import Bookmark

# Register your models here.
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')