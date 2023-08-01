from django.contrib.auth.models import Group
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import ProfileModel

userModel = get_user_model()


@receiver(post_save, sender=userModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(profile=instance)
        user_group = Group.objects.get(name='User')
        instance.groups.add(user_group)

