from django.contrib import admin
from django.utils.html import format_html
from django.contrib.humanize.templatetags.humanize import intcomma # setting app에 humanize가 추가되어 있어야 한다.
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_format', 'styled_stock')

    def price_format(self, obj):
        price = intcomma(obj.price)
        return '{} 원'.format(price)

    def styled_stock(self, obj):
        if obj.stock <= 50:
            return format_html('<b><span style="color:red">{} 개</span></b>'.format(intcomma(obj.stock)))
        return '{} 개'.format(intcomma(obj.stock))

    price_format.short_description = '가격'    
    styled_stock.short_description = '재고'

    def changelist_view(self, request, extra_context=None):
        extra_context = { 'title': '상품 목록'}
        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        product = Product.objects.get(pk=object_id)
        extra_context = { 'title': '상품명: {} 수정'.format(product.name)}
        return super().changeform_view(request, object_id, form_url, extra_context)

admin.site.register(Product, ProductAdmin)