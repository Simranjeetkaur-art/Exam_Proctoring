from django.urls import path
from . import views

# urlpatterns = [
#     path('category/', views.category_list, name='category_list'),
#     path('category/create/', views.category_create, name='category_create'),
#     path('category/<int:category_id>/', views.category_detail, name='category_detail'),
#     path('category/<int:category_id>/update/', views.category_update, name='category_update'),
#     path('category/<int:category_id>/delete/', views.category_delete, name='category_delete'),
#     path('exam/', views.exam_list, name='exam_list'),
#     path('exam/create/', views.exam_create, name='exam_create'),
#     path('exam/<int:exam_id>/', views.exam_detail, name='exam_detail'),
#     path('exam/<int:exam_id>/update/', views.exam_update, name='exam_update'),
#     path('exam/<int:exam_id>/delete/', views.exam_delete, name='exam_delete'),
#     path('question/', views.question_list, name='question_list'),
#     path('question/create/', views.question_create, name='question_create'),
#     path('question/<int:question_id>/', views.question_detail, name='question_detail'),
#     path('question/<int:question_id>/update/', views.question_update, name='question_update'),
#     path('question/<int:question_id>/delete/', views.question_delete, name='question_delete'),
#  ]

urlpatterns = [
    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('categories/<int:category_id>/update/', views.category_update, name='category_update'),
    path('categories/<int:category_id>/delete/', views.category_delete, name='category_delete'),
    
    # Course URLs
    path('courses/', views.course_list, name='course_list'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/<int:course_id>/update/', views.course_update, name='course_update'),
    path('courses/<int:course_id>/delete/', views.course_delete, name='course_delete'),
    
    # Exam URLs
    path('exams/', views.exam_list, name='exam_list'),
    path('exams/create/', views.exam_create, name='exam_create'),
    path('exams/<int:exam_id>/', views.exam_detail, name='exam_detail'),
    path('exams/<int:exam_id>/update/', views.exam_update, name='exam_update'),
    path('exams/<int:exam_id>/delete/', views.exam_delete, name='exam_delete'),
    
    # Question URLs
    path('questions/', views.question_list, name='question_list'),
    path('questions/create/', views.question_create, name='question_create'),
    path('questions/<int:question_id>/', views.question_detail, name='question_detail'),
    path('questions/<int:question_id>/update/', views.question_update, name='question_update'),
    path('questions/<int:question_id>/delete/', views.question_delete, name='question_delete'),

# ================================= #
    # ExamAttempt URLs
    path('exam_attempts/', views.exam_attempt_list, name='exam_attempt_list'),
    path('exam_attempts/<int:attempt_id>/', views.exam_attempt_detail, name='exam_attempt_detail'),
    path('exam_attempts/create/', views.exam_attempt_create, name='exam_attempt_create'),
    path('exam_attempts/<int:attempt_id>/update/', views.exam_attempt_update, name='exam_attempt_update'),
    path('exam_attempts/<int:attempt_id>/delete/', views.exam_attempt_delete, name='exam_attempt_delete'),

    # ExamSubmission URLs
    path('exam_submissions/', views.exam_submission_list, name='exam_submission_list'),
    path('exam_submissions/<int:submission_id>/', views.exam_submission_detail, name='exam_submission_detail'),
    path('exam_submissions/create/', views.exam_submission_create, name='exam_submission_create'),
    path('exam_submissions/<int:submission_id>/update/', views.exam_submission_update, name='exam_submission_update'),
    path('exam_submissions/<int:submission_id>/delete/', views.exam_submission_delete, name='exam_submission_delete'),

    # StudentAnswer URLs
    path('student_answers/', views.student_answer_list, name='student_answer_list'),
    path('student_answers/<int:answer_id>/', views.student_answer_detail, name='student_answer_detail'),
    path('student_answers/create/', views.student_answer_create, name='student_answer_create'),
    path('student_answers/<int:answer_id>/update/', views.student_answer_update, name='student_answer_update'),
    path('student_answers/<int:answer_id>/delete/', views.student_answer_delete, name='student_answer_delete'),
]
