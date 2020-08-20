from django import template

register = template.Library()

@register.filter(name='cut')

def cut(value,arg):
    """
    This cuts all value of "arg" from the String!
    """
    return value.replace(arg,'')

#register.filter('cut',cut)

"""
Here first cut is custom tag name and second is cut function, instead of this using decorator above
"""
