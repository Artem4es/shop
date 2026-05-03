import time

from django.shortcuts import get_object_or_404, render

from main_page.forms import OrderForm
from main_page.models import Brand, BikeModel, Article, Review

from .telegram import admin_id, bot


def index(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get("name")
            bike = form.cleaned_data.get("bike")
            phone = form.cleaned_data.get("phone")
            comment = form.cleaned_data.get("comment")

            bot.send_message(chat_id=admin_id, text=f"Ура, новая заявка от {name}!")
            bot.send_message(chat_id=admin_id, text=f"Хочет прошить мотоцикл: {bike}")
            bot.send_message(chat_id=admin_id, text=phone)
            if comment:
                bot.send_message(chat_id=admin_id, text=comment)
            return render(request, "suc.html")
        return render(request, "error.html", {"form": form})

    form = OrderForm()
    context = {"form": form}
    return render(request, "index.html", context)


def yandex_webmaster(request):
    return render(request, "yandex_551046113a1adf80.html")


def google(request):
    time.sleep(5)
    print(time.time())
    return render(request, "google91b4364c93644c83.html")


def brands(request):
    items = Brand.objects.all().prefetch_related("models")
    return render(request, "brands.html", {"brands": items})


def bike_model_detail(request, slug: str):
    model = get_object_or_404(BikeModel.objects.select_related("brand"), slug=slug)
    reviews = model.reviews.all()[:12]
    return render(request, "model_detail.html", {"model": model, "reviews": reviews})


def articles(request):
    items = Article.objects.filter(is_published=True)
    return render(request, "articles.html", {"articles": items})


def article_detail(request, slug: str):
    item = get_object_or_404(Article, slug=slug, is_published=True)
    return render(request, "article_detail.html", {"article": item})


def reviews(request):
    items = Review.objects.select_related("bike_model", "bike_model__brand").all()
    return render(request, "reviews.html", {"reviews": items})