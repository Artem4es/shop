from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from main_page import views

app_name = "shop"

urlpatterns = [
    path("", views.index, name="index"),
    path("yandex_551046113a1adf80.html", views.yandex_webmaster),
    path("google91b4364c93644c83.html", views.google),
    path("favicon.ico", RedirectView.as_view(url="/static/assets/turbo.png")),
    path("brands/", views.brands, name="brands"),
    path("models/<slug:slug>/", views.bike_model_detail, name="bike_model_detail"),
    path("articles/", views.articles, name="articles"),
    path("articles/<slug:slug>/", views.article_detail, name="article_detail"),
    path("reviews/", views.reviews, name="reviews"),
    path("admin/", admin.site.urls),
]
