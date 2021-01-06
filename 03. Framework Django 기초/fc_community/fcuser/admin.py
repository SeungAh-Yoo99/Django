from django.contrib import admin
from .models import Fcuser  # model 안에 있는 Fcuser 클래스를 가져온다.

# Register your models here.


class FcuserAdmin(admin.ModelAdmin):
    # 어느 정보를 출력하고 싶은지 명시 할 수 있다.
    list_display = ('username', 'password', 'useremail')


admin.site.register(Fcuser, FcuserAdmin)
