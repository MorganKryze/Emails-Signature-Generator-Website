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
