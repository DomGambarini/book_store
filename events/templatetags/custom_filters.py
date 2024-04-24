from django import template
register = template.Library()


@register.filter
def format_duration(duration):
    total_seconds = duration.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    return '{:02d}hour:{:02d}mins'.format(hours, minutes)
