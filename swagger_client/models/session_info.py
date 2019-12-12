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


class SessionInfo(object):
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
        'id': 'str',
        'type': 'str',
        'configuration': 'str',
        'locale': 'str',
        'expires': 'datetime',
        'charge': 'str',
        'settle': 'bool',
        'recurring': 'bool',
        'customer': 'str',
        'subscription': 'str',
        'created': 'datetime',
        'currency': 'str',
        'agent': 'str',
        'url': 'str',
        'cancel_url': 'str',
        'accept_url': 'str',
        'payment_methods': 'list[str]',
        'card_on_file': 'str',
        'button_text': 'str',
        'subscription_session_done': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'configuration': 'configuration',
        'locale': 'locale',
        'expires': 'expires',
        'charge': 'charge',
        'settle': 'settle',
        'recurring': 'recurring',
        'customer': 'customer',
        'subscription': 'subscription',
        'created': 'created',
        'currency': 'currency',
        'agent': 'agent',
        'url': 'url',
        'cancel_url': 'cancel_url',
        'accept_url': 'accept_url',
        'payment_methods': 'payment_methods',
        'card_on_file': 'card_on_file',
        'button_text': 'button_text',
        'subscription_session_done': 'subscription_session_done'
    }

    def __init__(self, id=None, type=None, configuration=None, locale=None, expires=None, charge=None, settle=None, recurring=None, customer=None, subscription=None, created=None, currency=None, agent=None, url=None, cancel_url=None, accept_url=None, payment_methods=None, card_on_file=None, button_text=None, subscription_session_done=None):  # noqa: E501
        """SessionInfo - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._type = None
        self._configuration = None
        self._locale = None
        self._expires = None
        self._charge = None
        self._settle = None
        self._recurring = None
        self._customer = None
        self._subscription = None
        self._created = None
        self._currency = None
        self._agent = None
        self._url = None
        self._cancel_url = None
        self._accept_url = None
        self._payment_methods = None
        self._card_on_file = None
        self._button_text = None
        self._subscription_session_done = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if configuration is not None:
            self.configuration = configuration
        if locale is not None:
            self.locale = locale
        if expires is not None:
            self.expires = expires
        if charge is not None:
            self.charge = charge
        if settle is not None:
            self.settle = settle
        if recurring is not None:
            self.recurring = recurring
        if customer is not None:
            self.customer = customer
        if subscription is not None:
            self.subscription = subscription
        if created is not None:
            self.created = created
        if currency is not None:
            self.currency = currency
        if agent is not None:
            self.agent = agent
        if url is not None:
            self.url = url
        if cancel_url is not None:
            self.cancel_url = cancel_url
        if accept_url is not None:
            self.accept_url = accept_url
        if payment_methods is not None:
            self.payment_methods = payment_methods
        if card_on_file is not None:
            self.card_on_file = card_on_file
        if button_text is not None:
            self.button_text = button_text
        if subscription_session_done is not None:
            self.subscription_session_done = subscription_session_done

    @property
    def id(self):
        """Gets the id of this SessionInfo.  # noqa: E501


        :return: The id of this SessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SessionInfo.


        :param id: The id of this SessionInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this SessionInfo.  # noqa: E501


        :return: The type of this SessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SessionInfo.


        :param type: The type of this SessionInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["CHARGE", "RECURRING", "SUBSCRIPTION", "SUBSCRIPTION_CHARGE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def configuration(self):
        """Gets the configuration of this SessionInfo.  # noqa: E501


        :return: The configuration of this SessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this SessionInfo.


        :param configuration: The configuration of this SessionInfo.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def locale(self):
        """Gets the locale of this SessionInfo.  # noqa: E501


        :return: The locale of this SessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this SessionInfo.


        :param locale: The locale of this SessionInfo.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def expires(self):
        """Gets the expires of this SessionInfo.  # noqa: E501


        :return: The expires of this SessionInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this SessionInfo.


        :param expires: The expires of this SessionInfo.  # noqa: E501
        :type: datetime
        """

        self._expires = expires

    @property
    def charge(self):
        """Gets the charge of this SessionInfo.  # noqa: E501


        :return: The charge of this SessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._charge

    @charge.setter
    def charge(self, charge):
        """Sets the charge of this SessionInfo.


        :param charge: The charge of this SessionInfo.  # noqa: E501
        :type: str
        """

        self._charge = charge

    @property
    def settle(self):
        """Gets the settle of this SessionInfo.  # noqa: E501


        :return: The settle of this SessionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._settle

    @settle.setter
    def settle(self, settle):
        """Sets the settle of this SessionInfo.


        :param settle: The settle of this SessionInfo.  # noqa: E501
        :type: bool
        """

        self._settle = settle

    @property
    def recurring(self):
        """Gets the recurring of this SessionInfo.  # noqa: E501


        :return: The recurring of this SessionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._recurring

    @recurring.setter
    def recurring(self, recurring):
        """Sets the recurring of this SessionInfo.


        :param recurring: The recurring of this SessionInfo.  # noqa: E501
        :type: bool
        """

        self._recurring = recurring

    @property
    def customer(self):
        """Gets the customer of this SessionInfo.  # noqa: E501


        :return: The customer of this SessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this SessionInfo.


        :param customer: The customer of this SessionInfo.  # noqa: E501
        :type: str
        """

        self._customer = customer

    @property
    def subscription(self):
        """Gets the subscription of this SessionInfo.  # noqa: E501


        :return: The subscription of this SessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this SessionInfo.


        :param subscription: The subscription of this SessionInfo.  # noqa: E501
        :type: str
        """

        self._subscription = subscription

    @property
    def created(self):
        """Gets the created of this SessionInfo.  # noqa: E501


        :return: The created of this SessionInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SessionInfo.


        :param created: The created of this SessionInfo.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def currency(self):
        """Gets the currency of this SessionInfo.  # noqa: E501


        :return: The currency of this SessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SessionInfo.


        :param currency: The currency of this SessionInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNDEFINED", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYR", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "USS", "UYI", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XBA", "XBB", "XBC", "XBD", "XCD", "XDR", "XOF", "XPD", "XPF", "XPT", "XSU", "XTS", "XUA", "XXX", "YER", "ZAR", "ZMW", "ZWL"]  # noqa: E501
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"  # noqa: E501
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def agent(self):
        """Gets the agent of this SessionInfo.  # noqa: E501


        :return: The agent of this SessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this SessionInfo.


        :param agent: The agent of this SessionInfo.  # noqa: E501
        :type: str
        """

        self._agent = agent

    @property
    def url(self):
        """Gets the url of this SessionInfo.  # noqa: E501


        :return: The url of this SessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SessionInfo.


        :param url: The url of this SessionInfo.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def cancel_url(self):
        """Gets the cancel_url of this SessionInfo.  # noqa: E501


        :return: The cancel_url of this SessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._cancel_url

    @cancel_url.setter
    def cancel_url(self, cancel_url):
        """Sets the cancel_url of this SessionInfo.


        :param cancel_url: The cancel_url of this SessionInfo.  # noqa: E501
        :type: str
        """

        self._cancel_url = cancel_url

    @property
    def accept_url(self):
        """Gets the accept_url of this SessionInfo.  # noqa: E501


        :return: The accept_url of this SessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._accept_url

    @accept_url.setter
    def accept_url(self, accept_url):
        """Sets the accept_url of this SessionInfo.


        :param accept_url: The accept_url of this SessionInfo.  # noqa: E501
        :type: str
        """

        self._accept_url = accept_url

    @property
    def payment_methods(self):
        """Gets the payment_methods of this SessionInfo.  # noqa: E501


        :return: The payment_methods of this SessionInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._payment_methods

    @payment_methods.setter
    def payment_methods(self, payment_methods):
        """Sets the payment_methods of this SessionInfo.


        :param payment_methods: The payment_methods of this SessionInfo.  # noqa: E501
        :type: list[str]
        """

        self._payment_methods = payment_methods

    @property
    def card_on_file(self):
        """Gets the card_on_file of this SessionInfo.  # noqa: E501


        :return: The card_on_file of this SessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._card_on_file

    @card_on_file.setter
    def card_on_file(self, card_on_file):
        """Sets the card_on_file of this SessionInfo.


        :param card_on_file: The card_on_file of this SessionInfo.  # noqa: E501
        :type: str
        """

        self._card_on_file = card_on_file

    @property
    def button_text(self):
        """Gets the button_text of this SessionInfo.  # noqa: E501


        :return: The button_text of this SessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._button_text

    @button_text.setter
    def button_text(self, button_text):
        """Sets the button_text of this SessionInfo.


        :param button_text: The button_text of this SessionInfo.  # noqa: E501
        :type: str
        """

        self._button_text = button_text

    @property
    def subscription_session_done(self):
        """Gets the subscription_session_done of this SessionInfo.  # noqa: E501


        :return: The subscription_session_done of this SessionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._subscription_session_done

    @subscription_session_done.setter
    def subscription_session_done(self, subscription_session_done):
        """Sets the subscription_session_done of this SessionInfo.


        :param subscription_session_done: The subscription_session_done of this SessionInfo.  # noqa: E501
        :type: bool
        """

        self._subscription_session_done = subscription_session_done

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
        if issubclass(SessionInfo, dict):
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
        if not isinstance(other, SessionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
