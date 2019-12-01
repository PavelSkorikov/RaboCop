from django.shortcuts import render
from rest_framework import generics
from FindJob.serializers import *
from FindJob.models import *
from FindJob.permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
# метод который создает объект в базе данных
class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionDetailSerializer
    # правило доступа, импортируется из rest_framework.permissions, определяет что
    # что тоько аутентифицированнный пользователь и администратор имеет доступ
    permission_classes = (IsAuthenticated, )
