from django import template
from sorl.thumbnail.templatetags.thumbnail import thumbnail

register = template.Library()


def sorl_thumbnail(parser, token):
    return thumbnail(parser, token)

register.tag(sorl_thumbnail)
