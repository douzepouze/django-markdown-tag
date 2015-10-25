from django.conf import settings

MARKDOWN_OPTIONS_DEFAULT = {
    "extensions": [
        'markdown.extensions.extra',
    ],
}

DEBUG = settings.DEBUG
