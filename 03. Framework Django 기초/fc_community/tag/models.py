from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='태그명')
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):  # 클래스를 문자열로 변환 했을 때 어떻게 변환 할 지 정해주는 내장 함수
        return self.name

    class Meta:
        db_table = 'fastcampus_tag'
        verbose_name = '패스트캠퍼스 태그'
        verbose_name_plural = '패스트캠퍼스 태그'  # 복수형 지정
