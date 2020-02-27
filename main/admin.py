from django.contrib import admin
from .models import ObjectClassModel


@admin.register(ObjectClassModel)
class ObjectClassAdmin(admin.ModelAdmin):
    pass
