from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.contrib import admin
from django.utils.html import format_html
from django.db import transaction
from .models import Order
# Register your models here.

def refund(modeladmin, request, queryset): # queryset에는 체크로 선택한 주문들이 넘어온다.
    with transaction.atomic():
        qs = queryset.filter(~Q(status='환불'))
        ct = ContentType.objects.get_for_model(queryset.model)
        for obj in qs:
            obj.product.stock += obj.quantity
            obj.product.save()

            LogEntry.objects.log_action(
                user_id=request.user.id,
                content_type_id=ct.pk,
                object_id=obj.pk,
                object_repr='{}의 {} 주문 환불'.format(obj.fcuser, obj.product),
                action_flag=CHANGE,
                change_message='주문 환불'
            )
        qs.update(status='환불')

refund.short_description = '환불'

class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('fcuser', 'product', 'quantity', 'styled_status', 'action')
    change_list_template = 'admin/order_change_list.html'

    actions = [
        refund
    ]

    def action(self, obj):
        if obj.status != '환불':
            return format_html('<input type="button" value="환불" onclick="order_refund_submit({})" class="btn btn-primary btm-sm">'.format(obj.id))
    
    def styled_status(self, obj):
        if obj.status == '환불':
            return format_html('<span style="color:red">{}</span>'.format(obj.status)) # format_html 함수는 string이 아니라 진짜 tag로 사용할 수 있게 한다.
        if obj.status == '결제완료':
            return format_html('<span style="color:green">{}</span>'.format(obj.status))
        return obj.status

    styled_status.short_description = '상태' # admin 페이지에서 style_status 대신 상태라고 표시된다.

    def changelist_view(self, request, extra_context=None):
        extra_context = { 'title': '주문 목록'}

        if request.method == 'POST':
            obj_id = request.POST.get('obj_id')
            if obj_id:
                qs = Order.objects.filter(pk=obj_id)
                ct = ContentType.objects.get_for_model(qs.model)
                for obj in qs:
                    obj.product.stock += obj.quantity
                    obj.product.save()

                    LogEntry.objects.log_action(
                        user_id=request.user.id,
                        content_type_id=ct.pk,
                        object_id=obj.pk,
                        object_repr='{}의 {} 주문 환불'.format(obj.fcuser, obj.product),
                        action_flag=CHANGE,
                        change_message='주문 환불'
                    )
                qs.update(status='환불')

        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        order = Order.objects.get(pk=object_id)
        extra_context = { 'title': "{}의 주문 '{}' 수정".format(order.fcuser.email, order.product.name)}
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_and_continue'] = False
        return super().changeform_view(request, object_id, form_url, extra_context)

admin.site.register(Order, OrderAdmin)