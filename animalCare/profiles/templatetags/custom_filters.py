from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='is_member_of_group')
def is_member_of_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
        return group in user.groups.all()
    except Group.DoesNotExist:
        return False
