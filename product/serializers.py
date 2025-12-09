from rest_framework import serializers
from .models import Category, Product, Review
from django.db.models import Avg

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=255,
        required=True,
        allow_blank=False
    )

    class Meta:
        model = Category
        fields = ['id', 'name']

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("Категория с таким названием уже существует.")
        return value


class ReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField(required=True, allow_blank=False)
    stars = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Review
        fields = ['id', 'text', 'product', 'stars']

    def validate_product(self, value):
        if not Product.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Продукт не найден.")
        return value


class ProductWithReviewsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, allow_blank=False)
    description = serializers.CharField(required=True, allow_blank=False)
    price = serializers.FloatField(min_value=0)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'reviews', 'rating']

    def get_rating(self, obj):
        avg = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        return round(avg, 2) if avg else None

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Название продукта должно быть не меньше 2 символов.")
        return value

    def validate_description(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Описание продукта слишком короткое.")
        return value


