from django import template
from django.template import Library

register = Library()

@register.simple_tag
def find(assignment,submitted):
    for s in submitted:
        if s.assignment == assignment:
            return s
    return None