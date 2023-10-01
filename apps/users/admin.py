from django.contrib import admin
# Register your models here.
from .forms import *
from .models import *
from django.contrib.auth.admin import UserAdmin
class MyAdmin(UserAdmin):
    list_filter = ['role','is_active','is_staff','is_superuser']
    list_display = ['role','username','email','is_staff','is_superuser']
admin.site.register(User,MyAdmin)
class SellerAdmin(UserAdmin):
    list_filter = ['role','is_active']
    model = Seller
    add_form =SellerForm
    
admin.site.register(Seller,SellerAdmin)

##################################
# class CustomerAdmin(UserAdmin):
#     model = Customer
#     add_form =CustomerForm

# admin.site.register(Customer,CustomerAdmin)