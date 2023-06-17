from django import forms
from .models import Category, Course, Exam, Question,ExamAttempt, ExamSubmission, StudentAnswer


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class ExamAttemptForm(forms.ModelForm):
    class Meta:
        model = ExamAttempt
        exclude = ('attempt_date',)

class ExamSubmissionForm(forms.ModelForm):
    class Meta:
        model = ExamSubmission
        fields = '__all__'

class StudentAnswerForm(forms.ModelForm):
    class Meta:
        model = StudentAnswer
        fields = '__all__'




