from django import template

register = template.Library()


def cut(value,arg):
    """
        This cut out all the value of arg and replace it
    """
    return value.replace(arg, "")


register.filter('cut', cut)




















