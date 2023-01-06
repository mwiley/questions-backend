from django.db import models

# Create your models here.

class Question(models.Model):
    title_text = models.CharField(max_length=300)
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')