from django.contrib import admin

from warehouse.models import Warehouse
from warehouse.forms import WareForm


class WareAdmin(admin.ModelAdmin):
    form = WareForm


admin.site.register(Warehouse, WareAdmin)
