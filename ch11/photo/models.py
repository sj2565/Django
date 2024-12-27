from django.db import models
from django.urls import reverse

# Create your models here.
class Album(models.Model):
    name = models.CharField('NAME', max_length=30)
    description = models.CharField('One Line Description', max_length=100, blank=True)

    class Meta:
        ordering = ('name', )   # ('ex', ) 이렇게 적어야 튜플형식

    def __str__(self):  # java로 따지면 toString()과 유사
        return self.name

    def __get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))

from photo.fields import ThumbnailImageField    # 사용자 정의 커스텀 필드(우리가 직접 만듬)

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField('TITLE', max_length=50)
    description = models.TextField('Photo Description', blank=True)

    image = ThumbnailImageField('IMAGE', upload_to='photo/%Y/%m')   # 사용자 정의 커스텀 필드
    upload_dt = models.DateTimeField('UPLOAD DATE', auto_now_add=True)

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args = (self.id, ))

