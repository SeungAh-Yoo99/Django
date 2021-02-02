from django.contrib import admin
from django.utils.html import format_html
from .models import Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('fcuser', 'product', 'styled_status')
    
    def styled_status(self, obj):
        if obj.status == '환불':
            return format_html('<span style="color:red">{}</span>'.format(obj.status)) # format_html 함수는 string이 아니라 진짜 tag로 사용할 수 있게 한다.
        if obj.status == '결제완료':
            return format_html('<span style="color:green">{}</span>'.format(obj.status))
        return obj.status

    styled_status.short_description = '상태' # admin 페이지에서 style_status 대신 상태라고 표시된다.

admin.site.register(Order, OrderAdmin)
