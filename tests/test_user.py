from django.test import TestCase
from controlcenter.models import User


class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create(username="John", status="working")
        User.objects.create(username="Mary", status="vacation")
        User.objects.create(username="Alex", status="vacation")

    def test_user_status(self):
        john = User.objects.get(username='John')
        self.assertEqual(john.status, 'working')
        john.status = 'vacation'
        john.save()
        self.assertEqual(john.status, 'vacation')
