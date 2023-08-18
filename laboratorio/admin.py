from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

# Register your models here.
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "laboratorio")

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "laboratorio", "get_fabricacion_year","p_costo", "p_venta")

    ordering = ('nombre', 'laboratorio')

    list_display_links = ('nombre', 'laboratorio')

    list_filter = ('nombre', 'laboratorio')
    
    def get_fabricacion_year(self, obj):
        return obj.f_fabricacion.year

    get_fabricacion_year.short_description = 'F FABRICACION'

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)

