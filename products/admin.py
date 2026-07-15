from django.contrib import admin

from products.models import Category, Product, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["name"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "created_at", "tags_list"]
    list_filter = ["category", "tags"]
    search_fields = ["name", "description"]
    filter_horizontal = ["tags"]
    list_select_related = ["category"]
    ordering = ["-created_at"]
    readonly_fields = ["created_at", "updated_at"]

    @admin.display(description="tags")
    def tags_list(self, obj):
        return ", ".join(t.name for t in obj.tags.all())

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related("tags")
