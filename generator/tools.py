from jinja2 import Environment, FileSystemLoader

HTML_TEMPLATE = "signature-template.html"


def generate_html(data: dict):
    env = Environment(
        loader=FileSystemLoader("generator/templates"),
        autoescape=False,
    )

    template = env.get_template(HTML_TEMPLATE)
    data_conf_dict = dict(data)

    social_media_html = ""
    socials = data_conf_dict["socials"]

    social_media_mapping = {
        "web": "website",
        "github": "github",
        "instagram": "instagram",
        "linkedin": "linkedin",
        "slack": "slack",
        "youtube": "youtube",
        "twitter": "twitter",
        "facebook": "facebook",
    }
    skip_next_link = False

    for key, value in socials.items():
        if skip_next_link:
            if key.endswith("_link"):
                value = "None"
            skip_next_link = False
        if key.endswith("_selected") and not value:
            skip_next_link = True
            continue
        if key.endswith("_link"):
            social_media = social_media_mapping[key.split("_")[0]]
            if value != "None":
                social_media_html += (
                    f'\n\t\t\t\t<a href="{value}"><img'
                    ' src="https://raw.githubusercontent.com/MorganKryze/Emails-Signature-Generator-Website/main/assets/img/icons/'
                    f'{social_media}.svg" alt="{social_media}_icon"></a>'
                )

    data_conf_dict["social_media_html"] = social_media_html

    return template.render(data_conf_dict)


def map_config_to_form(config_data):
    mapped_data = {}
    # Map signature_name
    mapped_data["signatureName"] = config_data.get("signature_name")

    # Map personal_information
    personal_info = config_data.get("personal_information", {})
    mapped_data.update(
        {
            "name": personal_info.get("name"),
            "title": personal_info.get("title"),
            "organizationName": personal_info.get("organization_name"),
            "organizationURL": personal_info.get("organization_url"),
            "email": personal_info.get("email"),
            "additional": personal_info.get("additional"),
        }
    )

    # Map image
    image_data = config_data.get("image", {})
    mapped_data.update(
        {
            "isImageSelected": image_data.get("is_image_selected", False),
            "imageLink": image_data.get("image_link", "") if image_data.get("image_link") != "None" else "",
            "imageType": image_data.get("image_type", "photo"),
        }
    )

    # Map socials
    socials_data = config_data.get("socials", {})
    mapped_data.update(
        {
            "isWebSelected": socials_data.get("is_web_selected", False),
            "webLink": socials_data.get("web_link", "")
            if socials_data.get("web_link") != "None"
            else "",
            "isGithubSelected": socials_data.get("is_github_selected", False),
            "githubLink": socials_data.get("github_link", "")
            if socials_data.get("github_link") != "None"
            else "",
            "isInstagramSelected": socials_data.get("is_instagram_selected", False),
            "instagramLink": socials_data.get("instagram_link", "")
            if socials_data.get("instagram_link") != "None"
            else "",
            "isLinkedinSelected": socials_data.get("is_linkedin_selected", False),
            "linkedinLink": socials_data.get("linkedin_link", "")
            if socials_data.get("linkedin_link") != "None"
            else "",
            "isSlackSelected": socials_data.get("is_slack_selected", False),
            "slackLink": socials_data.get("slack_link", "")
            if socials_data.get("slack_link") != "None"
            else "",
            "isYoutubeSelected": socials_data.get("is_youtube_selected", False),
            "youtubeLink": socials_data.get("youtube_link", "")
            if socials_data.get("youtube_link") != "None"
            else "",
            "isTwitterSelected": socials_data.get("is_twitter_selected", False),
            "twitterLink": socials_data.get("twitter_link", "")
            if socials_data.get("twitter_link") != "None"
            else "",
            "isFacebookSelected": socials_data.get("is_facebook_selected", False),
            "facebookLink": socials_data.get("facebook_link", "")
            if socials_data.get("facebook_link") != "None"
            else "",
        }
    )

    return mapped_data
