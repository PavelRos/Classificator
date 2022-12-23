from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main_app import views


urlpatterns = [
    path("", views.index),
    path("add_file", views.saveFileInDB)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
