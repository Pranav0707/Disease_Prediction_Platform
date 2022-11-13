from django.db import models

# Create your models here.


class Feedback(models.Model):
    name=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=25)
    email=models.EmailField()
    message=models.TextField()
    created_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name