from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classificator import views as classificator_views
from main_app import views


urlpatterns = [
    path("", views.index),
    path("add_file", views.saveFileInDB),
    path("train", classificator_views.train),
    path("classificate", classificator_views.classificate),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
