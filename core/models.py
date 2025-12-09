from django.db import models
from django.urls import reverse

class Concept(models.Model):
    name = models.CharField(
        "Название профессии",
        max_length=50,
        help_text='Пример: "Юриспруденция", "Экономисты", "Программисты"'
    )
    icon = models.CharField(
        "Иконка",
        max_length=10,
        help_text='Пример: "⚖️", "💻", "📈"'
    )
    color = models.CharField(
        "Цвет (название)",
        max_length=20,
        default="фиолетовый",
        help_text='Пример: "фиолетовый", "зелёный", "синий"'
    )
    description = models.CharField(
        "Описание концепции",
        max_length=100,
        help_text='Пример: "право и справедливость", "технологии и цифра"'
    )

    class Meta:
        verbose_name = "Концепция"
        verbose_name_plural = "Концепции"

    def __str__(self):
        return self.name


class Course(models.Model):
    concept = models.ForeignKey(
        Concept,
        on_delete=models.CASCADE,
        verbose_name="Концепция",
        help_text='Выберите концепцию, к которой относится курс'
    )
    title = models.CharField(
        "Название предмета",
        max_length=100,
        help_text='Пример: "Юриспруденция", "Экономика""'
    )
    subtitle = models.CharField(
        "Краткое описание",
        max_length=150,
        help_text='Пример: "Основы права", "Введение в экономику"'
    )
    description = models.TextField(
        "Описание курса",
        help_text='Пример: "Законы, права человека, ответственность. Вопросы по Конституции и базовым кодексам."'
    )
    button_text = models.CharField(
        "Текст кнопки",
        max_length=100,
        default="Перейти к курсу",
        help_text='Текст кнопки для перехода к курсу'
    )
    is_active = models.BooleanField(
        "Доступность",
        default=True,
        help_text='Если курс неактивен, кнопка будет недоступна'
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title
