from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Order(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=30, help_text="Имя")
    bike = models.CharField(verbose_name="Мотик", max_length=30, help_text="Мотоцикл")
    phone = models.CharField(verbose_name="Телефон", max_length=30, help_text="Телефон")
    comment = models.TextField(
        verbose_name="Комментарий", help_text="Расскажите, что Вы ожидаете от прошивки"
    )
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-order_date",)
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "bike", "phone"],
                name="unique_order",
                violation_error_message="Вы уже оставили заказ!",
            ),
        ]


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Бренд")
    slug = models.SlugField(max_length=120, unique=True, verbose_name="Слаг")

    class Meta:
        ordering = ("name",)
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse("brand_detail", kwargs={"slug": self.slug})


class BikeModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="models", verbose_name="Бренд")
    name = models.CharField(max_length=150, verbose_name="Модель")
    slug = models.SlugField(max_length=180, unique=True, verbose_name="Слаг")
    years = models.CharField(max_length=60, blank=True, verbose_name="Годы выпуска")
    short_description = models.CharField(max_length=255, blank=True, verbose_name="Короткое описание")
    content = models.TextField(blank=True, verbose_name="Описание/ликбез по модели")
    # image = models.ImageField(upload_to="bikes/", blank=True, null=True, verbose_name="Изображение")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("brand__name", "name")
        unique_together = ("brand", "name")
        verbose_name = "Модель мотоцикла"
        verbose_name_plural = "Модели мотоциклов"

    def __str__(self) -> str:
        return f"{self.brand.name} {self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.brand.name}-{self.name}")
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse("bike_model_detail", kwargs={"slug": self.slug})


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=220, unique=True, verbose_name="Слаг")
    summary = models.CharField(max_length=300, blank=True, verbose_name="Короткое описание")
    content = models.TextField(verbose_name="Содержимое")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse("article_detail", kwargs={"slug": self.slug})


class Review(models.Model):
    author = models.CharField(max_length=120, verbose_name="Автор")
    text = models.TextField(verbose_name="Отзыв")
    bike_model = models.ForeignKey(
        BikeModel, on_delete=models.SET_NULL, null=True, blank=True, related_name="reviews", verbose_name="Модель"
    )
    source_url = models.URLField(blank=True, verbose_name="Ссылка на источник")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self) -> str:
        model = f" ({self.bike_model})" if self.bike_model else ""
        return f"{self.author}{model}"
