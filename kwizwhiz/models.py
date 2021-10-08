from django.db import models
import bcrypt
import re

class KidUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = KidUserManager()

class Updated(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Quiz(models.Model):

    class Meta:
        verbose_name_plural = "Quizzes"
        ordering = ['id']

    category = models.ForeignKey(Category, related_name='quizzes', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100, default='New Quiz')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

# Create your models here.
