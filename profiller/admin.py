from django.contrib import admin
from profiller.models import Profil, ProfilDurum
# Register your models here.

class AdminProfil(admin.ModelAdmin):
    list_display = ('user','bio','sehir')
    list_filter =('user','bio','sehir')
    search_fields =('user','bio','sehir')

class AdminProfilDurum(admin.ModelAdmin):
    list_display = ('user_profil','yaratilma_zamani')
    list_filter =('user_profil','yaratilma_zamani','guncellenme_zamani')
    search_fields =('user_profil','yaratilma_zamani', 'guncellenme_zamani')


admin.site.register(Profil, AdminProfil)
admin.site.register(ProfilDurum, AdminProfilDurum)