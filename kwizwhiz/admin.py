from django.contrib import admin
from .models import *

class KidUserAdmin(admin.ModelAdmin):
    pass
admin.site.register(KidUser, KidUserAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category, CategoryAdmin)

class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['answer_text', 'is_right']

admin.site.register(Quiz, QuizAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'quiz']
    inlines = [AnswerInlineModel]
admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'is_right', 'question']
admin.site.register(Answer, AnswerAdmin)

# Register your models here.
