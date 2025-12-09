from django.db import models
from django.urls import reverse

class Concept(models.Model):
    name = models.CharField("Название концепции", max_length=50)  # Юриспруденция, Экономисты
    icon = models.CharField("Иконка", max_length=10)              # ⚖️, 💻 и т.д.
    color = models.CharField("Цвет (HEX или название)", max_length=20)  # #8a2be2 или "фиолетовый"
    description = models.CharField("Описание концепции", max_length=100)  # право и справедливость

    class Meta:
        verbose_name = "Концепция"
        verbose_name_plural = "Концепции"

    def __str__(self):
        return self.name

class Course(models.Model):
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, verbose_name="Концепция")
    title = models.CharField("Название предмета", max_length=100)       # Юриспруденция
    subtitle = models.CharField("Краткое описание", max_length=150)     # Основы права
    description = models.TextField("Описание курса")                    # Подробное описание
    button_text = models.CharField("Текст кнопки", max_length=100, default="Перейти к курсу")
    is_active = models.BooleanField("Доступность", default=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("course-detail", args=[str(self.id)])