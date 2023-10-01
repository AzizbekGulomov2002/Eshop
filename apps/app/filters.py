from django_filters import rest_framework as filters

from apps.app.models import *
import django_filters

class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ['category', 'count']
        
class ProTypeFilter(filters.FilterSet):
    class Meta:
        model = ProType
        fields = ['type', 'name','size','price','discount']        
        
class ServiceFilter(filters.FilterSet):
    class Meta:
        model = Service
        fields = ['category', 'master','name','price','discount'] 
        
        
