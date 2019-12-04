from django.shortcuts import render
from rest_framework import generics
from FindJob.serializers import *
from FindJob.models import *
from FindJob.permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

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