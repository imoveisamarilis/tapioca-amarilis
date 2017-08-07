import os
import unittest

from tapioca_amarilisv1 import AmarilisV1


class TestTapiocaAmarilisV1(unittest.TestCase):
    def test_resource_access(self):
        api_client = AmarilisV1(
            user=os.getenv('AMARILIS_USER', default=''),
            password=os.getenv('AMARILIS_PASSWORD', default=''),
        )
        resource = api_client.bookings()
        assert resource.data == 'https://pms.imoveisamarilis.com.br/api/v1/bookings/'

    def test_homolog_api_root(self):
        api_client = AmarilisV1(
            user=os.getenv('AMARILIS_USER', default=''),
            password=os.getenv('AMARILIS_PASSWORD', default=''),
            debug=True
        )
        resource = api_client.bookings()
        assert resource.data == 'https://hlg-pms.imoveisamarilis.com.br/api/v1/bookings/'

    def test_custom_api_root(self):
        api_client = AmarilisV1(
            user=os.getenv('AMARILIS_USER', default=''),
            password=os.getenv('AMARILIS_PASSWORD', default=''),
            debug=True,
            api_root='http://localhost:8000/api/v1/'
        )
        resource = api_client.bookings()
        assert resource.data == 'http://localhost:8000/api/v1/bookings/'


if __name__ == '__main__':
    unittest.main()
