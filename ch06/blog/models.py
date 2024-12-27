from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager     # ch06에서 추가

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)  # 포스트 제목
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')  # 제목의 별칭
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')  # 포스트 한 줄 설명
    content = models.TextField('CONTENT')  # 포스트의 내용
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)  # 생성 일자
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)  # 수정 일자
    tags = TaggableManager(blank=True)  # ch06에서 추가됨

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # blog 앱 중에서 url 이름이 post_detail인 항목을 찾아준다.
        # args는 매개 변수를 의미한다.
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()
