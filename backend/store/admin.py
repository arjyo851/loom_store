from django.contrib import admin
from .models import Store, StoreStatusLog, StoreTiming, StoreReport

# Register your models here.
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('store_id', 'timezone_str')
    list_filter = ('timezone_str',)
    search_fields = ('store_id',)

@admin.register(StoreTiming)
class StoreTimingAdmin(admin.ModelAdmin):
    list_display = ('store', 'day', 'start_time', 'end_time')
    list_filter = ('day',)
    search_fields = ('store__store_id',)  # Use store__ prefix to access related field

@admin.register(StoreStatusLog)
class StoreStatusLogAdmin(admin.ModelAdmin):
    list_display = ('store', 'status', 'timestamp')
    list_filter = ('status',)
    search_fields = ('store__store_id',)  # Use store__ prefix to access related field

@admin.register(StoreReport)
class StoreReportAdmin(admin.ModelAdmin):
    list_display = ('store', 'status', 'report_url')
    list_filter = ('status',)
    search_fields = ('store__store_id',)  # Use store__ prefix to access related field
