# 관리자용 페이지 관련 기능 작성
from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)
