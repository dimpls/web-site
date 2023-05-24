from django import template

register = template.Library()


@register.filter
def get_value(dictionary, key):
    return dictionary.get(key, '')

@register.filter
def stars_range(value):
    return range(1, value + 1)
