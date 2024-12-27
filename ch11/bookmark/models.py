from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Bookmark(models.Model):   # cf) 자바에서는 class Bookmark extends models.Model
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)
    
    # ch11에서 추가됨
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):  # cf) 자바의 toString() 메소드와 유사한 개념의 메소드
        return self.title