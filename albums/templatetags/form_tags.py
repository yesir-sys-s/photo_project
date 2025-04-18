from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='addclass')
def addclass(field, css_class):
    if hasattr(field, 'as_widget'):
        return field.as_widget(attrs={'class': css_class})
    return field

@register.filter(name='attr')
def attr(field, args):
    if not hasattr(field, 'as_widget'):
        return field
        
    attrs = {}
    if ':' in args:
        attr, value = args.split(':')
        attrs[attr] = value
    return field.as_widget(attrs=attrs)
