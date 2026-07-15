from django.db.models import Q
from rest_framework import generics

from products.models import Category, Product, Tag
from products.serializers import CategorySerializer, ProductSerializer, TagSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.order_by("-id")
    serializer_class = CategorySerializer


class TagList(generics.ListAPIView):
    queryset = Tag.objects.order_by("-id")
    serializer_class = TagSerializer


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        params = self.request.query_params
        qs = (
            Product.objects.select_related("category")
            .prefetch_related("tags")
            .order_by("-id")
        )

        q = params.get("q")
        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(description__icontains=q))

        category = params.get("category")
        if category and category.isdigit():
            qs = qs.filter(category_id=category)

        tags = [t for t in params.getlist("tag") if t.isdigit()]
        if tags:
            qs = qs.filter(tags__in=tags).distinct()

        return qs
