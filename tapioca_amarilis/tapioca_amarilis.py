from tapioca import TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin
from requests.auth import HTTPBasicAuth

from .resource_mapping import RESOURCE_MAPPING


class AmarilisV1ClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://pms.imoveisamarilis.com.br/api/v1/'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(AmarilisV1ClientAdapter, self).get_request_kwargs(api_params, *args, **kwargs)
        params['auth'] = HTTPBasicAuth(api_params.get('user'), api_params.get('password'))

        return params

    def get_api_root(self, api_params):
        custom_host = api_params.get('host', None)
        if custom_host:
            return custom_host
        return self.api_root

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass


AmarilisV1 = generate_wrapper_from_adapter(AmarilisV1ClientAdapter)
