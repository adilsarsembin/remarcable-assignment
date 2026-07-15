from django.urls import include, path
from django.views.generic import TemplateView

from products import views

api_patterns = [
    path("products/", views.ProductList.as_view(), name="product-list"),
    path("categories/", views.CategoryList.as_view(), name="category-list"),
    path("tags/", views.TagList.as_view(), name="tag-list"),
]

urlpatterns = [
    path("", TemplateView.as_view(template_name="products/index.html")),
    path("api/", include(api_patterns)),
]
    