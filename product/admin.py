from django.contrib import admin
from .models import FabricSoftener, Traders


@admin.register(FabricSoftener)
class SoftenerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock')
    ordering = ('name',)
    list_filter = ('name', 'price',)
    search_fields = ('name', 'price')


@admin.register(Traders)
class TradersAadmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'mobile_phone',
                    'country', 'proof_id', 'profile_picture')
    ordering = ('name',)
    list_filter = ('name', 'title', 'proof_id',)
    search_fields = ('name', 'proof_id')
