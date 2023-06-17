from datetime import timezone
import os
from django.db import models
from users.models import User

# class Category(models.Model):
#     category_name = models.CharField(max_length=100, unique=True)
#     category_description = models.CharField(max_length=100, blank=True)
#     category_status = models.BooleanField(default=True)
#     date_created = models.DateTimeField(auto_now_add=True, blank=True)

#     def __str__(self):
#         return self.category_name

#     class Meta:
#         managed = True
#         db_table = 'category'
#         verbose_name_plural = "Categories"


# class Course(models.Model):
#     course_name = models.CharField(max_length=100, unique=True)
#     course_description = models.CharField(max_length=100, blank=True)
#     course_image = models.ImageField(upload_to='course_images', blank=True, default='default_image.png')
#     course_status = models.BooleanField(default=True)
#     date_created = models.DateTimeField(auto_now_add=True, blank=True)
#     course_category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.course_name

#     def save(self, *args, **kwargs):
#         # Delete the old image file if it exists
#         if self.id:
#             old_instance = Course.objects.get(id=self.id)
#             if self.course_image != old_instance.course_image#                 old_instance.course_image.delete(save=False

#         # Set the filename of the course_image to the course_name
#         filename = f"{self.course_name}{os.path.splitext(self.course_image.name)[1]}"
#         self.course_image.name = filename
#         super().save(*args, **kwargs)

#     def delete(self, *args, **kwargs):
#         # Delete the course image file if it exists
#         self.course_image.delete(save=False)

#         super().delete(*args, **kwargs)

#     class Meta:
#         managed = True
#         db_table = 'course'


# class Exam(models.Model):
#     exam_name = models.CharField(max_length=100, unique=True)
#     exam_description = models.CharField(max_length=100, blank=True)
#     exam_start_date = models.DateTimeField(blank=True)
#     exam_duration = models.IntegerField(blank=True)
#     exam_status = models.BooleanField(default=True)
#     date_created = models.DateTimeField(auto_now_add=True, blank=True)
#     exam_course = models.ForeignKey(Course, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.exam_name

#     class Meta:
#         managed = True
#         db_table = 'exam'


# class Question(models.Model):
#     question_name = models.CharField(max_length=100, unique=True)
#     question_text = models.CharField(max_length=200, blank=True)
#     option1 = models.CharField(max_length=100, blank=True)
#     option2 = models.CharField(max_length=100, blank=True)
#     option3 = models.CharField(max_length=100, blank=True)
#     option4 = models.CharField(max_length=100, blank=True)
#     correct_answer = models.CharField(max_length=100, blank=True)
#     question_status = models.BooleanField(default=True)
#     question_exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.question_name

#     class Meta:
#         managed = True
#         db_table = 'question'



# class ExamAttempt(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  
#     exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
#     start_time = models.DateTimeField(auto_now_add=True)
#     end_time = models.DateTimeField(null=True, blank=True)
#     is_completed = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.exam.exam_name} - {self.user.name}"

#     def save(self, *args, **kwargs):
#         if self.is_completed and not self.end_time:
#             self.end_time = timezone.now()
#         super().save(*args, **kwargs)

#     class Meta:
#         managed = True
#         db_table = 'exam_attempt'

# # from django.db import models

# # class ExamAttempt(models.Model):
# #     exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
# #     student = models.ForeignKey(User, on_delete=models.CASCADE)
# #     attempt_date = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return f"Attempt for {self.exam.exam_name} by {self.user.name}"

# #     class Meta:
# #         managed = True
# #         db_table = 'exam_attempt'


# class ExamSubmission(models.Model):
#     exam_attempt = models.OneToOneField(ExamAttempt, on_delete=models.CASCADE)
#     student_answers = models.ManyToManyField(Question, through='StudentAnswer')

#     def __str__(self):
#         return f"{self.exam_attempt.exam.exam_name} - {self.exam_attempt.user.name}"

#     class Meta:
#         managed = True
#         db_table = 'exam_submission'


# class StudentAnswer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     exam_submission = models.ForeignKey(ExamSubmission, on_delete=models.CASCADE)
#     selected_option = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.question.question_name} - {self.exam_submission.exam_attempt.user.name}"

#     class Meta:
#         managed = True
#         db_table = 'student_answer'


# from django.db import models
# from django.utils import timezone
# from users.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    category_description = models.CharField(max_length=100, blank=True)
    category_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        managed = True
        db_table = 'category'
        verbose_name_plural = "Categories"


class Course(models.Model):
    course_name = models.CharField(max_length=100, unique=True)
    course_description = models.CharField(max_length=100, blank=True)
    course_image = models.ImageField(upload_to='course_images', blank=True, default='default_image.png')
    course_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    course_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name

    def save(self, *args, **kwargs):
        # Delete the old image file if it exists
        if self.id:
            old_instance = Course.objects.get(id=self.id)
            if self.course_image != old_instance.course_image:
                old_instance.course_image.delete(save=False)

        # Set the filename of the course_image to the course_name
        filename = f"{self.course_name}{os.path.splitext(self.course_image.name)[1]}"
        self.course_image.name = filename
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the course image file if it exists
        self.course_image.delete(save=False)

        super().delete(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'course'


class Exam(models.Model):
    exam_name = models.CharField(max_length=100, unique=True)
    exam_description = models.CharField(max_length=100, blank=True)
    exam_start_date = models.DateTimeField(blank=True)
    exam_duration = models.IntegerField(blank=True)
    exam_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    exam_course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.exam_name

    class Meta:
        managed = True
        db_table = 'exam'


class Question(models.Model):
    question_name = models.CharField(max_length=100, unique=True)
    question_text = models.CharField(max_length=200, blank=True)
    option1 = models.CharField(max_length=100, blank=True)
    option2 = models.CharField(max_length=100, blank=True)
    option3 = models.CharField(max_length=100, blank=True)
    option4 = models.CharField(max_length=100, blank=True)
    correct_answer = models.CharField(max_length=100, blank=True)
    question_status = models.BooleanField(default=True)
    question_exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_name

    class Meta:
        managed = True
        db_table = 'question'


class ExamAttempt(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    student_name = models.CharField(max_length=100)
    # attempt_date = models.DateTimeField(default=timezone.now)
    attempt_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attempt for {self.exam} by {self.student}"

    class Meta:
        managed = True
        db_table = 'exam_attempt'


class ExamSubmission(models.Model):
    attempt = models.ForeignKey(ExamAttempt, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=100)

    def __str__(self):
        return f"Submission for Attempt {self.attempt} - Question {self.question}"

    class Meta:
        managed = True
        db_table = 'exam_submission'


class StudentAnswer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return f"Answer for {self.question} by {self.student}"

    class Meta:
        managed = True
        db_table = 'student_answer'
