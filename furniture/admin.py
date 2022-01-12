from django.contrib import admin

from furniture.models import Category, Furniture
from .admin import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Furniture)
