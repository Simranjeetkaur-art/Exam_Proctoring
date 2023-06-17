from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


# user1 = User(username='Student1')
# user1.save()

# user2 = User(username='Student2')
# user2.save()

# user3 = User(username='Student3')
# user3.save()