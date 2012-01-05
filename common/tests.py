from django.test import TestCase
from django.contrib.auth.models import User

from common.models import UserProfile

class UserProfileTest(TestCase):
    def test_generate_confirm_code(self):
        confirm_code = UserProfile.generate_confirm_code()
        self.assertIsNotNone(confirm_code)
        self.assertEqual(len(confirm_code), 32)
        self.assertNotEqual(confirm_code, UserProfile.generate_confirm_code())

    def test_profile_created_when_create_user(self):
        u = User.objects.create(username='demo')
        p = u.get_profile()
        self.assertIsNotNone(p)
        self.assertIsNotNone(p.confirm_code)
        self.assertEqual(len(p.confirm_code), 32)
