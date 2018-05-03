from django import template
from django.template.loader import get_template

register = template.Library()

@register.filter(name='is_deploma')
def is_deploma(value):
    return value['year'] == '2' and value['course'] == 'BTech'

@register.filter(name='is_first_year')
def is_first_year(value):
    return value['year'] == '1' and value['course'] == 'BTech'

@register.filter(name='is_mca')
def is_mca(value):
    return value['course'] == 'MCA'
