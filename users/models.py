from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User

from dotpy.core.utils import generate_code

import logging

logger = logging.getLogger(__name__)

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    email_verified = models.BooleanField(default=False)
    confirm_code = models.CharField(max_length=20, null=True, blank=True)
    website = models.URLField(max_length=64, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.user.username

def create_user_profile(sender, instance=None, **kwargs):
    if instance and kwargs.get('created', False):
        confirm_code = generate_code(20)
        MAX_TRIED_TIMES = 3
        count = 0
        while UserProfile.objects.filter(confirm_code=confirm_code).exists():
            logger.info('Confirm-code exists in database: %s' % confirm_code)
            count += 1
            if count >= MAX_TRIED_TIMES:
                log.error('Tried %d times to generate code. Give up.' % MAX_TRIED_TIMES)
                raise Exception('Code generated exists and are always the same!')
            confirm_code = generate_code(20)
        profile = UserProfile(user=instance, confirm_code=confirm_code)
        profile.save()

def delete_user_profile(sender, instance=None, **kwargs):
    if instance:
        profile = instance.get_profile()
        profile.delete()

post_save.connect(create_user_profile, sender=User, dispatch_uid='dotpy.users.modes.UserProfile')
pre_delete.connect(delete_user_profile, sender=User, dispatch_uid='dotpy.users.modes.UserProfile')
