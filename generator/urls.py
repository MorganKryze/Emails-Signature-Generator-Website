from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("custom/", views.custom, name="custom"),
    path("download-config/", views.download_config, name="download-config"),
    path("preview/", views.download_signature, name="preview"),
]
