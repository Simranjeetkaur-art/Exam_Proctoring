import os
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    category_description = models.CharField(max_length=100,blank=True)
    category_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        managed = True
        db_table = 'category'
        verbose_name_plural = "Categories"

    
class Course(models.Model):
    course_name = models.CharField(max_length=100, unique=True)
    course_description = models.CharField(max_length=100,blank=True)
    course_image = models.ImageField(upload_to='course_images', blank=True, default='default_image.png')
    course_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True)
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
    exam_description = models.CharField(max_length=100,blank=True)
    exam_start_date = models.DateTimeField(blank=True)
    exam_duration = models.IntegerField(blank=True)
    exam_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True)
    exam_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.exam_name
    
    class Meta:
        managed = True
        db_table = 'exam'

class Question(models.Model):
    question_name = models.CharField(max_length=100, unique=True)
    question_text = models.CharField(max_length=200,blank=True)
    option1 = models.CharField(max_length=100,blank=True)
    option2 = models.CharField(max_length=100,blank=True)
    option3 = models.CharField(max_length=100,blank=True)
    option4 = models.CharField(max_length=100,blank=True)
    correct_answer = models.CharField(max_length=100,blank=True)
    question_status = models.BooleanField(default=True)
    question_exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question_name
    
    class Meta:
        managed = True
        db_table = 'question'