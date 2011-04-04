from django.test import TestCase
from django.contrib.auth.models import User

from users.models import UserProfile

class UserProfileTest(TestCase):
    def test_create(self):
        """
        Tests that a profile is created automatically for a newly created user.
        """
        self.assertEquals(User.objects.count(), 0)
        self.assertEquals(UserProfile.objects.count(), 0)
        user = User(username='test', email='test@dotpy.org', first_name='Test', last_name='User')
        user.save()
        self.assertEquals(User.objects.count(), 1)
        self.assertEquals(UserProfile.objects.count(), 1)
        profile = user.get_profile()
        self.assertEquals(UserProfile.objects.all()[0], profile)
        self.assertEquals(profile.user, user)

