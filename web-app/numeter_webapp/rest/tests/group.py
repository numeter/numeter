"""
Tests for group REST management.
"""

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from core.models import Group
from core.tests.utils import set_users
from rest.tests.utils import set_clients

LIST_URL = reverse('group-list')

class Group_GET_list_Test(APITestCase):
    """
    Test GET list. Same as
    ``curl -i -X GET http://127.0.0.1:8081/rest/groups/ -H 'Accept: application/json'``
    """
    @set_users()
    @set_clients()
    def setUp(self):
        self.DETAIL_URL = reverse('group-detail', args=[Group.objects.all()[0].pk])

    def test_anonymous(self):
        """Forbidden access to anonymous."""
        r = self.client.get(LIST_URL)
        self.assertEqual(r.status_code, 401, 'Bad response (%i)' % r.status_code)

    def test_superuser(self):
        """Granted access for superuser."""
        r = self.admin_client.get(LIST_URL)
        self.assertEqual(r.status_code, 200, 'Bad response (%i)' % r.status_code)

    def test_simple_user(self):
        """Forbidden access to simple user."""
        r = self.user_client.get(LIST_URL)
        self.assertEqual(r.status_code, 403, 'Bad response (%i)' % r.status_code)


class Group_GET_detail_Test(APITestCase):
    """
    Test GET details. Same as
    ``curl -i -X GET http://127.0.0.1:8081/rest/groups/1 -H 'Accept: application/json'``
    """
    @set_users()
    @set_clients()
    def setUp(self):
        self.DETAIL_URL = reverse('group-detail', args=[Group.objects.all()[0].pk])

    def test_anonymous(self):
        """Forbidden access to anonymous."""
        r = self.client.get(self.DETAIL_URL)
        self.assertEqual(r.status_code, 401, 'Bad response (%i)' % r.status_code)

    def test_superuser(self):
        """Granted access for superuser."""
        r = self.admin_client.get(self.DETAIL_URL)
        self.assertEqual(r.status_code, 200, 'Bad response (%i)' % r.status_code)

    def test_simple_user(self):
        """Forbidden access to simple group."""
        r = self.user_client.get(self.DETAIL_URL)
        self.assertEqual(r.status_code, 403, 'Bad response (%i)' % r.status_code)


class Group_POST_Test(APITestCase):
    """
    Test POST. Same as
    ``curl -i -X POST http://127.0.0.1:8081/rest/groups/ -H 'Accept: application/json'``
    """
    @set_users()
    @set_clients()
    def setUp(self):
        self.DETAIL_URL = reverse('group-detail', args=[Group.objects.all()[0].pk])

    def test_anonymous(self):
        """Forbidden access to anonymous."""
        r = self.client.post(LIST_URL)
        self.assertEqual(r.status_code, 401, 'Bad response (%i)' % r.status_code)

    def test_superuser(self):
        """Granted access for superuser."""
        data = {'name':'NEW GROUP'}
        r = self.admin_client.post(LIST_URL, data=data)
        self.assertEqual(r.status_code, 201, 'Bad response (%i)' % r.status_code)

    def test_simple_user(self):
        """Forbidden access to simple user."""
        data = {'name':'NEW GROUP'}
        r = self.user_client.post(LIST_URL)
        self.assertEqual(r.status_code, 403, 'Bad response (%i)' % r.status_code)


class Group_DELETE_Test(APITestCase):
    """
    Test DELETE. Same as
    ``curl -i -X DELETE http://127.0.0.1:8081/rest/groups/1 -H 'Accept: application/json'``
    """
    @set_users()
    @set_clients()
    def setUp(self):
        self.DETAIL_URL = reverse('group-detail', args=[Group.objects.all()[0].pk])

    def test_anonymous(self):
        """Forbidden access to anonymous."""
        r = self.client.delete(self.DETAIL_URL)
        self.assertEqual(r.status_code, 401, 'Bad response (%i)' % r.status_code)

    def test_superuser(self):
        """Granted access for superuser."""
        r = self.admin_client.delete(self.DETAIL_URL)
        self.assertEqual(r.status_code, 204, 'Bad response (%i)' % r.status_code)

    def test_simple_user(self):
        """Forbidden access to simple group."""
        r = self.user_client.delete(self.DETAIL_URL)
        self.assertEqual(r.status_code, 403, 'Bad response (%i)' % r.status_code)


class Group_PATCH_Test(APITestCase):
    """
    Test PATCH. Same as
    ``curl -i -X PATCH http://127.0.0.1:8081/rest/groups/1 -H 'Accept: application/json'``
    """
    @set_users()
    @set_clients()
    def setUp(self):
        self.DETAIL_URL = reverse('group-detail', args=[Group.objects.all()[0].pk])

    def test_anonymous(self):
        """Forbidden access to anonymous."""
        r = self.client.patch(self.DETAIL_URL)
        self.assertEqual(r.status_code, 401, 'Bad response (%i)' % r.status_code)

    def test_superuser(self):
        """Granted access for superuser."""
        data = {'name':'NEW GROUP'}
        r = self.admin_client.patch(self.DETAIL_URL, data=data)
        self.assertEqual(r.status_code, 200, 'Bad response (%i)' % r.status_code)

    def test_simple_user(self):
        """Forbidden access to simple group."""
        r = self.user_client.patch(self.DETAIL_URL)
        self.assertEqual(r.status_code, 403, 'Bad response (%i)' % r.status_code)
