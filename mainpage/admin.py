from django.contrib import admin
from .models import Employee, Departament

# Register your models here.
admin.site.register(Departament)
admin.site.register(Employee)