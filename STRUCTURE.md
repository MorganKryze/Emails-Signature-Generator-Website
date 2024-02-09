# Project structure

## Introduction

Here are the most important files and directories of the project( you may ignore the other files and directories):

```plaintext
Emails-Signature-Generator-Website
├── dev_workflow
│   ├── create_trans_id.sh
│   ├── load_trans.sh
│   └── run.sh
├── generator
│   ├── locale
│   │   ├── de
│   │   ├── en
│   │   ├── es
│   │   └── fr
│   ├── templates
│   │   ├── base.html
│   │   ├── signature-template.html
│   │   └── 404.html
│   ├── forms.py
│   ├── tools.py
│   ├── urls.py
│   └── views.py
├── config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── assets
│   └── img
│       └── ...
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── manage.py
├── build_files.sh
└── vercel.json
```

## Small descriptives

### dev workflow

The `dev_workflow` directory contains the scripts to run the project, update the translations. To add a new language, you will need to add it in the settings.py and update the shells (include new lines with the language code).

### generator

The `generator` directory contains the main files of the project.

- The `locale` directory contains the translations of the app (english, spanish, french and german) inside .po files.
- The `templates` directory contains the html files for the navigation and the template for the signature (if you do not know what bas.html is I recommend you to read this [exchange](https://stackoverflow.com/questions/14720464/django-project-base-template)).
- The `forms.py` file contains the form to create a signature.
- The `tools.py` file contains the functions to generate the html from the data collected from the form.
- The `urls.py` file contains the links between the patterns and views.
- The `views.py` file contains the views associated with the html files.
  
### config

The `config` directory contains the settings of the project. For a Django project, this directory is created using the command `django-admin startproject config`. This folder can manage different apps like the `generator` app.

- The `settings.py` file contains the overall settings of the project (installed apps, middleware, databases, etc) and the settings for the internationalization.
- The `urls.py` file contains the main urls of the project (the urls of the apps are included here associated with the i18n).
- The `wsgi.py` file contains the settings for the WSGI (Web Server Gateway Interface) which is a specification that describes how a web server communicates with web applications (Note: add the following line to the file `app = application` for the vercel deployment).

### assets

The `assets` directory contains the images of the project, would it be svg or jpg files.

### build_files.sh and vercel.json

The `build_files.sh` file is a shell script to build the files of the project for the deployment. The `vercel.json` file is the configuration file for the vercel deployment that indicates the build command and the output directory.

### manage.py

The `manage.py` file is a command-line utility that lets you interact with this Django project in various ways. You can read more about it [here](https://docs.djangoproject.com/en/3.2/ref/django-admin/).
