from django.contrib import admin

# Register your models here.

from learning_logs.models import Us, Tipo, Distrito, Concelho, Freguesia, Gruposintomas, Opcoesintomas

admin.site.register(Us)
admin.site.register(Tipo)
admin.site.register(Distrito)
admin.site.register(Concelho)
admin.site.register(Freguesia)
admin.site.register(Gruposintomas)
admin.site.register(Opcoesintomas)