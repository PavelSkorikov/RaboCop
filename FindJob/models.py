import uuid
from django.db import models
# импортируем стандартную Django - модель пользователя
from django.contrib.auth import get_user_model

User = get_user_model()

# Модель таблицы с найденными вакансиями
class Vacancy(models.Model):
    # создаем уникальный идентификатор для поля с использованием uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # заголовок вакансии
    title = models.CharField(max_length=256)
    # описание вакансии
    # если balank=True - поле необязательно и может быть пустым (по умолчанию - False)
    description = models.CharField(max_length=512, blank=True)
    # ссылка на вакансию
    link = models.CharField(max_length=256, unique=True)
    # компания, предоставляющая вакансию
    company = models.CharField(max_length=128)
    # город размещения вакансии
    city = models.CharField(max_length=256)
    # дата размещения вакансии
    date = models.CharField(max_length=20)
    # дата создания записи в базе
    createAt = models.DateField(auto_now_add=True)
    # связанная модель пользователя, выполняющего поиск
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # для удобочитаемого отображения объекта в админке
    def __str__(self):
        return self.title
    # сортируем по дате создания записи
    class Meta:
        ordering = ['createAt']

# Модель поискового запроса
class Question(models.Model):
    # создаем уникальный идентификатор для поля с использованием uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # ключевые слова для запроса
    keywords = models.CharField(max_length=128)
    # требуется опыт или нет
    skill = models.BooleanField()
    # тип занятости
    EMPLOYMENT = (
        ('NO', 'Не знаю'),
        ('FULL', 'Полная занятость'),
        ('PARTIAL', 'Частичная занятость'),
        ('TEMPORARY', 'Временная работа'),
        ('INTERN', 'Стажировка'),
    )
    employment_type = models.CharField(max_length=9, choices=EMPLOYMENT, default='NO')
    createAt = models.DateField(auto_now_add=True)
    # связанная модель пользователя, выполняющего поиск
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    # для удобочитаемого отображения объекта в админке
    def __str__(self):
        return self.keywords
    # сортируем по дате создания записи
    class Meta:
        ordering = ['createAt']
