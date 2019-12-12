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


class CreateSubscription(object):
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
        'quantity': 'int',
        'discounts': 'list[CreateSubscriptionDiscount]',
        'add_ons': 'list[CreateSubscriptionAddOn]',
        'additional_costs': 'list[CreateSubscriptionAdditionalCost]',
        'amount_incl_vat': 'bool',
        'grace_duration': 'int',
        'no_trial': 'bool',
        'no_setup_fee': 'bool',
        'conditional_create': 'bool'
    }

    attribute_map = {
        'amount': 'amount',
        'quantity': 'quantity',
        'discounts': 'discounts',
        'add_ons': 'add_ons',
        'additional_costs': 'additional_costs',
        'amount_incl_vat': 'amount_incl_vat',
        'grace_duration': 'grace_duration',
        'no_trial': 'no_trial',
        'no_setup_fee': 'no_setup_fee',
        'conditional_create': 'conditional_create'
    }

    def __init__(self, amount=None, quantity=None, discounts=None, add_ons=None, additional_costs=None, amount_incl_vat=None, grace_duration=None, no_trial=None, no_setup_fee=None, conditional_create=None):  # noqa: E501
        """CreateSubscription - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._quantity = None
        self._discounts = None
        self._add_ons = None
        self._additional_costs = None
        self._amount_incl_vat = None
        self._grace_duration = None
        self._no_trial = None
        self._no_setup_fee = None
        self._conditional_create = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if quantity is not None:
            self.quantity = quantity
        if discounts is not None:
            self.discounts = discounts
        if add_ons is not None:
            self.add_ons = add_ons
        if additional_costs is not None:
            self.additional_costs = additional_costs
        if amount_incl_vat is not None:
            self.amount_incl_vat = amount_incl_vat
        if grace_duration is not None:
            self.grace_duration = grace_duration
        if no_trial is not None:
            self.no_trial = no_trial
        if no_setup_fee is not None:
            self.no_setup_fee = no_setup_fee
        if conditional_create is not None:
            self.conditional_create = conditional_create

    @property
    def amount(self):
        """Gets the amount of this CreateSubscription.  # noqa: E501

        Optional custom per quantity plan price. If provided the plan price billed for each billing period will be overridden by this price.  # noqa: E501

        :return: The amount of this CreateSubscription.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreateSubscription.

        Optional custom per quantity plan price. If provided the plan price billed for each billing period will be overridden by this price.  # noqa: E501

        :param amount: The amount of this CreateSubscription.  # noqa: E501
        :type: int
        """
        if amount is not None and amount < 0:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `0`")  # noqa: E501

        self._amount = amount

    @property
    def quantity(self):
        """Gets the quantity of this CreateSubscription.  # noqa: E501

        Optional quantity of the plan product for this subscription. If not provided the default is the default plan quantity defined for the plan.  # noqa: E501

        :return: The quantity of this CreateSubscription.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CreateSubscription.

        Optional quantity of the plan product for this subscription. If not provided the default is the default plan quantity defined for the plan.  # noqa: E501

        :param quantity: The quantity of this CreateSubscription.  # noqa: E501
        :type: int
        """
        if quantity is not None and quantity < 1:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `1`")  # noqa: E501

        self._quantity = quantity

    @property
    def discounts(self):
        """Gets the discounts of this CreateSubscription.  # noqa: E501

        Discounts to attach to subscription  # noqa: E501

        :return: The discounts of this CreateSubscription.  # noqa: E501
        :rtype: list[CreateSubscriptionDiscount]
        """
        return self._discounts

    @discounts.setter
    def discounts(self, discounts):
        """Sets the discounts of this CreateSubscription.

        Discounts to attach to subscription  # noqa: E501

        :param discounts: The discounts of this CreateSubscription.  # noqa: E501
        :type: list[CreateSubscriptionDiscount]
        """

        self._discounts = discounts

    @property
    def add_ons(self):
        """Gets the add_ons of this CreateSubscription.  # noqa: E501

        Add-ons to attach to subscription. The same add-on can only be attached to subscription once unless unique handles are supplied for the subscription add-on.  # noqa: E501

        :return: The add_ons of this CreateSubscription.  # noqa: E501
        :rtype: list[CreateSubscriptionAddOn]
        """
        return self._add_ons

    @add_ons.setter
    def add_ons(self, add_ons):
        """Sets the add_ons of this CreateSubscription.

        Add-ons to attach to subscription. The same add-on can only be attached to subscription once unless unique handles are supplied for the subscription add-on.  # noqa: E501

        :param add_ons: The add_ons of this CreateSubscription.  # noqa: E501
        :type: list[CreateSubscriptionAddOn]
        """

        self._add_ons = add_ons

    @property
    def additional_costs(self):
        """Gets the additional_costs of this CreateSubscription.  # noqa: E501

        Additional costs to add to subscription at creation time  # noqa: E501

        :return: The additional_costs of this CreateSubscription.  # noqa: E501
        :rtype: list[CreateSubscriptionAdditionalCost]
        """
        return self._additional_costs

    @additional_costs.setter
    def additional_costs(self, additional_costs):
        """Sets the additional_costs of this CreateSubscription.

        Additional costs to add to subscription at creation time  # noqa: E501

        :param additional_costs: The additional_costs of this CreateSubscription.  # noqa: E501
        :type: list[CreateSubscriptionAdditionalCost]
        """

        self._additional_costs = additional_costs

    @property
    def amount_incl_vat(self):
        """Gets the amount_incl_vat of this CreateSubscription.  # noqa: E501

        Whether the optional amount is including VAT. Defaults to true.  # noqa: E501

        :return: The amount_incl_vat of this CreateSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._amount_incl_vat

    @amount_incl_vat.setter
    def amount_incl_vat(self, amount_incl_vat):
        """Sets the amount_incl_vat of this CreateSubscription.

        Whether the optional amount is including VAT. Defaults to true.  # noqa: E501

        :param amount_incl_vat: The amount_incl_vat of this CreateSubscription.  # noqa: E501
        :type: bool
        """

        self._amount_incl_vat = amount_incl_vat

    @property
    def grace_duration(self):
        """Gets the grace_duration of this CreateSubscription.  # noqa: E501

        A grace duration in seconds from the creation of a subscription where no dunning process is started for a failing invoice. This allows a certain amount of time for the customer to sign up with a payment method.  # noqa: E501

        :return: The grace_duration of this CreateSubscription.  # noqa: E501
        :rtype: int
        """
        return self._grace_duration

    @grace_duration.setter
    def grace_duration(self, grace_duration):
        """Sets the grace_duration of this CreateSubscription.

        A grace duration in seconds from the creation of a subscription where no dunning process is started for a failing invoice. This allows a certain amount of time for the customer to sign up with a payment method.  # noqa: E501

        :param grace_duration: The grace_duration of this CreateSubscription.  # noqa: E501
        :type: int
        """
        if grace_duration is not None and grace_duration < 0:  # noqa: E501
            raise ValueError("Invalid value for `grace_duration`, must be a value greater than or equal to `0`")  # noqa: E501

        self._grace_duration = grace_duration

    @property
    def no_trial(self):
        """Gets the no_trial of this CreateSubscription.  # noqa: E501

        Override plan trial settings and disable trial  # noqa: E501

        :return: The no_trial of this CreateSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._no_trial

    @no_trial.setter
    def no_trial(self, no_trial):
        """Sets the no_trial of this CreateSubscription.

        Override plan trial settings and disable trial  # noqa: E501

        :param no_trial: The no_trial of this CreateSubscription.  # noqa: E501
        :type: bool
        """

        self._no_trial = no_trial

    @property
    def no_setup_fee(self):
        """Gets the no_setup_fee of this CreateSubscription.  # noqa: E501

        Override plan setup fee settings and disable fee  # noqa: E501

        :return: The no_setup_fee of this CreateSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._no_setup_fee

    @no_setup_fee.setter
    def no_setup_fee(self, no_setup_fee):
        """Sets the no_setup_fee of this CreateSubscription.

        Override plan setup fee settings and disable fee  # noqa: E501

        :param no_setup_fee: The no_setup_fee of this CreateSubscription.  # noqa: E501
        :type: bool
        """

        self._no_setup_fee = no_setup_fee

    @property
    def conditional_create(self):
        """Gets the conditional_create of this CreateSubscription.  # noqa: E501

        If the subscription is eligible to bill for the first period right away, this option will make the creation conditional on a successful payment of the first invoice. Default is false.  # noqa: E501

        :return: The conditional_create of this CreateSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._conditional_create

    @conditional_create.setter
    def conditional_create(self, conditional_create):
        """Sets the conditional_create of this CreateSubscription.

        If the subscription is eligible to bill for the first period right away, this option will make the creation conditional on a successful payment of the first invoice. Default is false.  # noqa: E501

        :param conditional_create: The conditional_create of this CreateSubscription.  # noqa: E501
        :type: bool
        """

        self._conditional_create = conditional_create

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
        if issubclass(CreateSubscription, dict):
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
        if not isinstance(other, CreateSubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other