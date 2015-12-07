__author__ = 'mehmet'

from django import template

register = template.Library()


@register.filter
def ada(d, key):
    return d[key]
