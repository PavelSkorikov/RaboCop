from django.contrib import admin
from FindJob.models import *

class QuestionAdmin(admin.ModelAdmin):
    """форма запроса"""
    list_display = ('id', 'keywords', 'skill', 'employment_type', 'schedule_work', 'createAt', 'user')

class VacancyAdmin(admin.ModelAdmin):
    """форма запроса"""
    list_display = ('id', 'title', 'description', 'link', 'company', 'city', 'date', 'createAt', 'user')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Vacancy, VacancyAdmin)
