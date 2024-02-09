# Emails-Signature-Generator-Website

> A website to create and customize your email signature in seconds.

[![Demo-page](assets/img/jpg/demo.jpeg)](https://emails-signature-generator.vercel.app)

## Getting Started

The project does not need to be installed to be used as it is available [here](https://emails-signature-generator.vercel.app).

### Prerequisites

- Python 3.9 (not higher because of Django 4.2.9)

### Build

To build the project, you can either download the zip file or clone the repository:

```bash
git clone https://github.com/MorganKryze/Emails-Signature-Generator-Website.git
```

In addition, you will need to install the following libraries in your python environment:

```bash
cd Emails-Signature-Generator-Website
pip install -r requirements.txt
```

> [!NOTE]
> I recomment using a virtual environment ([venv](https://docs.python.org/3/library/venv.html) or [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)) to avoid conflicts with your other projects.

You also need gettext to compile the translations. The details instructions are available [here](https://www.drupal.org/docs/8/modules/potion/how-to-install-setup-gettext).

### Usage

Now you may use the executable files from the dev_wrokflow folder to run the project:

This command will start the server on your local machine:

```bash
sh dev_workflow/run.sh
```

This command will create the ids for the messages of the app:

```bash
sh dev_workflow/create_trans_ids.sh
```

This command will compile the messages of the app:

```bash
sh dev_workflow/load_trans.sh
```

### Project structure

To understand the project structure, you can refer to the [STRUCTURE.md](STRUCTURE.md) file.

### Supported social media

- Website
- Github
- Instagram
- Linkedin
- Slack
- Facebook
- Youtube
- Twitter

### Supported email clients

- [Apple Mail](https://www.hubspot.com/email-signature-generator/add-html-signature-mail-mac)
- [Thunderbird](https://www.youtube.com/watch?v=oPP4_i_kfQE)
- [Outlook (Windows)](https://www.youtube.com/watch?v=gL5WfVg55c4)
- [Outlook (Mac)](https://superuser.com/questions/1325233/use-html-signature-in-outlook-2016-for-mac)
- [Gmail](https://www.youtube.com/watch?v=DpW2XJkYYDQ)

### Supported languages

- English
- French
- Spanish
- German

## Future improvements

- Custom the font
- Custom the color
- Custom the html template
- Add more social media
- Add more email clients
- Add more languages
- Add informative popups or banners for issues or warnings

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
