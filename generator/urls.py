from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("guidelines/", views.guidelines, name="guidelines"),
    path("terms/", views.terms, name="terms"),
    path("custom/", views.custom, name="custom"),
    path("preview/", views.preview, name="preview"),
    path("download-signature/", views.download_signature, name="download-signature"),
    path("download-config/", views.download_config, name="download-config"),
]
