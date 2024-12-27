from django.contrib import admin
from photo.models import Album, Photo

# Register your models here.
class PhotoInline(admin.StackedInline):     # StatckedInline : 세로로 쭈욱 나열되는 형식
    model = Photo   # 일대N 관계에서 N에 해당하는 테이블을 명시한다.
    extra = 2   # 폼 셋에 들어 있는 비어 있는 폼의 개수를 지정한다.

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline, )   # Album을 보여줄 때 Photo의 정보도 같이 보여 주도록 한다.
    list_display = ('id', 'name', 'description')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')