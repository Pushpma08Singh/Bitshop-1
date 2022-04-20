from django.contrib import admin
from .models import supplied, supplier
# Register your models here.

# class supplierAdmin(admin.ModelAdmin):
#     list_display = ('supplier_name', 'supplier_id')
#     #prepopulated_fields = {'slug':('product_name',)}

# class suppliedAdmin(admin.ModelAdmin):
#     list_display = ('product_id ', 'supplied_qnt')

admin.site.register(supplied)
admin.site.register(supplier)