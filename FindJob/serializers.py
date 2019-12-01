from rest_framework import serializers
from FindJob.models import *

# сериализатор для всех полей таблицы Category
class QuestionDetailSerializer(serializers.ModelSerializer):
    # добавляет скрытое поле пользователя, которого берет из request запроса
    # таким образом авторизованный пользователь привязывается к данному объекту
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Question
        fields = '__all__'

# сериализатор для определенных полей таблицы Category
class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('keywords', 'location', 'remote', 'skill')

class VacancyDetailSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Vacancy
        fields = '__all__'
class VacancyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'