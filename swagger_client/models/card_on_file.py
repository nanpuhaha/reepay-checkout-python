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


class CardOnFile(object):
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
        'card_type': 'str',
        'exp_date': 'str',
        'masked_card': 'str',
        'token': 'str'
    }

    attribute_map = {
        'card_type': 'cardType',
        'exp_date': 'expDate',
        'masked_card': 'maskedCard',
        'token': 'token'
    }

    def __init__(self, card_type=None, exp_date=None, masked_card=None, token=None):  # noqa: E501
        """CardOnFile - a model defined in Swagger"""  # noqa: E501

        self._card_type = None
        self._exp_date = None
        self._masked_card = None
        self._token = None
        self.discriminator = None

        if card_type is not None:
            self.card_type = card_type
        if exp_date is not None:
            self.exp_date = exp_date
        if masked_card is not None:
            self.masked_card = masked_card
        if token is not None:
            self.token = token

    @property
    def card_type(self):
        """Gets the card_type of this CardOnFile.  # noqa: E501


        :return: The card_type of this CardOnFile.  # noqa: E501
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this CardOnFile.


        :param card_type: The card_type of this CardOnFile.  # noqa: E501
        :type: str
        """

        self._card_type = card_type

    @property
    def exp_date(self):
        """Gets the exp_date of this CardOnFile.  # noqa: E501


        :return: The exp_date of this CardOnFile.  # noqa: E501
        :rtype: str
        """
        return self._exp_date

    @exp_date.setter
    def exp_date(self, exp_date):
        """Sets the exp_date of this CardOnFile.


        :param exp_date: The exp_date of this CardOnFile.  # noqa: E501
        :type: str
        """

        self._exp_date = exp_date

    @property
    def masked_card(self):
        """Gets the masked_card of this CardOnFile.  # noqa: E501


        :return: The masked_card of this CardOnFile.  # noqa: E501
        :rtype: str
        """
        return self._masked_card

    @masked_card.setter
    def masked_card(self, masked_card):
        """Sets the masked_card of this CardOnFile.


        :param masked_card: The masked_card of this CardOnFile.  # noqa: E501
        :type: str
        """

        self._masked_card = masked_card

    @property
    def token(self):
        """Gets the token of this CardOnFile.  # noqa: E501


        :return: The token of this CardOnFile.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CardOnFile.


        :param token: The token of this CardOnFile.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if issubclass(CardOnFile, dict):
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
        return (
            self.__dict__ == other.__dict__
            if isinstance(other, CardOnFile)
            else False
        )

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
