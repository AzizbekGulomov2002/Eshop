from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
class SellerForm(UserCreationForm):
    class Meta:
        model = Seller
        fields = "__all__"
# class CustomerForm(UserCreationForm):
#     class Meta:
#         model = Customer
#         fields = "__all__"
