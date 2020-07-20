from adapay.api import request_tools
from adapay.api.request_tools import request_post


class Bill(object):

    @classmethod
    def download(cls, **kwargs):
        return request_post(request_tools.bill_download, kwargs)


