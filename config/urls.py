from django.conf.urls import i18n
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path

urlpatterns = i18n_patterns(
    path("i18n/", include(i18n)),
    path("", include("generator.urls")),
)
