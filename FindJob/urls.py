from django.urls import path, include
from FindJob.views import *

app_name = 'FindJob'
urlpatterns = [
    # блок Запроса
    path('question/create/', QuestionCreateView.as_view()),
    path('question/all/', QuestionListView.as_view()),
    # <uuid:pk> это номер id записи которую Django rest достанет из БД
    path('question/detail/<uuid:pk>', QuestionDetailView.as_view()),
    path('question/edit/<uuid:pk>', QuestionEditView.as_view()),
    path('vacancy/list/', vacancy_return.as_view()),
]
