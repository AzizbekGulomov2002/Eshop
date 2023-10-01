from django.contrib import admin
from .models import Cart, CartItem, Category, Marketing, Order, Product, Image, ProType, Service, Master, ImageService

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ImageInline(admin.TabularInline):
    model = Image
    fields = ["image"]

class ImageServiceInline(admin.TabularInline):
    model = ImageService
    fields = ["image"]

class ProTypeInline(admin.TabularInline):
    model = ProType
    fields = ["name","size","price",'discount',]
@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProTypeInline, ]
    list_per_page = 10
    
class ProTypeAdmin(admin.ModelAdmin):
    list_display = ["name","size","price",'discount',]
    inlines = [ImageInline, ]
    list_per_page = 10
    search_fields = ['name']
    class Meta:
        model = ProType
admin.site.register(ProType, ProTypeAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["category","master","name",'price','discount','desc']
    inlines = [ImageServiceInline, ]
    list_per_page = 10
    search_fields = ['name']
    class Meta:
        model = Service
admin.site.register(Service, ServiceAdmin)

class MasterAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_per_page = 10
    search_fields = ['name']
    class Meta:
        model = Master
admin.site.register(Master, MasterAdmin)


class MarketAdmin(admin.ModelAdmin):
    list_display = ["contact"]
    list_per_page = 10
    search_fields = ['name']
    class Meta:
        model = Marketing
admin.site.register(Marketing, MarketAdmin)



# Card and Store


class CartItemAdmin(admin.TabularInline):
    model = CartItem
    list_display = ['id', "title",  'product', "description"]
    list_filter = ['prodcut',]
    readonly_fields = ('cart', 'order', 'product', 'size', 'quantity')


class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemAdmin]
    list_display = ('session_id', 'num_of_items', 'cart_total', 'completed',
                    'id')
    list_filter = ('completed', 'created_at')
    list_per_page = 20

class OrderAdmin(admin.ModelAdmin):
    inlines = [CartItemAdmin]
    list_display = ('phone_number', 'num_of_items', 'cart_total', 'status', 'id')
    list_filter = ('status')
    list_per_page = 20


class OrderAdmin(admin.ModelAdmin):
    inlines = [CartItemAdmin]
    list_display = ('phone_number', 'num_of_items', 'cart_total', 'status', 'id')
    list_filter = ('status')
    list_per_page = 20
    

admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
