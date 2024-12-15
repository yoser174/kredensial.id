from django.contrib import admin

from apps.webapp.models import PermohonanKredensial


class PermohonanKredensialAdmin(admin.ModelAdmin):
    pass


admin.site.register(PermohonanKredensial, PermohonanKredensialAdmin)
