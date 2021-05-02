from django.contrib import admin
from investment.models import Post, Category

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category_id", "modify_dt")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "create_dt")
    prepopulated_fields = {"slug": ("name",)}