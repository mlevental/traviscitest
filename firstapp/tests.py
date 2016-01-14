from django.test import TestCase

class TestIndexPage(TestCase):
    def test_get_index_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<input type='hidden' name='csrfmiddlewaretoken'")