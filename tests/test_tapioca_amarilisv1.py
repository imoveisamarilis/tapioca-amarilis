import os
import unittest

from tapioca_amarilisv1 import AmarilisV1


class TestTapiocaAmarilisV1(unittest.TestCase):
    def setUp(self):
        self.api_client = AmarilisV1(
            user=os.getenv('AMARILIS_USER', default=''),
            password=os.getenv('AMARILIS_PASSWORD', default=''),
        )

    def test_resource_access(self):
        resource = self.api_client.bookings()
        assert resource.data == 'https://pms.imoveisamarilis.com.br/api/v1/bookings/'


if __name__ == '__main__':
    unittest.main()
