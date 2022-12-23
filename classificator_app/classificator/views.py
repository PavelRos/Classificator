from django.shortcuts import render
from main_app.models import Article
from django.http import HttpResponseRedirect
from .models import Svc_model
from django.db.utils import OperationalError

# Create your views here.


def train(request):
    global svc_model
    try:
        svc_model = Svc_model.createModelFromData(Article.objects.all())
    except OperationalError:
        render(
            request,
            "errors.html",
            {"text": "Отсутствует соединение с базой данных","code":503},
            status=503
        )
    return HttpResponseRedirect("/")
