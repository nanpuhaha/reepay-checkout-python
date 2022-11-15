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


class Charge(object):
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
        'handle': 'str',
        'state': 'str',
        'customer': 'str',
        'amount': 'int',
        'currency': 'str',
        'authorized': 'datetime',
        'settled': 'datetime',
        'cancelled': 'datetime',
        'created': 'datetime',
        'transaction': 'str',
        'error': 'str',
        'source': 'ChargeSource',
        'order_lines': 'list[OrderLine]',
        'refunded_amount': 'int',
        'authorized_amount': 'int',
        'error_state': 'str',
        'recurring_payment_method': 'str',
        'billing_address': 'InvoiceBillingAddress',
        'shipping_address': 'InvoiceShippingAddress'
    }

    attribute_map = {
        'handle': 'handle',
        'state': 'state',
        'customer': 'customer',
        'amount': 'amount',
        'currency': 'currency',
        'authorized': 'authorized',
        'settled': 'settled',
        'cancelled': 'cancelled',
        'created': 'created',
        'transaction': 'transaction',
        'error': 'error',
        'source': 'source',
        'order_lines': 'order_lines',
        'refunded_amount': 'refunded_amount',
        'authorized_amount': 'authorized_amount',
        'error_state': 'error_state',
        'recurring_payment_method': 'recurring_payment_method',
        'billing_address': 'billing_address',
        'shipping_address': 'shipping_address'
    }

    def __init__(self, handle=None, state=None, customer=None, amount=None, currency=None, authorized=None, settled=None, cancelled=None, created=None, transaction=None, error=None, source=None, order_lines=None, refunded_amount=None, authorized_amount=None, error_state=None, recurring_payment_method=None, billing_address=None, shipping_address=None):  # noqa: E501
        """Charge - a model defined in Swagger"""  # noqa: E501

        self._handle = None
        self._state = None
        self._customer = None
        self._amount = None
        self._currency = None
        self._authorized = None
        self._settled = None
        self._cancelled = None
        self._created = None
        self._transaction = None
        self._error = None
        self._source = None
        self._order_lines = None
        self._refunded_amount = None
        self._authorized_amount = None
        self._error_state = None
        self._recurring_payment_method = None
        self._billing_address = None
        self._shipping_address = None
        self.discriminator = None

        self.handle = handle
        self.state = state
        self.customer = customer
        self.amount = amount
        self.currency = currency
        if authorized is not None:
            self.authorized = authorized
        if settled is not None:
            self.settled = settled
        if cancelled is not None:
            self.cancelled = cancelled
        self.created = created
        if transaction is not None:
            self.transaction = transaction
        if error is not None:
            self.error = error
        self.source = source
        self.order_lines = order_lines
        self.refunded_amount = refunded_amount
        self.authorized_amount = authorized_amount
        if error_state is not None:
            self.error_state = error_state
        if recurring_payment_method is not None:
            self.recurring_payment_method = recurring_payment_method
        if billing_address is not None:
            self.billing_address = billing_address
        if shipping_address is not None:
            self.shipping_address = shipping_address

    @property
    def handle(self):
        """Gets the handle of this Charge.  # noqa: E501

        Per account unique reference to charge/invoice. E.g. order id from own system. Multiple payments can be attempted for the same handle but only one succeeded charge can exist per handle. Max length 255 with allowable characters [a-zA-Z0-9_.-@].  # noqa: E501

        :return: The handle of this Charge.  # noqa: E501
        :rtype: str
        """
        return self._handle

    @handle.setter
    def handle(self, handle):
        """Sets the handle of this Charge.

        Per account unique reference to charge/invoice. E.g. order id from own system. Multiple payments can be attempted for the same handle but only one succeeded charge can exist per handle. Max length 255 with allowable characters [a-zA-Z0-9_.-@].  # noqa: E501

        :param handle: The handle of this Charge.  # noqa: E501
        :type: str
        """
        if handle is None:
            raise ValueError("Invalid value for `handle`, must not be `None`")  # noqa: E501

        self._handle = handle

    @property
    def state(self):
        """Gets the state of this Charge.  # noqa: E501

        The charge state one of the following: `authorized`, `settled`, `failed`, `cancelled`  # noqa: E501

        :return: The state of this Charge.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Charge.

        The charge state one of the following: `authorized`, `settled`, `failed`, `cancelled`  # noqa: E501

        :param state: The state of this Charge.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["authorized", "settled", "failed", "cancelled"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def customer(self):
        """Gets the customer of this Charge.  # noqa: E501

        Customer handle  # noqa: E501

        :return: The customer of this Charge.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this Charge.

        Customer handle  # noqa: E501

        :param customer: The customer of this Charge.  # noqa: E501
        :type: str
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def amount(self):
        """Gets the amount of this Charge.  # noqa: E501

        The invoice amount including VAT  # noqa: E501

        :return: The amount of this Charge.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Charge.

        The invoice amount including VAT  # noqa: E501

        :param amount: The amount of this Charge.  # noqa: E501
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501
        if amount < 0:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `0`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this Charge.  # noqa: E501

        Currency for the account in [ISO 4217](http://da.wikipedia.org/wiki/ISO_4217) three letter alpha code  # noqa: E501

        :return: The currency of this Charge.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Charge.

        Currency for the account in [ISO 4217](http://da.wikipedia.org/wiki/ISO_4217) three letter alpha code  # noqa: E501

        :param currency: The currency of this Charge.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def authorized(self):
        """Gets the authorized of this Charge.  # noqa: E501

        When the charge was authorized, if the charge went through an authorize and settle flow, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :return: The authorized of this Charge.  # noqa: E501
        :rtype: datetime
        """
        return self._authorized

    @authorized.setter
    def authorized(self, authorized):
        """Sets the authorized of this Charge.

        When the charge was authorized, if the charge went through an authorize and settle flow, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :param authorized: The authorized of this Charge.  # noqa: E501
        :type: datetime
        """

        self._authorized = authorized

    @property
    def settled(self):
        """Gets the settled of this Charge.  # noqa: E501

        When the charge was settled, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :return: The settled of this Charge.  # noqa: E501
        :rtype: datetime
        """
        return self._settled

    @settled.setter
    def settled(self, settled):
        """Sets the settled of this Charge.

        When the charge was settled, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :param settled: The settled of this Charge.  # noqa: E501
        :type: datetime
        """

        self._settled = settled

    @property
    def cancelled(self):
        """Gets the cancelled of this Charge.  # noqa: E501

        When the charge was cancelled, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :return: The cancelled of this Charge.  # noqa: E501
        :rtype: datetime
        """
        return self._cancelled

    @cancelled.setter
    def cancelled(self, cancelled):
        """Sets the cancelled of this Charge.

        When the charge was cancelled, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :param cancelled: The cancelled of this Charge.  # noqa: E501
        :type: datetime
        """

        self._cancelled = cancelled

    @property
    def created(self):
        """Gets the created of this Charge.  # noqa: E501

        When the invoice was created, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :return: The created of this Charge.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Charge.

        When the invoice was created, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :param created: The created of this Charge.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def transaction(self):
        """Gets the transaction of this Charge.  # noqa: E501

        Transaction id assigned by Reepay. Assigned when transaction is performed.  # noqa: E501

        :return: The transaction of this Charge.  # noqa: E501
        :rtype: str
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this Charge.

        Transaction id assigned by Reepay. Assigned when transaction is performed.  # noqa: E501

        :param transaction: The transaction of this Charge.  # noqa: E501
        :type: str
        """

        self._transaction = transaction

    @property
    def error(self):
        """Gets the error of this Charge.  # noqa: E501

        Reepay error code if failed. See [transaction errors](https://reference.reepay.com/api/#transaction-errors).  # noqa: E501

        :return: The error of this Charge.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Charge.

        Reepay error code if failed. See [transaction errors](https://reference.reepay.com/api/#transaction-errors).  # noqa: E501

        :param error: The error of this Charge.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def source(self):
        """Gets the source of this Charge.  # noqa: E501

        Object describing the source for the charge. E.g. credit card.  # noqa: E501

        :return: The source of this Charge.  # noqa: E501
        :rtype: ChargeSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Charge.

        Object describing the source for the charge. E.g. credit card.  # noqa: E501

        :param source: The source of this Charge.  # noqa: E501
        :type: ChargeSource
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def order_lines(self):
        """Gets the order_lines of this Charge.  # noqa: E501

        Order lines for charge  # noqa: E501

        :return: The order_lines of this Charge.  # noqa: E501
        :rtype: list[OrderLine]
        """
        return self._order_lines

    @order_lines.setter
    def order_lines(self, order_lines):
        """Sets the order_lines of this Charge.

        Order lines for charge  # noqa: E501

        :param order_lines: The order_lines of this Charge.  # noqa: E501
        :type: list[OrderLine]
        """
        if order_lines is None:
            raise ValueError("Invalid value for `order_lines`, must not be `None`")  # noqa: E501

        self._order_lines = order_lines

    @property
    def refunded_amount(self):
        """Gets the refunded_amount of this Charge.  # noqa: E501

        Refunded amount  # noqa: E501

        :return: The refunded_amount of this Charge.  # noqa: E501
        :rtype: int
        """
        return self._refunded_amount

    @refunded_amount.setter
    def refunded_amount(self, refunded_amount):
        """Sets the refunded_amount of this Charge.

        Refunded amount  # noqa: E501

        :param refunded_amount: The refunded_amount of this Charge.  # noqa: E501
        :type: int
        """
        if refunded_amount is None:
            raise ValueError("Invalid value for `refunded_amount`, must not be `None`")  # noqa: E501

        self._refunded_amount = refunded_amount

    @property
    def authorized_amount(self):
        """Gets the authorized_amount of this Charge.  # noqa: E501

        Authorized amount if authorization was performed. The maximum amount that can be settled.  # noqa: E501

        :return: The authorized_amount of this Charge.  # noqa: E501
        :rtype: int
        """
        return self._authorized_amount

    @authorized_amount.setter
    def authorized_amount(self, authorized_amount):
        """Sets the authorized_amount of this Charge.

        Authorized amount if authorization was performed. The maximum amount that can be settled.  # noqa: E501

        :param authorized_amount: The authorized_amount of this Charge.  # noqa: E501
        :type: int
        """
        if authorized_amount is None:
            raise ValueError("Invalid value for `authorized_amount`, must not be `None`")  # noqa: E501

        self._authorized_amount = authorized_amount

    @property
    def error_state(self):
        """Gets the error_state of this Charge.  # noqa: E501

        Reepay error state if failed: `soft_declined`, `hard_declined` or `processing_error`. Soft and hard declines indicate a card decline. A soft decline is possibly recoverable and a subsequent request with the same card may succeed. E.g. insufficient funds. A processing error indicates an error processing the card either at Reepay, the acquirer, or between Reepay amd the acquirer.  # noqa: E501

        :return: The error_state of this Charge.  # noqa: E501
        :rtype: str
        """
        return self._error_state

    @error_state.setter
    def error_state(self, error_state):
        """Sets the error_state of this Charge.

        Reepay error state if failed: `soft_declined`, `hard_declined` or `processing_error`. Soft and hard declines indicate a card decline. A soft decline is possibly recoverable and a subsequent request with the same card may succeed. E.g. insufficient funds. A processing error indicates an error processing the card either at Reepay, the acquirer, or between Reepay amd the acquirer.  # noqa: E501

        :param error_state: The error_state of this Charge.  # noqa: E501
        :type: str
        """
        allowed_values = ["soft_declined", "hard_declined", "processing_error"]  # noqa: E501
        if error_state not in allowed_values:
            raise ValueError(
                "Invalid value for `error_state` ({0}), must be one of {1}"  # noqa: E501
                .format(error_state, allowed_values)
            )

        self._error_state = error_state

    @property
    def recurring_payment_method(self):
        """Gets the recurring_payment_method of this Charge.  # noqa: E501

        Optional reference to recurring payment method created in conjunction with charging  # noqa: E501

        :return: The recurring_payment_method of this Charge.  # noqa: E501
        :rtype: str
        """
        return self._recurring_payment_method

    @recurring_payment_method.setter
    def recurring_payment_method(self, recurring_payment_method):
        """Sets the recurring_payment_method of this Charge.

        Optional reference to recurring payment method created in conjunction with charging  # noqa: E501

        :param recurring_payment_method: The recurring_payment_method of this Charge.  # noqa: E501
        :type: str
        """

        self._recurring_payment_method = recurring_payment_method

    @property
    def billing_address(self):
        """Gets the billing_address of this Charge.  # noqa: E501

        Optional billing address  # noqa: E501

        :return: The billing_address of this Charge.  # noqa: E501
        :rtype: InvoiceBillingAddress
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this Charge.

        Optional billing address  # noqa: E501

        :param billing_address: The billing_address of this Charge.  # noqa: E501
        :type: InvoiceBillingAddress
        """

        self._billing_address = billing_address

    @property
    def shipping_address(self):
        """Gets the shipping_address of this Charge.  # noqa: E501

        Optional shipping address  # noqa: E501

        :return: The shipping_address of this Charge.  # noqa: E501
        :rtype: InvoiceShippingAddress
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this Charge.

        Optional shipping address  # noqa: E501

        :param shipping_address: The shipping_address of this Charge.  # noqa: E501
        :type: InvoiceShippingAddress
        """

        self._shipping_address = shipping_address

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
        if issubclass(Charge, dict):
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
        return self.__dict__ == other.__dict__ if isinstance(other, Charge) else False

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
