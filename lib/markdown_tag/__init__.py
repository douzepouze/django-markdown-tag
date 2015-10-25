#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2008-2010 ActiveState Corp.
# Copyright (c) 2015 Steffen Görtz
# License: MIT (http://www.opensource.org/licenses/mit-license.php)

r"""A small Django app that provides template tags for Markdown using the
python-markdown library.

See <http://github.com/douzepouze/django-markdown-tag> for more info.
"""
from markdown_tag.conf import settings

__version_info__ = (1, 0, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "Steffen Görtz"


def markdown(text, options={}):
    import markdown
    if not text:
        return ""
    local_options = settings.MARKDOWN_OPTIONS_DEFAULT
    local_options.update(options)
    return markdown.markdown(text, **local_options)
