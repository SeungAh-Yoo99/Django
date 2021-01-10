from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey(
        'fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='작성자')
    # on_delete는 fcuser가 삭제 되면 어떻게 할 것인가에 대한 정책
    # CASCADE : 같이 삭제 하겠다.
    # SET_NULL : null 값으로 채운다.
    # SET_DEFAULT : 기본값 지정.
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):  # 클래스를 문자열로 변환 했을 때 어떻게 변환 할 지 정해주는 내장 함수
        return self.title

    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시글'
        verbose_name_plural = '패스트캠퍼스 게시글'  # 복수형 지정
