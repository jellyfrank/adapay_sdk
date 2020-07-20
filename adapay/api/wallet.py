from adapay.api import request_tools
from adapay.api.request_tools import request_post


class Wallet(object):
    wallet_base_url = 'https://page.adapay.tech'

    @classmethod
    def login(cls, **kwargs):
        """
        钱包用户登录
        :param kwargs:
        :return:
        """
        return request_post(request_tools.wallet_login, kwargs, base_url=Wallet.wallet_base_url)

    @classmethod
    def pay(cls, **kwargs):
        """
        钱包支付
        :param kwargs:
        :return:
        """
        return request_post(request_tools.wallet_pay, kwargs, base_url=Wallet.wallet_base_url)


