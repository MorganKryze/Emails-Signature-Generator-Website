from jinja2 import Environment, FileSystemLoader

HTML_TEMPLATE = "signature-template.html"


def generate_html(data: dict):
    env = Environment(
        loader=FileSystemLoader("generator/templates"),
        autoescape=False,
    )

    template = env.get_template(HTML_TEMPLATE)
    data_conf_dict = dict(data)

    return template.render(data_conf_dict)
