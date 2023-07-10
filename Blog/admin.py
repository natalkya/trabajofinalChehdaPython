from django.contrib import admin
from .models import Pagina

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css')
        }

admin.site.register(Pagina, PageAdmin)
