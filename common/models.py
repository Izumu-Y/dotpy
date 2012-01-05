from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import uuid
import logging

logger = logging.getLogger(__name__)

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    confirm_code = models.CharField(max_length=32, unique=True)

    @staticmethod
    def generate_confirm_code():
        return uuid.uuid4().hex

    def __unicode__(self):
        return 'profile - ' + self.user.__unicode__()

@receiver(post_save, sender=User, dispatch_uid='common.models.create_user_profile')
def create_user_profile(sender, instance, created, **kw_args):
    if created:
        logger.debug('Creating UserProfile for user: %s', instance)
        UserProfile.objects.create(user=instance, confirm_code=UserProfile.generate_confirm_code())
