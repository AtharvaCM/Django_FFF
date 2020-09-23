from django.test import TestCase
from django.contrib.auth.models import User
from fff.models import Profile


class UserTestCase(TestCase):
    user = None

    def setUp(self):
        print("inside setup boiz")
        self.user = User.objects.create_user(
            username='testuser', email='test@sample.com', password='Samplepass1')
        # self.profile = Profile.objects.create(user=self.user)

    # MODEL TEST
    def test_user_creation(self):
        print("in hereeee")
        # u = self.setUp()
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(self.user.username, 'testuser')
