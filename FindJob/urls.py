from django.urls import path, include
from FindJob.views import *

app_name = 'FindJob'
urlpatterns = [
    # блок Категория товара
    path('question/create/', QuestionCreateView.as_view()),

]