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
                "signature_name": form.cleaned_data.get("signatureName") or "None",
                "name": form.cleaned_data.get("name") or "None",
                "title": form.cleaned_data.get("title") or "None",
                "organization_name": form.cleaned_data.get("organizationName") or "None",
                
                # "image_option": form.cleaned_data.get("imageOption", False),
                # "image_type": form.cleaned_data.get("imageType", "photo"),
            }
            print(data_conf)
    else:
        form = ConfigForm()

    return render(request, "custom.html", {"form": form})


def download_config(request):
    response = HttpResponse(yaml.dump(data_conf, sort_keys=False), content_type="text/plain")
    response["Content-Disposition"] = "attachment; filename=data.yaml"
    return response
