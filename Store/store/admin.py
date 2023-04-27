from django.contrib import admin

from store.models import Store
from store.forms import StoreForm


class StoreAdmin(admin.ModelAdmin):
    form = StoreForm

admin.site.register(Store, StoreAdmin)
