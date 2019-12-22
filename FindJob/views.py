from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView, Response
from FindJob.serializers import *
from FindJob.models import *
from FindJob.permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# модули парсеры добывающие данные о вакансиях
from FindJob.helpers.hh import getVacancy_hh
from FindJob.helpers.superjob import getVacancy_sj

from threading import Thread

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
        # вытаскиваем из запроса параметры поиска вакансии
        query_params = {}
        query_params['keywords'] = request.GET.get('keywords', '')
        query_params['experience'] = request.GET.get('skill', '')
        query_params['employment'] = request.GET.get('employment', '')

        data = []
        hh = Thread(target=getVacancy_hh, args=(query_params, data))
        hh.start()
        sj = Thread(target=getVacancy_sj, args=(query_params, data))
        sj.start()
        hh.join()
        sj.join()
        return JsonResponse(data, safe=False)
