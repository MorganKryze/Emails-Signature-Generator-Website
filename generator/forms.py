from django import forms
from django.utils.translation import gettext_lazy as _


class ConfigForm(forms.Form):
    config_file = forms.FileField(required=False)

    signatureName = forms.CharField(
        label=_("Enter signature name"), max_length=100, required=True
    )

    name = forms.CharField(
        label=_("Enter your full name"), max_length=100, required=True
    )

    title = forms.CharField(
        label=_("Enter your job title"), max_length=100, required=True
    )

    organizationName = forms.CharField(
        label=_("Enter your organization name"), max_length=100, required=True
    )

    organizationURL = forms.URLField(
        label=_("Enter your organization URL"), required=True
    )

    email = forms.EmailField(label=_("Enter your email address"), required=True)

    additional = forms.CharField(
        label=_("Enter organization address, phone number, quote, etc."),
        widget=forms.Textarea,
        required=True,
    )

    isImageSelected = forms.BooleanField(required=False)

    imageLink = forms.URLField(label=_("Enter image URL"), required=False)

    IMAGE_TYPE_CHOICES = [
        ("photo", _("Photo")),
        ("logo", _("Logo")),
    ]
    imageType = forms.ChoiceField(
        choices=IMAGE_TYPE_CHOICES,
        widget=forms.RadioSelect,
        initial="photo",
        required=False,
    )

    isWebSelected = forms.BooleanField(required=False)
    webLink = forms.URLField(label=_("Enter Website URL"), required=False)

    isGithubSelected = forms.BooleanField(required=False)
    githubLink = forms.URLField(label=_("Enter GitHub URL"), required=False)

    isInstagramSelected = forms.BooleanField(required=False)
    instagramLink = forms.URLField(label=_("Enter Instagram URL"), required=False)

    isLinkedinSelected = forms.BooleanField(required=False)
    linkedinLink = forms.URLField(label=_("Enter LinkedIn URL"), required=False)

    isSlackSelected = forms.BooleanField(required=False)
    slackLink = forms.URLField(label=_("Enter Slack URL"), required=False)

    isYoutubeSelected = forms.BooleanField(required=False)
    youtubeLink = forms.URLField(label=_("Enter YouTube URL"), required=False)

    isTwitterSelected = forms.BooleanField(required=False)
    twitterLink = forms.URLField(label=_("Enter Twitter URL"), required=False)

    isFacebookSelected = forms.BooleanField(required=False)
    facebookLink = forms.URLField(label=_("Enter Facebook URL"), required=False)
