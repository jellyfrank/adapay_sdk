import adapay
from adapay_core import ApiRequest

pay_message_token = '/v1/token/apply'

payment_create = '/v1/payments'
payment_confirm = '/v1/payments/confirm'
payment_confirm_query = '/v1/payments/confirm/{payment_confirm_id}'
payment_confirm_query_list = '/v1/payments/confirm/list'
payment_reverse = '/v1/payments/reverse'
payment_reverse_query = '/v1/payments/reverse/{reverse_id}'
payment_reverse_query_list = '/v1/payments/reverse/list'
payment_query = '/v1/payments/{payment_id}'
payment_close = '/v1/payments/{}/close'

refund_create = '/v1/payments/{}/refunds'
refund_query = '/v1/payments/refunds'

bill_download = '/v1/bill/download'

member_create = '/v1/members'
member_query = '/v1/members/{member_id}'
member_query_list = '/v1/members/list'
member_update = '/v1/members/update'
corp_member_create = '/v1/corp_members'
corp_member_query = '/v1/corp_members/{member_id}'

settle_account_create = '/v1/settle_accounts'
settle_account_modify = '/v1/settle_accounts/modify'
settle_account_query = '/v1/settle_accounts/{settle_account_id}'
settle_account_delete = '/v1/settle_accounts/delete'
settle_account_detail_query = '/v1/settle_accounts/settle_details'
settle_account_balance_query = '/v1/settle_accounts/balance'
settle_account_cash_draw = '/v1/cashs'

query_identity = '/v1/union/user_identity'

wallet_login = '/v1/walletLogin'
wallet_pay = '/v1/account/payment'


def __request_init(url, request_params, base_url):
    ApiRequest.base_url = base_url
    ApiRequest.build(adapay.api_key, adapay.private_key, adapay.public_key, url, request_params, adapay.__version__,
                     adapay.connect_timeout)


def request_post(url, request_params, files=None, base_url=adapay.base_url):
    __request_init(url, request_params, base_url)
    return ApiRequest.post(files)


def request_get(url, request_params, base_url=adapay.base_url):
    __request_init(url, request_params, base_url)
    return ApiRequest.get()
