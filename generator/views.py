from django.shortcuts import render
from .forms import ConfigForm

from django.http import HttpResponse
import yaml


data_conf = {}


def index(request):
    return render(request, "index.html")


def custom(request):
    if request.method == "POST":
        form = ConfigForm(request.POST)
        if form.is_valid():
            global data_conf
            data_conf = {
                "signature_name": form.cleaned_data.get("signatureName"),
                "name": form.cleaned_data.get("name"),
                "title": form.cleaned_data.get("title"),
                "organization_name": form.cleaned_data.get("organizationName"),
                "organization_url": form.cleaned_data.get("organizationURL"),
                "email": form.cleaned_data.get("email"),
                "additional": form.cleaned_data.get("additional", "None") or "None",
                "is_image_selected": form.cleaned_data.get("isImageSelected", False) or False,
                "image_link": form.cleaned_data.get("imageLink", "None") or "None",
                "image_type": form.cleaned_data.get("imageType", "photo") or "None",
                "web_checkbox": form.cleaned_data.get("webCheckbox", False) or False,
                "web_link": form.cleaned_data.get("webLink", "None") or "None",
                
            }
    else:
        form = ConfigForm()

    return render(request, "custom.html", {"form": form})


def download_config(request):
    response = HttpResponse(
        yaml.dump(data_conf, sort_keys=False), content_type="text/plain"
    )
    response["Content-Disposition"] = "attachment; filename=data.yaml"
    return response
