from django.contrib import admin

# Register your models here.
from .models import Category,Course,Exam,Question

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(Question)