from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image


class Profile(models.Model):
    image = models.ImageField(default='profile_pic/default.png',
                              upload_to='profile_pic/', blank=True, null=True, )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, )

    mobile_number = models.CharField(max_length=100, blank=True, null=True, )
    address = models.CharField(max_length=100, blank=True, null=True, )
    post_code = models.CharField(max_length=100, blank=True, null=True, )
    country = models.CharField(max_length=100, blank=True, null=True, )
    state = models.CharField(max_length=100, blank=True, null=True, )
    consulting_fee = models.CharField(max_length=50,  blank=True, null=True)
    consultant = 'consultant'
    client = 'client'
    account_select = [
        (consultant, 'consultant'),
        (client, 'client'),
    ]
    status = models.CharField(
        max_length=13,
        choices=account_select,
        default=client,
    )

    def __str__(self):
        return '{} profile.'.format(self.user.username)


def creat_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(creat_profile, sender=User)
