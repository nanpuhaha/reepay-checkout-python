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


class StrongAuth(object):
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
        'amount': 'int',
        'currency': 'str',
        'order_id': 'str',
        'order_text': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency',
        'order_id': 'orderId',
        'order_text': 'orderText'
    }

    def __init__(self, amount=None, currency=None, order_id=None, order_text=None):  # noqa: E501
        """StrongAuth - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._currency = None
        self._order_id = None
        self._order_text = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if order_id is not None:
            self.order_id = order_id
        if order_text is not None:
            self.order_text = order_text

    @property
    def amount(self):
        """Gets the amount of this StrongAuth.  # noqa: E501


        :return: The amount of this StrongAuth.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this StrongAuth.


        :param amount: The amount of this StrongAuth.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this StrongAuth.  # noqa: E501


        :return: The currency of this StrongAuth.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this StrongAuth.


        :param currency: The currency of this StrongAuth.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def order_id(self):
        """Gets the order_id of this StrongAuth.  # noqa: E501


        :return: The order_id of this StrongAuth.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this StrongAuth.


        :param order_id: The order_id of this StrongAuth.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def order_text(self):
        """Gets the order_text of this StrongAuth.  # noqa: E501


        :return: The order_text of this StrongAuth.  # noqa: E501
        :rtype: str
        """
        return self._order_text

    @order_text.setter
    def order_text(self, order_text):
        """Sets the order_text of this StrongAuth.


        :param order_text: The order_text of this StrongAuth.  # noqa: E501
        :type: str
        """

        self._order_text = order_text

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
        if issubclass(StrongAuth, dict):
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
        if not isinstance(other, StrongAuth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other