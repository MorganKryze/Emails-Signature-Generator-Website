import yaml
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import ConfigForm
from .tools import generate_html, get_latest_version, map_config_to_form

data_conf = {}


def index(request: HttpRequest) -> HttpResponse:
    """Index view.

    Args:
    ----
        request (HttpRequest): Request object.

    Returns:
    -------
        HttpResponse: Response object.

    """
    return render(request, "index.html", {"version": get_latest_version()})


def terms(request: HttpRequest) -> HttpResponse:
    """Terms view.

    Args:
    ----
        request (HttpRequest): Request object.

    Returns:
    -------
        HttpResponse: Response object.

    """
    return render(request, "terms.html", {"version": get_latest_version()})


def guidelines(request: HttpRequest) -> HttpResponse:
    """Guidelines view.

    Args:
    ----
        request (HttpRequest): Request object.

    Returns:
    -------
        HttpResponse: Response object.

    """
    return render(request, "guidelines.html", {"version": get_latest_version()})


def clients(request: HttpRequest) -> HttpResponse:
    """Clients view.

    Args:
    ----
        request (HttpRequest): Request object.

    Returns:
    -------
        HttpResponse: Response object.

    """
    return render(request, "clients.html", {"version": get_latest_version()})


def custom(request: HttpRequest) -> HttpResponse:
    """Customizatio view.

    Args:
    ----
        request (HttpRequest): Request object.

    Returns:
    -------
        HttpResponse: Response object.

    """
    if request.method == "POST":
        form = ConfigForm(request.POST, request.FILES)
        config_file = request.FILES.get("config_file")
        if config_file:
            config_data = yaml.safe_load(config_file)
            mapped_data = map_config_to_form(config_data)
            form = ConfigForm(initial=mapped_data)
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
                        "isGithubSelected",
                        False,
                    )
                    or False,
                    "github_link": form.cleaned_data.get("githubLink", "None")
                    or "None",
                    "is_instagram_selected": form.cleaned_data.get(
                        "isInstagramSelected",
                        False,
                    )
                    or False,
                    "instagram_link": form.cleaned_data.get("instagramLink", "None")
                    or "None",
                    "is_linkedin_selected": form.cleaned_data.get(
                        "isLinkedinSelected",
                        False,
                    )
                    or False,
                    "linkedin_link": form.cleaned_data.get("linkedinLink", "None")
                    or "None",
                    "is_slack_selected": form.cleaned_data.get("isSlackSelected", False)
                    or False,
                    "slack_link": form.cleaned_data.get("slackLink", "None") or "None",
                    "is_youtube_selected": form.cleaned_data.get(
                        "isYoutubeSelected",
                        False,
                    )
                    or False,
                    "youtube_link": form.cleaned_data.get("youtubeLink", "None")
                    or "None",
                    "is_twitter_selected": form.cleaned_data.get(
                        "isTwitterSelected",
                        False,
                    )
                    or False,
                    "twitter_link": form.cleaned_data.get("twitterLink", "None")
                    or "None",
                    "is_facebook_selected": form.cleaned_data.get(
                        "isFacebookSelected",
                        False,
                    )
                    or False,
                    "facebook_link": form.cleaned_data.get("facebookLink", "None")
                    or "None",
                },
            }

    else:
        form = ConfigForm()

    return render(
        request,
        "custom.html",
        {"form": form, "version": get_latest_version()},
    )


def preview(request: HttpRequest) -> HttpResponse:  # noqa: ARG001
    """Preview view.

    Args:
    ----
        request (HttpRequest): Request object.

    Returns:
    -------
        HttpResponse: Response object.

    """
    html = generate_html(dict(data_conf))

    return HttpResponse(html)


def download_signature(request: HttpRequest) -> HttpResponse:  # noqa: ARG001
    """Download signature view.

    Returns
    -------
        HttpResponse: Response object.

    """
    html = generate_html(dict(data_conf))

    signature_name = data_conf.get("signature_name", "")
    filename = f"signature-{signature_name}.html"

    response = HttpResponse(html, content_type="text/html")
    response["Content-Disposition"] = f"attachment; filename={filename}"
    return response


def download_config(request: HttpRequest) -> HttpResponse:  # noqa: ARG001
    """Download config view.

    Returns
    -------
        HttpResponse: Response object.

    """
    signature_name = data_conf.get("signature_name", "")
    filename = f"{signature_name}.yaml"

    response = HttpResponse(
        yaml.dump(data_conf, sort_keys=False),
        content_type="text/plain",
    )
    response["Content-Disposition"] = f"attachment; filename=config-{filename}"
    return response
