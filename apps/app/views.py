from django.shortcuts import render

from rest_framework import viewsets
from .models import Category, Product, Service,ProType,Image, Master, ImageService
from .serializers import CategorySerializer, ServiceSerializer, ProductSerializer, MasterSerializer, ProTypeSerializer,ImageSerializer, ImageServiceSerializer


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