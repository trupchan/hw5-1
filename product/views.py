from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Category, Product, Review
from .serializers import (
    CategorySerializer, CategoryWithCountSerializer,
    ProductWithReviewsSerializer, ReviewSerializer
)

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryWithCountListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWithCountSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWithReviewsSerializer 

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWithReviewsSerializer


class ProductWithReviewsListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWithReviewsSerializer


class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
