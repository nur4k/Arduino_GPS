from django.contrib import admin

from main_app.models import Item, Driver


admin.site.register((Item, Driver))
