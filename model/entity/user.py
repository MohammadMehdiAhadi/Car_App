import re
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship

from model.entity import *


class User(Base):
    __tablename__ = "user_tbl"
    _id = Column("id", Integer, primary_key=True)
    _name = Column("name", String(30))
    _family = Column("family", String(30))
    _gender = Column("gender", String(8))
    _birth_date = Column("birth_date", Date)
    _email = Column("email", String(30))
    _city = Column("city", String(30))
    _address = Column("address", String(30))
    _phone = Column("phone", String(30))
    _username = Column("username", String(30), nullable=False)
    _password = Column("password", String(30), nullable=False)
    _status = Column("status", Boolean)
    _user_id = Column("user_id", String(10), nullable=False)
    _image = Column("image", String(100))

    def __init__(self, name, family, gender, birth_date, email, city, address, phone, username, password, status, user_id,image):
        self.name = name
        self.family = family
        self.gender = gender
        self.birth_date = birth_date
        self.email = email
        self.city = city
        self.address = address
        self.phone = phone
        self.username = username
        self.password = password
        self.status = status
        self.user_id = user_id
        self.image = image

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        self._birth_date = birth_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and re.match("^[a-zA-Z\s]{1,30}$", name, re.I):
            self._name = name
        else:
            raise ValueError("Invalid name")

    # props
    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        if isinstance(family, str) and re.match("[a-zA-Z\s]{1,30}", family,re.I):
            self._family = family
        else:
            raise ValueError("Invalid family")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if isinstance(gender, str) and gender in ("Male", "Female"):
            self._gender = gender
        else:
            raise ValueError("Invalid gender")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if isinstance(email, str) and re.match("^[\w\.]{1,50}@(gmail|yahoo|msn)\.com$", email, re.I):
            self._email = email
        else:
            raise ValueError("Invalid email")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if isinstance(city, str) and re.match("^[a-zA-Z\s]{1,30}$",city,re.I):
            self._city = city
        else:
            raise ValueError("Invalid city")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if isinstance(address, str) and re.match("^[\w\s\.\+\-\/\,]{1,100}$", address, re.I):
            self._address = address
        else:
            raise ValueError("Invalid address")

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):

        self._phone = phone

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and re.match("\w+$", username):
            self._username = username
        else:
            raise ValueError("Invalid username")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        # if isinstance(password, str) and re.match("(^[A-Z]{1,}[a-z]{1,}[\d]{1,}[@$!%?&*]{1,}$){8,}", password):
        if isinstance(password, str) and re.match("^\w+$", password):
            self._password = password
        else:
            raise ValueError("Invalid password")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, bool):
            self._status = status
        else:
            raise ValueError("Invalid status")

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if isinstance(user_id, str) and re.match("^\d{3}-?\d{6}-?\d{1}$", user_id, re.I):
            self._user_id = user_id
        else:
            raise ValueError("Invalid user_id")

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image