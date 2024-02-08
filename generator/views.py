from django.shortcuts import render
from .forms import ConfigForm
from django.http import HttpResponse

from .tools import generate_html

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
                "personal_information": {
                    "name": form.cleaned_data.get("name"),
                    "title": form.cleaned_data.get("title"),
                    "organization_name": form.cleaned_data.get("organizationName"),
                    "organization_url": form.cleaned_data.get("organizationURL"),
                    "email": form.cleaned_data.get("email"),
                    "additional": form.cleaned_data.get("additional"),
                },
                "image": {
                    "is_image_selected": form.cleaned_data.get("isImageSelected", False)
                    or False,
                    "image_link": form.cleaned_data.get("imageLink", "None") or "None",
                    "image_type": form.cleaned_data.get("imageType", "photo") or "None",
                },
                "socials": {
                    "is_web_selected": form.cleaned_data.get("isWebSelected", False)
                    or False,
                    "web_link": form.cleaned_data.get("webLink", "None") or "None",
                    "is_github_selected": form.cleaned_data.get(
                        "isGithubSelected", False
                    )
                    or False,
                    "github_link": form.cleaned_data.get("githubLink", "None")
                    or "None",
                    "is_instagram_selected": form.cleaned_data.get(
                        "isInstagramSelected", False
                    )
                    or False,
                    "instagram_link": form.cleaned_data.get("instagramLink", "None")
                    or "None",
                    "is_linkedin_selected": form.cleaned_data.get(
                        "isLinkedinSelected", False
                    )
                    or False,
                    "linkedin_link": form.cleaned_data.get("linkedinLink", "None")
                    or "None",
                    "is_slack_selected": form.cleaned_data.get("isSlackSelected", False)
                    or False,
                    "slack_link": form.cleaned_data.get("slackLink", "None") or "None",
                    "is_youtube_selected": form.cleaned_data.get(
                        "isYoutubeSelected", False
                    )
                    or False,
                    "youtube_link": form.cleaned_data.get("youtubeLink", "None")
                    or "None",
                    "is_twitter_selected": form.cleaned_data.get(
                        "isTwitterSelected", False
                    )
                    or False,
                    "twitter_link": form.cleaned_data.get("twitterLink", "None")
                    or "None",
                    "is_facebook_selected": form.cleaned_data.get(
                        "isFacebookSelected", False
                    )
                    or False,
                    "facebook_link": form.cleaned_data.get("facebookLink", "None")
                    or "None",
                },
            }
    else:
        form = ConfigForm()

    return render(request, "custom.html", {"form": form})


def preview(request):
    html = generate_html(dict(data_conf))

    return HttpResponse(html)


def download_signature(request):
    html = generate_html(dict(data_conf))

    response = HttpResponse(html, content_type="text/html")
    response["Content-Disposition"] = "attachment; filename=signature.html"
    return response


def download_config(request):
    response = HttpResponse(
        yaml.dump(data_conf, sort_keys=False), content_type="text/plain"
    )
    response["Content-Disposition"] = "attachment; filename=config.yaml"
    return response
