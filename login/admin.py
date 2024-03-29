from django.contrib import admin
from .models import Director, Administrator, Performer

# Register your models here.
admin.site.register(Director)
admin.site.register(Administrator)
admin.site.register(Performer)