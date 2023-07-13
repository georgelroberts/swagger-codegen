# coding: utf-8

"""
    Swagger Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from petstore_api.configuration import Configuration


class User(object):
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
        'id': 'int',
        'username': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'password': 'str',
        'phone': 'str',
        'user_status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email',
        'password': 'password',
        'phone': 'phone',
        'user_status': 'userStatus'
    }

    def __init__(self, id=None, username=None, first_name=None, last_name=None, email=None, password=None, phone=None, user_status=None, _configuration=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._username = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._password = None
        self._phone = None
        self._user_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password
        if phone is not None:
            self.phone = phone
        if user_status is not None:
            self.user_status = user_status

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this User.  # noqa: E501


        :return: The username of this User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.


        :param username: The username of this User.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501


        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.


        :param first_name: The first_name of this User.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501


        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.


        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501


        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.


        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def password(self):
        """Gets the password of this User.  # noqa: E501


        :return: The password of this User.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this User.


        :param password: The password of this User.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def phone(self):
        """Gets the phone of this User.  # noqa: E501


        :return: The phone of this User.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this User.


        :param phone: The phone of this User.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def user_status(self):
        """Gets the user_status of this User.  # noqa: E501

        User Status  # noqa: E501

        :return: The user_status of this User.  # noqa: E501
        :rtype: int
        """
        return self._user_status

    @user_status.setter
    def user_status(self, user_status):
        """Sets the user_status of this User.

        User Status  # noqa: E501

        :param user_status: The user_status of this User.  # noqa: E501
        :type: int
        """

        self._user_status = user_status

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
        if issubclass(User, dict):
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
        return self.to_dict() == other.to_dict() if isinstance(other, User) else False

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return self.to_dict() != other.to_dict() if isinstance(other, User) else True
