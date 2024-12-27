from django.contrib import admin
from blog.models import Post

@admin.register(Post)
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt', 'tag_list')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    
    # ch06에서 추가됨
    # prefetch_related 메소드는 N대N 관계의 쿼리 성능을 높이기 위해 사용하는 메소드
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        # 모든 태그 목록을 콤마로 연결해서 보여준다.
        return ', '.join(o.name for o in obj.tags.all())