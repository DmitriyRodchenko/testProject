from django.contrib import admin

# Register your models here.

from .models import StudentClass, Student

admin.site.register(StudentClass)
admin.site.register(Student)
