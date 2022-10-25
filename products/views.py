from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.authentication import TokenAuthentication

from utils.mixins import SerializerByMethodMixin

from products.models import Product
from products.serializers import ProductDetailSerializer, ProductSerializer
from products.permissions import isAdminOrSeller


class ProductView(SerializerByMethodMixin, ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdminOrSeller]

    queryset = Product.objects.all()

    serializer_map = {
        'GET': ProductSerializer,
        'POST': ProductDetailSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class ProductDetailView(RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdminOrSeller]

    queryset = Product.objects.all()

    serializer_class = ProductDetailSerializer
