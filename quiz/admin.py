from django.contrib import admin

# Register your models here.
from .models import Category,Course,Exam,Question,ExamAttempt,ExamSubmission,StudentAnswer

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(ExamAttempt)
admin.site.register(ExamSubmission)
admin.site.register(StudentAnswer)