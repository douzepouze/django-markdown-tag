A small Django app that provides template tags for using
[Markdown](http://daringfireball.net/projects/markdown/) using the
python-markdown library.

# Django project setup

1. Add `markdown_tag` to `INSTALLED_APPS` in your project's "settings.py".

2. Options of python-markdown can be set in the markdown_tag/conf/settings.py `MARKDOWN_OPTIONS_DEFAULT` dict.

# Usage

## `markdown` template filter

    {% load markdown_tags %}
    {{ myvar|markdown }} 

# Credits
This project was forked from the [django-markdown-deux](https://github.com/trentm/django-markdown-deux) project.
