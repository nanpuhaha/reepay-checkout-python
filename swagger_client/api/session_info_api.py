# coding: utf-8

"""
    Reepay Checkout API

    Reepay Checkout REST API  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SessionInfoApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_session(self, id, **kwargs):  # noqa: E501
        """Get session info  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_session(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Session id (required)
        :return: SessionInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_session_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_session_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_session_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get session info  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_session_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Session id (required)
        :return: SessionInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_session" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_session`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/session_info/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SessionInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sessions(self, relation_type, handle, **kwargs):  # noqa: E501
        """Get sessions by relation type and handle  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sessions(relation_type, handle, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str relation_type: Relation type (required)
        :param str handle: Relation handle (required)
        :return: list[SessionInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sessions_with_http_info(relation_type, handle, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sessions_with_http_info(relation_type, handle, **kwargs)  # noqa: E501
            return data

    def get_sessions_with_http_info(self, relation_type, handle, **kwargs):  # noqa: E501
        """Get sessions by relation type and handle  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sessions_with_http_info(relation_type, handle, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str relation_type: Relation type (required)
        :param str handle: Relation handle (required)
        :return: list[SessionInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['relation_type', 'handle']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sessions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'relation_type' is set
        if ('relation_type' not in params or
                params['relation_type'] is None):
            raise ValueError("Missing the required parameter `relation_type` when calling `get_sessions`")  # noqa: E501
        # verify the required parameter 'handle' is set
        if ('handle' not in params or
                params['handle'] is None):
            raise ValueError("Missing the required parameter `handle` when calling `get_sessions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'relation_type' in params:
            path_params['relation_type'] = params['relation_type']  # noqa: E501
        if 'handle' in params:
            path_params['handle'] = params['handle']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/session_info/{relation_type}/{handle}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SessionInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)