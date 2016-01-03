from django import template

register = template.Library()


@register.filter
def shuffle_participants(participants):
    return participants.order_by('?')
