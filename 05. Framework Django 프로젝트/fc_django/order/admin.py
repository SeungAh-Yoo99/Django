from django.db.models import F
from django.contrib import admin
from django.utils.html import format_html
from .models import Order
# Register your models here.

def refund(modeladmin, request, queryset): # queryset에는 체크로 선택한 주문들이 넘어온다.
    queryset.update(status='환불')
    for obj in queryset:
        obj.product.stock += obj.quantity
        obj.product.save()

refund.short_description = '환불'

class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('fcuser', 'product', 'quantity', 'styled_status')

    actions = [
        refund
    ]
    
    def styled_status(self, obj):
        if obj.status == '환불':
            return format_html('<span style="color:red">{}</span>'.format(obj.status)) # format_html 함수는 string이 아니라 진짜 tag로 사용할 수 있게 한다.
        if obj.status == '결제완료':
            return format_html('<span style="color:green">{}</span>'.format(obj.status))
        return obj.status

    styled_status.short_description = '상태' # admin 페이지에서 style_status 대신 상태라고 표시된다.

    def changelist_view(self, request, extra_context=None):
        extra_context = { 'title': '주문 목록'}
        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        order = Order.objects.get(pk=object_id)
        extra_context = { 'title': "{}의 주문 '{}' 수정".format(order.fcuser.email, order.product.name)}
        return super().changeform_view(request, object_id, form_url, extra_context)

admin.site.register(Order, OrderAdmin)