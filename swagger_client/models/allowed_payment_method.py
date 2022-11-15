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


class AllowedPaymentMethod(object):
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
        'type': 'str',
        'parameters': 'AllowedPaymentMethodParameters',
        'tokenization_specification': 'TokenizationSpecification'
    }

    attribute_map = {
        'type': 'type',
        'parameters': 'parameters',
        'tokenization_specification': 'tokenizationSpecification'
    }

    def __init__(self, type=None, parameters=None, tokenization_specification=None):  # noqa: E501
        """AllowedPaymentMethod - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._parameters = None
        self._tokenization_specification = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if parameters is not None:
            self.parameters = parameters
        if tokenization_specification is not None:
            self.tokenization_specification = tokenization_specification

    @property
    def type(self):
        """Gets the type of this AllowedPaymentMethod.  # noqa: E501


        :return: The type of this AllowedPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AllowedPaymentMethod.


        :param type: The type of this AllowedPaymentMethod.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def parameters(self):
        """Gets the parameters of this AllowedPaymentMethod.  # noqa: E501


        :return: The parameters of this AllowedPaymentMethod.  # noqa: E501
        :rtype: AllowedPaymentMethodParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this AllowedPaymentMethod.


        :param parameters: The parameters of this AllowedPaymentMethod.  # noqa: E501
        :type: AllowedPaymentMethodParameters
        """

        self._parameters = parameters

    @property
    def tokenization_specification(self):
        """Gets the tokenization_specification of this AllowedPaymentMethod.  # noqa: E501


        :return: The tokenization_specification of this AllowedPaymentMethod.  # noqa: E501
        :rtype: TokenizationSpecification
        """
        return self._tokenization_specification

    @tokenization_specification.setter
    def tokenization_specification(self, tokenization_specification):
        """Sets the tokenization_specification of this AllowedPaymentMethod.


        :param tokenization_specification: The tokenization_specification of this AllowedPaymentMethod.  # noqa: E501
        :type: TokenizationSpecification
        """

        self._tokenization_specification = tokenization_specification

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
        if issubclass(AllowedPaymentMethod, dict):
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
            if isinstance(other, AllowedPaymentMethod)
            else False
        )

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
