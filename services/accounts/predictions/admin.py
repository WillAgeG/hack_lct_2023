from django.contrib import admin

from .models import Predict


class PredictAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'user', 'created', 'modified')
    list_filter = ('status', 'user', 'created', 'modified')
    search_fields = ('user__email', 'status')
    readonly_fields = ('created', 'modified')


admin.site.register(Predict, PredictAdmin)
