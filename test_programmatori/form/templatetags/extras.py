from django import template
from datetime import date

register = template.Library()

@register.simple_tag()
def getAge(birth):
    today = date.today()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    return age

@register.simple_tag()
def multiply(a, b):
    return a*b

@register.simple_tag()
def divide(a, b):
    return a/b

@register.simple_tag()
def subtract(a, b):
    return a-b

@register.simple_tag()
def addition(a, b):
    return a+b