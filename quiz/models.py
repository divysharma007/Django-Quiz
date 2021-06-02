from django.db import models
from django.db.models.query import QuerySet
from user.models import User

class Answer(models.Model):
    answer=models.CharField(max_length=100)
    def __str__(self):
        return self.answer[0:50]

class Question(models.Model):
    question=models.TextField()
    answer=models.ManyToManyField(Answer)

    def __str__(self):
        return self.question[0:50]

class Quiz(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    questions=models.ManyToManyField(Question)
    enrollment_key=models.CharField(max_length=16,default="none")

    
# Create your models here.
