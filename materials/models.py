from django.db import models


class Course(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Название", help_text="Укажите название курса"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Опишите основные материалы курса",
    )
    preview = models.ImageField(
        upload_to="materials/courses",
        verbose_name="Превью",
        blank=True,
        null=True,
        help_text="Добавьте изображение",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Название", help_text="Укажите название урока"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Опишите содержание урока",
    )
    preview = models.ImageField(
        upload_to="materials/lessons",
        verbose_name="Превью",
        blank=True,
        null=True,
        help_text="Добавьте изображение",
    )
    url = models.URLField(
        verbose_name="Cсылка на видео",
        blank=True,
        null=True,
        help_text="Укажите ссылку на видео",
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        blank=True,
        null=True,
        help_text="Укажите курс",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
