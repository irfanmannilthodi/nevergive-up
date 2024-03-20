from django.contrib import admin

# Register your models here.
from .models import Product,Category

class CtegoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CtegoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)