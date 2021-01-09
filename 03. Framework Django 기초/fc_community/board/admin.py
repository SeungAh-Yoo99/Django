from django.contrib import admin
from .models import Board

# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    # 어느 정보를 출력하고 싶은지 명시 할 수 있다.
    list_display = ('title', )


admin.site.register(Board, BoardAdmin)
