from django.contrib import admin
from .models import Category, Quiz, Question, Choice, Result

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4
    max_num = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('text', 'quiz')
    list_filter = ('quiz',)

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'quiz_type', 'created_at')
    list_filter = ('category', 'quiz_type')

class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'total_questions', 'taken_at')
    list_filter = ('quiz', 'user')

admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Result, ResultAdmin)
