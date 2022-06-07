# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import six

from addonpayments.utils import ValidateUtils as Validate


class HppValidator(object):
    """
    Attrs validator for fields used in HPP request object.
    A HPP validator is simply a callable that takes three arguments:
        * The instance that’s being validate
        * The attribute that it’s validating, and finally
        * The value that is passed for it.
    If the validations of the fields fail, the ValueError exception is throw
    """

    @staticmethod
    def country(instance, attribute, value):
        """
        Validator for currency attribute:
            * Type: Optional
            * Format: a-zA-Z0-9“”,.-|
            * Length: 3
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 50)
        Validate.validate_regex(attribute.name, value, r'^[a-zA-Z0-9“”,.\-/|]*$', 'alphanumeric and “”,.-')

    @staticmethod
    def comment(instance, attribute, value):
        """
        Validator for comment attribute:
            * Type:     Optional
            * Format:   a-zA-Z0-9 '",+“”.-_&\/@!?%()*:£$&€#[]|=
                        ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷ø¤ùúûüýþÿŒŽšœžŸ¥
            * Length:   0-255
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 255)
        Validate.validate_regex(
            attribute.name,
            value,
            r'^[a-zA-Z0-9 \'\",\+“”.\_\-&\\/@!?%()\*\:£$&€#\[\]|=\;'
            r'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷ø¤ùúûüýþÿŒŽšœžŸ¥]*$',
            'alphanumeric and \'",+“”.-_&\\/@!?%()*:£$&€#[]|='
            'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷ø¤ùúûüýþÿŒŽšœžŸ¥ and spaces'
        )

    @staticmethod
    def additional_info(instance, attribute, value):
        """
        Validator for additional_info attribute:
            * Type: Optional
            * Format: a-zA-Z0-9 “”.-_,+@
            * Length: 0-50
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 50)
        Validate.validate_regex(
            attribute.name, value, r'^[a-zA-Z0-9 “”.\-\_,+@]*$', 'alphanumeric and “”.-_,+@ and spaces'
        )

    @staticmethod
    def lang(instance, attribute, value):
        """
        Validator for lang attribute:
            * Type: Optional
            * Format: a-zA-Z
            * Length: 2
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length(attribute.name, value, 2)
        Validate.validate_regex(attribute.name, value, r'^[a-zA-Z]+$', 'alphanumeric')

    @staticmethod
    def url(instance, attribute, value):
        """
        Validator for url attribute:
            * Type: Optional
            * Format: a-zA-Z0-9',+.-_&\/?%:$&#=
            * Length: 0-255
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 255)
        Validate.validate_regex(
            attribute.name, value, r'^[a-zA-Z0-9\',+.\-\_&\\/?%:$&#=]*$', 'alphanumeric and \',+.-_&\/?%:$&#='
        )

    @staticmethod
    def shipping_code(instance, attribute, value):
        """
        Validator for shipping_code attribute:
            * Type: Optional
            * Format: a-zA-Z0-9 “”,.-|
            * Length: 0-30
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 30)
        Validate.validate_regex(
            attribute.name,
            value,
            r'^[a-zA-Z0-9 “”,.\-/|]*$',
            'alphanumeric and “”,.-/| and spaces'
        )

    @staticmethod
    def billing_code(instance, attribute, value):
        """
        Validator for billing_code attribute:
            * Type: Optional
            * Format: a-zA-Z0-9 “”,.-|
            * Length: 0-60
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 60)
        Validate.validate_regex(
            attribute.name,
            value,
            r'^[a-zA-Z0-9 “”,.\-/|]*$',
            'alphanumeric and “”,.-/| and spaces'
        )

    @staticmethod
    def card_payment_button(instance, attribute, value):
        """
        Validator for card_payment_button attribute:
            * Type: Optional
            * Format: a-zA-Z0-9 “”,.-|
            * Length: 0-60
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 25)
        Validate.validate_regex(
            attribute.name,
            value,
            r'^[a-zA-Z0-9\'",+“”.\-\_&\\/@!?%()*:£$&€#[]|=]*$',
            'alphanumeric and \'",+“”.-_&\\/@!?%()*:£$&€#[]|= '
        )

    @staticmethod
    def supplementary_data(instance, attribute, value):
        """
        Validator for supplementary_data attribute (this field can be a dictionary or a string):
            * Type: Optional
            * Format: a-zA-Z0-9{}'",+“”.-_&\/@!?%()*:£$&€#[]|= and spaces
            * Length: 0-60
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        try:
            Validate.validate_dict(attribute.name, value)
            # If value is a dict, convert keys and values to string
            value = ''.join(['{0}{1}'.format(k, v) for k, v in six.iteritems(value)])
        except ValueError:
            Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, six.text_type(value), 0, 255)
        Validate.validate_regex(
            attribute.name,
            value,
            r'^[a-zA-Z0-9 {}\'",+“”.\-\_&\\/@!?%()*:£$&€#\[\]\|=]*$',
            'alphanumeric and \'",+“”.-_&\\/@!?%()*:£$&€#[]|= and spaces'
        )

    @staticmethod
    def payer_ref(instance, attribute, value):
        """
        Validator for payer_ref attribute
        (this field must be mandatory if card_storage_enable and payer_exist are True):
            * Type: Conditional
            * Format: A-Za-z0-9_-\\
            * Length: 0-50
        :param instance: object
        :param attribute:
        :param value:
        """
        if int(instance.card_storage_enable) == 1 and int(instance.payer_exist) == 1:
            if not value:
                raise ValueError(
                    "{} is mandatory because CARD_STORAGE_ENABLE and PAYER_EXIST are set to '1'".format(attribute.name)
                )
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 50)
        Validate.validate_regex(
            attribute.name,
            value,
            r'^[a-zA-Z0-9\-\_\.]*$',
            'alphanumeric and _-.'
        )

    @staticmethod
    def pmt_ref(instance, attribute, value):
        """
        Validator for pmt_ref attribute:
            * Type: Optional
            * Format: a-zA-Z0-9
            * Length: 0-30
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 30)
        Validate.validate_regex(attribute.name, value, r'^[a-zA-Z0-9\-\_\.]*$', 'alphanumeric and -_.')

    @staticmethod
    def hpp_customer_email(instance, attribute, value):
        """
        Validator hpp_customer_email:
            * Type: Optional
            * Format: a-zA-Z0-9 “”.-_,+@!#$%&'*+/=?^`{|}~-
            * Length: 0-254
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 254)
        Validate.validate_regex(
            attribute.name, value, r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", 'alphanumeric and “”.-_,+@!#$%&*+/=?^_`{|}~-'
        )

    @staticmethod
    def hpp_customer_phonenumber_mobile(instance, attribute, value):
        """
        Validator for hpp_customer_phonenumber_mobile:
            * Type: Optional
            * Format: 0-9 |
            * Length: 0-60
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 60)
        Validate.validate_regex(
            attribute.name,
            value,
            r'^[0-9 |]*$',
            'numeric and |'
        )

    @staticmethod
    def hpp_billing_street(instance, attribute, value):
        """
        Validator for hpp_billing_street attribute:
            * Type:     Optional
            * Format:   a-zA-Z0-9 '",+“”.-_&\/@!?%()*:£$&€#[]|=
                        ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷ø¤ùúûüýþÿŒŽšœžŸ¥
            * Length:   0-50
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 50)
        Validate.validate_regex(
            attribute.name,
            value,
            r'^[a-zA-Z0-9 \'\",\+“”.\_\-&\\/@!?%()\*\:£$&€#\[\]|=\;\w'
            r'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷ø¤ùúûüýþÿŒŽšœžŸ¥]*$',
            'alphanumeric and \'",+“”.-_&\\/@!?%()*:£$&€#[]|=\w'
            'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷ø¤ùúûüýþÿŒŽšœžŸ¥ and spaces'
        )

    @staticmethod
    def city(instance, attribute, value):
        """
        Validator for city attribute:
            * Type: Optional
            * Format: a-zA-Z0-9“”,.-|
            * Length: 0-40
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 40)
        Validate.validate_regex(attribute.name, value, r"^[a-zA-Z\u0080-\u024F]+(?:. |-| |')*([1-9a-zA-Z\u0080-\u024F]+(?:. |-| |'))*[a-zA-Z\u0080-\u024F]*$", 'alphanumeric and “”,.-\u0080-\u024F')

    @staticmethod
    def hpp_billing_postalcode(instance, attribute, value):
        """
        Validator for hpp_billing_postalcode attribute:
            * Type: Optional
            * Format: a-zA-Z0-9 “”,.-|
            * Length: 0-16
        :param instance: object
        :param attribute:
        :param value:
        """
        if not value:
            return
        Validate.validate_str(attribute.name, value)
        Validate.validate_length_range(attribute.name, value, 0, 16)
        Validate.validate_regex(
            attribute.name,
            value,
            r'^[a-zA-Z0-9 “”,.\-/|]*$',
            'alphanumeric and “”,.-/| and spaces'
        )