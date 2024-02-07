from django.shortcuts import render
from .forms import ConfigForm

from django.http import HttpResponse
import yaml


from jinja2 import Environment, FileSystemLoader


HTML_TEMPLATE = "signature-template.html"


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
                "personal information": {
                    "name": form.cleaned_data.get("name"),
                    "title": form.cleaned_data.get("title"),
                    "organization_name": form.cleaned_data.get("organizationName"),
                    "organization_url": form.cleaned_data.get("organizationURL"),
                    "email": form.cleaned_data.get("email"),
                    "additional": form.cleaned_data.get("additional", "None") or "None",
                },
                "image": {
                    "is_image_selected": form.cleaned_data.get("isImageSelected", False)
                    or False,
                    "image_link": form.cleaned_data.get("imageLink", "None") or "None",
                    "image_type": form.cleaned_data.get("imageType", "photo") or "None",
                },
                "socials": {
                    "web_checkbox": form.cleaned_data.get("webCheckbox", False)
                    or False,
                    "web_link": form.cleaned_data.get("webLink", "None") or "None",
                    "github_checkbox": form.cleaned_data.get("githubCheckbox", False)
                    or False,
                    "github_link": form.cleaned_data.get("githubLink", "None")
                    or "None",
                    "instagram_checkbox": form.cleaned_data.get(
                        "instagramCheckbox", False
                    )
                    or False,
                    "instagram_link": form.cleaned_data.get("instagramLink", "None")
                    or "None",
                    "linkedin_checkbox": form.cleaned_data.get(
                        "linkedinCheckbox", False
                    )
                    or False,
                    "linkedin_link": form.cleaned_data.get("linkedinLink", "None")
                    or "None",
                    "slack_checkbox": form.cleaned_data.get("slackCheckbox", False)
                    or False,
                    "slack_link": form.cleaned_data.get("slackLink", "None") or "None",
                    "youtube_checkbox": form.cleaned_data.get("youtubeCheckbox", False)
                    or False,
                    "youtube_link": form.cleaned_data.get("youtubeLink", "None")
                    or "None",
                    "twitter_checkbox": form.cleaned_data.get("twitterCheckbox", False)
                    or False,
                    "twitter_link": form.cleaned_data.get("twitterLink", "None")
                    or "None",
                    "facebook_checkbox": form.cleaned_data.get(
                        "facebookCheckbox", False
                    )
                    or False,
                    "facebook_link": form.cleaned_data.get("facebookLink", "None")
                    or "None",
                },
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


def download_signature(request):
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=False,
    )
    template = env.get_template(HTML_TEMPLATE)
