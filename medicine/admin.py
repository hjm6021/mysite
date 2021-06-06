from django.contrib import admin
from medicine.models import Medicine

# Register your models here.
@admin.register(Medicine)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "medicine_dt")
