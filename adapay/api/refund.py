"""
2019.8.1 create by jun.hu
退款接口
"""

from adapay.api.request_tools import refund_create, refund_query, request_post, request_get


class Refund(object):

    @classmethod
    def create(cls, **kwargs):
        """
        发起退款流程
        """

        url = refund_create.format(kwargs.get('payment_id', ''))
        return request_post(url, kwargs)

    @classmethod
    def query(cls, **kwargs):
        """
        退款流程查询
        """

        return request_get(refund_query, kwargs)


