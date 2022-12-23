from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main_app import views


urlpatterns = [
    path("", views.index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
