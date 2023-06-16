from django.db import models

class Profiles(models.Model):
    ROLE_CHOICES = [
        ('S', 'Student'),
        ('T', 'Teacher'),
    ]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)

    def __str__(self):
        return self.profiles

    class Meta:
        managed = True
        db_table = 'profiles'
       
