#!/usr/bin/env python
# Copyright (c) 2008-2010 ActiveState Corp.
# Copyright (c) 2015 Steffen Görtz
# License: MIT (http://www.opensource.org/licenses/mit-license.php)

r"""A small Django app that provides template tags for Markdown using the
python-markdown library.

See <http://github.com/douzepouze/django-markdown-tag> for more info.
"""

__version_info__ = (1, 0, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "Steffen Görtz"


def markdown(text, style="default"):
    if not text:
        return ""
    import markdown
    return markdown.markdown()

def get_style(style):
    from markdown_tag.conf import settings
    try:
        return settings.MARKDOWN_DEUX_STYLES[style]
    except KeyError:
        return settings.MARKDOWN_DEUX_STYLES.get("default",
            settings.MARKDOWN_DEUX_DEFAULT_STYLE)
