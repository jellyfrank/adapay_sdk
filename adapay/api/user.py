from adapay.api import request_tools
from adapay.api.request_tools import request_post


class User(object):

    @classmethod
    def query_union_identity(cls, **kwargs):
        return request_post(request_tools.query_identity, kwargs)


