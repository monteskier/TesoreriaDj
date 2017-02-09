from django.contrib import admin
from .models import Entitat
from .models import Moviments
from django.forms import Textarea
from django.db import models
from django.utils.html import format_html


class EntitatAdmin(admin.ModelAdmin):
    list_display = ('codi','nom','email','saldo_inicial','saldo_ajuntament','diferencia');
    search_fields = ['codi','nom',];
    
    def diferencia(self, obj):
        return (obj.saldo_inicial - obj.saldo_ajuntament);
            

class MovimentsAdmin(admin.ModelAdmin):
    list_display = ('codiEnt','data_mov','operacio','accio','_import','conformitat');
    
admin.site.site_title = 'Tesoreria AjSVC'
admin.site.site_header = 'Tesoreria AjSVC'
admin.site.register(Moviments, MovimentsAdmin);
admin.site.register(Entitat, EntitatAdmin);

    