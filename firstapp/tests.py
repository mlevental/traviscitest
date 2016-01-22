from django.test import TestCase


class TestIndexPage(TestCase):
    def test_get_index_page(self):
        response = self.client.get('')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "<input type='hidden' name='csrfmiddlewaretoken'")
    #
    # def test_post_index_page(self):
    #     response = self.client.post('')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "<input type='hidden' name='csrfmiddlewaretoken'")
    #
    # def test_send_email(self):
    #     response = self.client.post('/sendemail', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    #     self.assertEqual(response.status_code, 200)
    #     assert response.content.__contains__('testValue')