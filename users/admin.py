from django.contrib import admin
from .models import CustomUser, Student


admin.site.register(CustomUser)
admin.site.register(Student)
