from venv import create
from django.db import models

# Create your models here.
class Article(models.Model):  # models.Model: 상속
    # id(primary key)는 자동으로 만들어진다
    title = models.CharField(max_length=10)
    content = models.TextField()
    create_at = models.DateField(auto_now_add=True)  # 생성시에 자동으로 추가
    