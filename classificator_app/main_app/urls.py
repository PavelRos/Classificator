from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from classificator import views as classificator_views
from main_app import views


urlpatterns = [
    path("", views.index),
    path("add_file", views.saveFileInDB),
    path("train", classificator_views.train),
    path("classificate", classificator_views.classificate),
    re_path(r"^text/(?P<id>.+)", views.getTextFromArticle),
    re_path(r"^remove/(?P<id>.+)", views.removeArticle),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = 'main_app.views.handler404'
