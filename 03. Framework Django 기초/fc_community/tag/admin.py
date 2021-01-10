from django.contrib import admin
from .models import Tag

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    # 어느 정보를 출력하고 싶은지 명시 할 수 있다.
    list_display = ('name', )


admin.site.register(Tag, TagAdmin)
