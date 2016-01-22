from django.test import TestCase

class S3_Test(TestCase):
    def test_send_email(self):
        response = self.client.post('/sendemail', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        assert response.content.__contains__('testValue')
