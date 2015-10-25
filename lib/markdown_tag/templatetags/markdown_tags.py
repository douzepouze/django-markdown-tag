from django import template
from django.utils.safestring import mark_safe
try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text

import markdown_tag
from markdown_tag.conf import settings

register = template.Library()


@register.filter(name="markdown")
def markdown_filter(value, options={}):
    """Processes the given value as Markdown, optionally using a particular
    Markdown style/config

    Syntax::

        {{ value|markdown }}            {# uses the "default" style #}
        {{ value|markdown:"mystyle" }}

    Markdown "styles" are defined by the `MARKDOWN_DEUX_STYLES` setting.
    """
    try:
        return mark_safe(markdown_tag.markdown(value, options))
    except ImportError:
        if settings.DEBUG:
            raise template.TemplateSyntaxError("Error in `markdown` filter: "
                "The python-markdown library isn't installed.")
        return force_text(value)
markdown_filter.is_safe = True
