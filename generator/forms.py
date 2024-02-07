from django import forms


class ConfigForm(forms.Form):
    signatureName = forms.CharField(
        label="Enter signature name", max_length=100, required=True
    )

    name = forms.CharField(label="Enter your full name", max_length=100, required=True)

    title = forms.CharField(label="Enter your job title", max_length=100, required=True)

    organizationName = forms.CharField(
        label="Enter your organization name", max_length=100, required=True
    )

    organizationURL = forms.URLField(label="Enter your organization URL", required=True)

    email = forms.EmailField(label="Enter your email address", required=True)

    additional = forms.CharField(
        label="Enter organization address, phone number, quote, etc.",
        widget=forms.Textarea,
        required=False,
    )

    isImageSelected = forms.BooleanField(required=False)

    imageLink = forms.URLField(label="Enter image URL", required=False)

    IMAGE_TYPE_CHOICES = [
        ("photo", "Photo"),
        ("logo", "Logo"),
    ]
    imageType = forms.ChoiceField(
        choices=IMAGE_TYPE_CHOICES,
        widget=forms.RadioSelect,
        initial="photo",
        required=False,
    )
