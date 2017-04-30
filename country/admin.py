from django.contrib import admin

from .models import Country, ExternalData, Project

class CountryAdmin(admin.ModelAdmin):
    model = Country
    filter_horizontal = ('external_data', 'projects', )

admin.site.register(ExternalData)
admin.site.register(Project)
admin.site.register(Country, CountryAdmin)
