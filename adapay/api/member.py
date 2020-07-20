from adapay.api import request_tools
from adapay.api.request_tools import request_post, request_get


class Member(object):

    @classmethod
    def create(cls, **kwargs):
        """
        创建用户
        """
        return request_post(request_tools.member_create, kwargs)

    @classmethod
    def query(cls, **kwargs):
        """
        查询用户
        """
        url = request_tools.member_query.format(member_id=kwargs.get('member_id'))
        return request_get(url, kwargs)

    @classmethod
    def query_list(cls, **kwargs):
        """
        查询用户
        """
        return request_get(request_tools.member_query_list, kwargs)

    @classmethod
    def update(cls, **kwargs):
        """
        更新用户
        """
        return request_post(request_tools.member_update, kwargs)


