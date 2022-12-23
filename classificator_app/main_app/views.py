from django.shortcuts import render
from .forms import filterForm
from .models import (
    Article,
)
from django.db.utils import OperationalError

# Create your views here.


def index(request):
    selected_label = request.GET.get("selected_label", None)
    direction_sort = request.GET.get("sorting", 0)
    sort_by = "date" if int(direction_sort) else "-date"
    try:
        if selected_label in {"Develop", "Other"}:
            category = "Разработка" if selected_label == "Develop" else "Другое"
            articles = Article.objects.filter(label=selected_label)
        else:
            articles = Article.objects.all()
            category = "Все"
        return render(
            request,
            "index.html",
            {
                "articles": articles.order_by(sort_by),
                "count": articles.count(),
                "filter_form": filterForm,
                "category": category,
            },
        )
    except OperationalError:
        return render(
            request,
            "errors.html",
            {"text": "Отсутствует соединение с базой данных","code":503},
            status=503
        )
