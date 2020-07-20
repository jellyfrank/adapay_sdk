from adapay.api import request_tools
from adapay.api.request_tools import request_post, request_get


class Account(object):

    @classmethod
    def create_settle(cls, **kwargs):
        """
        创建结算账户
        """
        return request_post(request_tools.settle_account_create, kwargs)

    @classmethod
    def query_settle(cls, **kwargs):
        """
        查询结算账户
        """
        url = request_tools.settle_account_query.format(settle_account_id=kwargs.get('settle_account_id'))
        return request_get(url, kwargs)

    @classmethod
    def modify_settle(cls, **kwargs):
        """
        修改结算配置
        """
        return request_post(request_tools.settle_account_modify, kwargs)

    @classmethod
    def delete_settle(cls, **kwargs):
        """
        删除结算账户
        """
        return request_post(request_tools.settle_account_delete, kwargs)

    @classmethod
    def query_settle_details(cls, **kwargs):
        """
        查询结算账户明细
        """
        return request_get(request_tools.settle_account_detail_query, kwargs)

    @classmethod
    def query_balance(cls, **kwargs):
        """
        查询账户余额
        """
        return request_get(request_tools.settle_account_balance_query, kwargs)

    @classmethod
    def draw_cash(cls, **kwargs):
        """
        取现
        """
        return request_post(request_tools.settle_account_cash_draw, kwargs)


