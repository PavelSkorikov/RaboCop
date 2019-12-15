from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView, Response
from FindJob.serializers import *
from FindJob.models import *
from FindJob.permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from FindJob.helpers.hh import *

# Create your views here.
# метод который создает объект в базе данных
class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionDetailSerializer
    permission_classes = (AllowAny, )
# метод который возвращает список объектов из таблицы
# он должен обязательно иметь параметр queryset в котором можно задавать условия выборки объектов
class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionListSerializer
    permission_classes = (IsAuthenticated, )
    # выбираем запросы которые сделал текущий пользователь и сортируем по убыванию даты создания заказа
    def get_queryset(self):
        return Question.objects.filter(user=self.request.user).order_by('-createAt')
# метод, который возвращает детальную информацию по одному запросу
class QuestionDetailView(generics.RetrieveAPIView):
    serializer_class = QuestionDetailSerializer
    queryset = Question.objects.all()
    permission_classes = (IsOwner, )
# метод редактирования или удаления запроса
class QuestionEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailSerializer
    queryset = Question.objects.all()
    permission_classes = (IsOwner, )

@csrf_exempt
def vacancy_return(request):
    if request.method == 'GET':
        data = get_vacancy('https://hh.ru/search/vacancy?st=searchVacancy&text=Node.js&experience=doesNotMatter&employment=full&schedule=remote&items_on_page=100')
        return JsonResponse(data, safe=False)
