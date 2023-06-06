from django.contrib import admin
from .models import New,Blog,Refresh,Comment

# Register your models here.

admin.site.register(New)
admin.site.register(Blog)
admin.site.register(Refresh)
admin.site.register(Comment)
