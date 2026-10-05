from django.contrib import admin

from .models import Farmer, Buyer, Contract

admin.site.register(Farmer)
admin.site.register(Buyer)
admin.site.register(Contract)

# Register your models here.
