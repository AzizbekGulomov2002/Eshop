from django.shortcuts import render

from rest_framework import viewsets
from .models import Category, Marketing, Order, Product, Service,ProType,Image, Master, ImageService
from .serializers import CategorySerializer, MarketSerializer, ServiceSerializer, ProductSerializer, MasterSerializer, ProTypeSerializer,ImageSerializer, ImageServiceSerializer


from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.urls.exceptions import Resolver404
from rest_framework import generics, status
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from django.shortcuts import get_object_or_404
from rest_framework import pagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from apps.app.filters import  ProductFilter, ProTypeFilter


from rest_framework.decorators import api_view
# Product Page
class ProductPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50
    filterset_class = Product

    def get_paginated_response(self, data):
        return Response({
            'page_size': self.page_size,
            'total_objects': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page_number': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })

# Product Type Page
class ProTypePagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50
    filterset_class = ProType

    def get_paginated_response(self, data):
        return Response({
            'page_size': self.page_size,
            'total_objects': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page_number': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    # filterset_class = StatusFilter
    search_fields = ['name']
    filterset_fields = ('status', )
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = ProductPagination
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProTypeViewSet(viewsets.ModelViewSet):
    queryset = ProType.objects.all().order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = ProTypePagination
    filterset_class = ProTypeFilter
    queryset = ProType.objects.all()
    serializer_class = ProTypeSerializer
    
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
class ImageServiceViewSet(viewsets.ModelViewSet):
    queryset = ImageService.objects.all().order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ImageService.objects.all()
    serializer_class = ImageServiceSerializer
    
class MasterViewSet(viewsets.ModelViewSet):
    queryset = Master.objects.all().order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Master.objects.all()
    serializer_class = MasterSerializer
    
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    
class MarketViewSet(viewsets.ModelViewSet):
    queryset = Marketing.objects.all().order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Marketing.objects.all()
    serializer_class = MarketSerializer
    
    
    
# Order



@api_view(['POST'])
def change_status(request, *args, **kwargs):
    status = request.data.get('status')
    id = request.data.get('id')
    order = get_object_or_404(Order, id=id)
    order.status = status
    order.save()
    return Response({
        "msg": "Success",
        "status": 200
    }, status=200)

@api_view(['GET'])
def count_products(request, *args, **kwargs):
    product_images = Image.objects.all()
    number = 0
    data = [{
        'color_id': None,
        'product_id': None
    }]
    for i in product_images:
        res = {
            'color_id': i.color_id,
            'product_id': i.product_id,
        }
        # if i.color_id != data['color_id'] and i.product_id != data['product_id']:
        if res not in data:
            result = product_images.filter(color_id=i.color_id, product_id=i.product_id)
            data.append(res)
            if result.exists():
                number += 1
    # print(number)
    # result = ProductImage.objects.values('product', 'color').annotate(dcount=Count('product')).order_by()
    # print(result)
    return Response({
        "msg": number,
        "status": 200
    }, status=200)
    
    
    
    
