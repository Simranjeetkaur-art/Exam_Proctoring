from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Course, Exam, Question
from .forms import CategoryForm, CourseForm, ExamForm, QuestionForm

# Category Views

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_exam_form.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'category_exam_form.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_exam_form.html', {'form': form, 'creating': True})

def category_update(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail', category_id=category_id)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_exam_form.html', {'form': form, 'category': category, 'updating': True})

def category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_exam_form.html', {'category': category})

# Exam Views

def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'category_exam_form.html', {'exams': exams})

def exam_detail(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    return render(request, 'category_exam_form.html', {'exam': exam})

def exam_create(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamForm()
    return render(request, 'category_exam_form.html', {'form': form, 'creating': True})

def exam_update(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('exam_detail', exam_id=exam_id)
    else:
        form = ExamForm(instance=exam)
    return render(request, 'category_exam_form.html', {'form': form, 'exam': exam, 'updating': True})

def exam_delete(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if request.method == 'POST':
        exam.delete()
        return redirect('exam_list')
    return render(request, 'category_exam_form.html', {'exam': exam})

# Question Views

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_form.html', {'questions': questions})

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'question_form.html', {'question': question})

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'question_form.html', {'form': form, 'creating': True})

def question_update(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('question_detail', question_id=question_id)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'question_form.html', {'form': form, 'question': question, 'updating': True})

def question_delete(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        question.delete()
        return redirect('question_list')
    return render(request, 'question_form.html', {'question': question})


# Course Views

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_form.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_form.html', {'course': course})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form, 'creating': True})

def course_update(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', course_id=course_id)
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form.html', {'form': form, 'course': course, 'updating': True})

def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'course_form.html',{'course':course})