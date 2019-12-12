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


class CreateSubscriptionSession(object):
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
        'configuration': 'str',
        'locale': 'str',
        'ttl': 'str',
        'subscription': 'str',
        'accept_url': 'str',
        'cancel_url': 'str',
        'payment_methods': 'list[str]',
        'button_text': 'str',
        'prepare_subscription': 'CreatePreparedSubscription'
    }

    attribute_map = {
        'configuration': 'configuration',
        'locale': 'locale',
        'ttl': 'ttl',
        'subscription': 'subscription',
        'accept_url': 'accept_url',
        'cancel_url': 'cancel_url',
        'payment_methods': 'payment_methods',
        'button_text': 'button_text',
        'prepare_subscription': 'prepare_subscription'
    }

    def __init__(self, configuration=None, locale=None, ttl=None, subscription=None, accept_url=None, cancel_url=None, payment_methods=None, button_text=None, prepare_subscription=None):  # noqa: E501
        """CreateSubscriptionSession - a model defined in Swagger"""  # noqa: E501

        self._configuration = None
        self._locale = None
        self._ttl = None
        self._subscription = None
        self._accept_url = None
        self._cancel_url = None
        self._payment_methods = None
        self._button_text = None
        self._prepare_subscription = None
        self.discriminator = None

        if configuration is not None:
            self.configuration = configuration
        if locale is not None:
            self.locale = locale
        if ttl is not None:
            self.ttl = ttl
        if subscription is not None:
            self.subscription = subscription
        if accept_url is not None:
            self.accept_url = accept_url
        if cancel_url is not None:
            self.cancel_url = cancel_url
        if payment_methods is not None:
            self.payment_methods = payment_methods
        if button_text is not None:
            self.button_text = button_text
        if prepare_subscription is not None:
            self.prepare_subscription = prepare_subscription

    @property
    def configuration(self):
        """Gets the configuration of this CreateSubscriptionSession.  # noqa: E501

        Optional handle for a configuration to use for this session  # noqa: E501

        :return: The configuration of this CreateSubscriptionSession.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this CreateSubscriptionSession.

        Optional handle for a configuration to use for this session  # noqa: E501

        :param configuration: The configuration of this CreateSubscriptionSession.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def locale(self):
        """Gets the locale of this CreateSubscriptionSession.  # noqa: E501

        Optional locale for session. E.g. `en_GB`, `da_DK`, `es_ES`. Defaults to configuration locale or account locale.   # noqa: E501

        :return: The locale of this CreateSubscriptionSession.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this CreateSubscriptionSession.

        Optional locale for session. E.g. `en_GB`, `da_DK`, `es_ES`. Defaults to configuration locale or account locale.   # noqa: E501

        :param locale: The locale of this CreateSubscriptionSession.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def ttl(self):
        """Gets the ttl of this CreateSubscriptionSession.  # noqa: E501

        Optional time-to-live duration. The session will expire after the duration from creation. The duration must be given as an ISO-8601 duration. See https://en.wikipedia.org/wiki/ISO_8601#Durations. E.g. PT3H (three hours).  # noqa: E501

        :return: The ttl of this CreateSubscriptionSession.  # noqa: E501
        :rtype: str
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this CreateSubscriptionSession.

        Optional time-to-live duration. The session will expire after the duration from creation. The duration must be given as an ISO-8601 duration. See https://en.wikipedia.org/wiki/ISO_8601#Durations. E.g. PT3H (three hours).  # noqa: E501

        :param ttl: The ttl of this CreateSubscriptionSession.  # noqa: E501
        :type: str
        """

        self._ttl = ttl

    @property
    def subscription(self):
        """Gets the subscription of this CreateSubscriptionSession.  # noqa: E501

        Handle for existing subscription to activate, add payment method to or change payment method for. Either this argument must be provided or `prepare_subscription`.  # noqa: E501

        :return: The subscription of this CreateSubscriptionSession.  # noqa: E501
        :rtype: str
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this CreateSubscriptionSession.

        Handle for existing subscription to activate, add payment method to or change payment method for. Either this argument must be provided or `prepare_subscription`.  # noqa: E501

        :param subscription: The subscription of this CreateSubscriptionSession.  # noqa: E501
        :type: str
        """

        self._subscription = subscription

    @property
    def accept_url(self):
        """Gets the accept_url of this CreateSubscriptionSession.  # noqa: E501

        If checkout is opened in separate window the customer will be directed to this page after success  # noqa: E501

        :return: The accept_url of this CreateSubscriptionSession.  # noqa: E501
        :rtype: str
        """
        return self._accept_url

    @accept_url.setter
    def accept_url(self, accept_url):
        """Sets the accept_url of this CreateSubscriptionSession.

        If checkout is opened in separate window the customer will be directed to this page after success  # noqa: E501

        :param accept_url: The accept_url of this CreateSubscriptionSession.  # noqa: E501
        :type: str
        """

        self._accept_url = accept_url

    @property
    def cancel_url(self):
        """Gets the cancel_url of this CreateSubscriptionSession.  # noqa: E501

        If checkout is opened in separate window the customer will be directed to this page if the customer cancels  # noqa: E501

        :return: The cancel_url of this CreateSubscriptionSession.  # noqa: E501
        :rtype: str
        """
        return self._cancel_url

    @cancel_url.setter
    def cancel_url(self, cancel_url):
        """Sets the cancel_url of this CreateSubscriptionSession.

        If checkout is opened in separate window the customer will be directed to this page if the customer cancels  # noqa: E501

        :param cancel_url: The cancel_url of this CreateSubscriptionSession.  # noqa: E501
        :type: str
        """

        self._cancel_url = cancel_url

    @property
    def payment_methods(self):
        """Gets the payment_methods of this CreateSubscriptionSession.  # noqa: E501

        Optional list of payment methods to use for the checkout session. Format: `<payment_methods> = list of <payment_method>` `<payment_method>  = [sca-|scafallback-|nosca-|]<payment_name>` `<payment_name>    = The id of payment method, e.g. dankort` See https://docs.reepay.com/docs/checkout-payment-methods for full documentation  # noqa: E501

        :return: The payment_methods of this CreateSubscriptionSession.  # noqa: E501
        :rtype: list[str]
        """
        return self._payment_methods

    @payment_methods.setter
    def payment_methods(self, payment_methods):
        """Sets the payment_methods of this CreateSubscriptionSession.

        Optional list of payment methods to use for the checkout session. Format: `<payment_methods> = list of <payment_method>` `<payment_method>  = [sca-|scafallback-|nosca-|]<payment_name>` `<payment_name>    = The id of payment method, e.g. dankort` See https://docs.reepay.com/docs/checkout-payment-methods for full documentation  # noqa: E501

        :param payment_methods: The payment_methods of this CreateSubscriptionSession.  # noqa: E501
        :type: list[str]
        """

        self._payment_methods = payment_methods

    @property
    def button_text(self):
        """Gets the button_text of this CreateSubscriptionSession.  # noqa: E501

        Optional alternative button text. Maximum length 32 characters.  # noqa: E501

        :return: The button_text of this CreateSubscriptionSession.  # noqa: E501
        :rtype: str
        """
        return self._button_text

    @button_text.setter
    def button_text(self, button_text):
        """Sets the button_text of this CreateSubscriptionSession.

        Optional alternative button text. Maximum length 32 characters.  # noqa: E501

        :param button_text: The button_text of this CreateSubscriptionSession.  # noqa: E501
        :type: str
        """

        self._button_text = button_text

    @property
    def prepare_subscription(self):
        """Gets the prepare_subscription of this CreateSubscriptionSession.  # noqa: E501

        Prepare subscription object. Either this argument must be provided or reference to existing subscription in `subscription`.  # noqa: E501

        :return: The prepare_subscription of this CreateSubscriptionSession.  # noqa: E501
        :rtype: CreatePreparedSubscription
        """
        return self._prepare_subscription

    @prepare_subscription.setter
    def prepare_subscription(self, prepare_subscription):
        """Sets the prepare_subscription of this CreateSubscriptionSession.

        Prepare subscription object. Either this argument must be provided or reference to existing subscription in `subscription`.  # noqa: E501

        :param prepare_subscription: The prepare_subscription of this CreateSubscriptionSession.  # noqa: E501
        :type: CreatePreparedSubscription
        """

        self._prepare_subscription = prepare_subscription

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
        if issubclass(CreateSubscriptionSession, dict):
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
        if not isinstance(other, CreateSubscriptionSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
