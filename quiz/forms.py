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
        fields = ['exam', 'student_name', 'attempt_date', 'score']
        widgets = {
            'attempt_date': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
        }

class ExamSubmissionForm(forms.ModelForm):
    class Meta:
        model = ExamSubmission
        fields = ['exam_attempt', 'question', 'selected_answer']

class StudentAnswerForm(forms.ModelForm):
    class Meta:
        model = StudentAnswer
        fields = ['submission', 'question', 'selected_answer']
