from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_staff_group(sender, **kwargs):
    Group.objects.get_or_create(name='Staff')
    Group.objects.get_or_create(name='Vet')
    Group.objects.get_or_create(name='User')
