# coding: utf-8

"""
    Reepay Checkout API

    Reepay Checkout REST API  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GooglepayPaymentRequestDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'auth_url': 'str',
        'environment': 'str',
        'api_version': 'int',
        'api_version_minor': 'int',
        'merchant_info': 'MerchantInfo',
        'transaction_info': 'TransactionInfo',
        'allowed_payment_methods': 'list[AllowedPaymentMethod]'
    }

    attribute_map = {
        'auth_url': 'authUrl',
        'environment': 'environment',
        'api_version': 'apiVersion',
        'api_version_minor': 'apiVersionMinor',
        'merchant_info': 'merchantInfo',
        'transaction_info': 'transactionInfo',
        'allowed_payment_methods': 'allowedPaymentMethods'
    }

    def __init__(self, auth_url=None, environment=None, api_version=None, api_version_minor=None, merchant_info=None, transaction_info=None, allowed_payment_methods=None):  # noqa: E501
        """GooglepayPaymentRequestDto - a model defined in Swagger"""  # noqa: E501

        self._auth_url = None
        self._environment = None
        self._api_version = None
        self._api_version_minor = None
        self._merchant_info = None
        self._transaction_info = None
        self._allowed_payment_methods = None
        self.discriminator = None

        if auth_url is not None:
            self.auth_url = auth_url
        if environment is not None:
            self.environment = environment
        if api_version is not None:
            self.api_version = api_version
        if api_version_minor is not None:
            self.api_version_minor = api_version_minor
        if merchant_info is not None:
            self.merchant_info = merchant_info
        if transaction_info is not None:
            self.transaction_info = transaction_info
        if allowed_payment_methods is not None:
            self.allowed_payment_methods = allowed_payment_methods

    @property
    def auth_url(self):
        """Gets the auth_url of this GooglepayPaymentRequestDto.  # noqa: E501


        :return: The auth_url of this GooglepayPaymentRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._auth_url

    @auth_url.setter
    def auth_url(self, auth_url):
        """Sets the auth_url of this GooglepayPaymentRequestDto.


        :param auth_url: The auth_url of this GooglepayPaymentRequestDto.  # noqa: E501
        :type: str
        """

        self._auth_url = auth_url

    @property
    def environment(self):
        """Gets the environment of this GooglepayPaymentRequestDto.  # noqa: E501


        :return: The environment of this GooglepayPaymentRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this GooglepayPaymentRequestDto.


        :param environment: The environment of this GooglepayPaymentRequestDto.  # noqa: E501
        :type: str
        """

        self._environment = environment

    @property
    def api_version(self):
        """Gets the api_version of this GooglepayPaymentRequestDto.  # noqa: E501


        :return: The api_version of this GooglepayPaymentRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this GooglepayPaymentRequestDto.


        :param api_version: The api_version of this GooglepayPaymentRequestDto.  # noqa: E501
        :type: int
        """

        self._api_version = api_version

    @property
    def api_version_minor(self):
        """Gets the api_version_minor of this GooglepayPaymentRequestDto.  # noqa: E501


        :return: The api_version_minor of this GooglepayPaymentRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._api_version_minor

    @api_version_minor.setter
    def api_version_minor(self, api_version_minor):
        """Sets the api_version_minor of this GooglepayPaymentRequestDto.


        :param api_version_minor: The api_version_minor of this GooglepayPaymentRequestDto.  # noqa: E501
        :type: int
        """

        self._api_version_minor = api_version_minor

    @property
    def merchant_info(self):
        """Gets the merchant_info of this GooglepayPaymentRequestDto.  # noqa: E501


        :return: The merchant_info of this GooglepayPaymentRequestDto.  # noqa: E501
        :rtype: MerchantInfo
        """
        return self._merchant_info

    @merchant_info.setter
    def merchant_info(self, merchant_info):
        """Sets the merchant_info of this GooglepayPaymentRequestDto.


        :param merchant_info: The merchant_info of this GooglepayPaymentRequestDto.  # noqa: E501
        :type: MerchantInfo
        """

        self._merchant_info = merchant_info

    @property
    def transaction_info(self):
        """Gets the transaction_info of this GooglepayPaymentRequestDto.  # noqa: E501


        :return: The transaction_info of this GooglepayPaymentRequestDto.  # noqa: E501
        :rtype: TransactionInfo
        """
        return self._transaction_info

    @transaction_info.setter
    def transaction_info(self, transaction_info):
        """Sets the transaction_info of this GooglepayPaymentRequestDto.


        :param transaction_info: The transaction_info of this GooglepayPaymentRequestDto.  # noqa: E501
        :type: TransactionInfo
        """

        self._transaction_info = transaction_info

    @property
    def allowed_payment_methods(self):
        """Gets the allowed_payment_methods of this GooglepayPaymentRequestDto.  # noqa: E501


        :return: The allowed_payment_methods of this GooglepayPaymentRequestDto.  # noqa: E501
        :rtype: list[AllowedPaymentMethod]
        """
        return self._allowed_payment_methods

    @allowed_payment_methods.setter
    def allowed_payment_methods(self, allowed_payment_methods):
        """Sets the allowed_payment_methods of this GooglepayPaymentRequestDto.


        :param allowed_payment_methods: The allowed_payment_methods of this GooglepayPaymentRequestDto.  # noqa: E501
        :type: list[AllowedPaymentMethod]
        """

        self._allowed_payment_methods = allowed_payment_methods

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GooglepayPaymentRequestDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GooglepayPaymentRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
