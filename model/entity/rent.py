import re
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship

from model.entity import *


class Rent(Base):
    __tablename__ = "rent_tbl"

    _id = Column("id", Integer, primary_key=True)
    _name = Column("name", String(30))
    _color = Column("color", String(20))
    _brand = Column("brand", String(30))
    _year = Column("year", Date)
    _city = Column("city" , String(30))
    _car_id = Column("stuff_id", Integer, ForeignKey("stuff_tbl.id"))
    _renter_id = Column("renter_id", Integer, ForeignKey("user_tbl.id"))
    _sender_id = Column("sender_id", Integer, ForeignKey("user_tbl.id"))
    _rent_date = Column("rent_date", Date)
    _return_date = Column("return_date", Date)
    _rent_price = Column("rent_price", Integer)
    _information = Column("information", String(255))
    _status = Column("status", Boolean)

    stuff = relationship("Rent")
    sender = relationship("User", foreign_keys=[_sender_id])
    renter = relationship("User", foreign_keys=[_renter_id])

    def __init__(self,name, color, brand, year,city, car_id, renter_id, sender_id, rent_date, return_date, rent_price,
             information, status):
        self.name = name
        self.color = color
        self.brand = brand
        self.year = year
        self.city = city
        self.car_id = car_id
        self.renter_id = renter_id
        self.sender_id = sender_id
        self.rent_date = rent_date
        self.return_date = return_date
        self.rent_price = rent_price
        self.information = information
        self.status = status

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def renter(self):
        return self._renter

    @renter.setter
    def renter(self, renter):
        self._renter = renter

    @property
    def stuff(self):
        return self._stuff

    @stuff.setter
    def stuff(self, stuff):
        self._stuff = stuff

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, sender):
        self._sender = sender


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and re.match("^[a-zA-Z\s]{2,30}$", name, re.I):
            self._name = name
        else:
            raise ValueError("Invalid name")


    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if isinstance(color, str) and re.match("\w+$", color):
            self._color = color
        else:
            raise ValueError("Color Not Found")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if isinstance(city, str) and re.match("^[a-zA-Z\s]{2,30}$", city, re.I):
            self._city = city
        else:
            raise ValueError("Invalid city")



    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str) and re.match("^[a-zA-Z\s]{2,30}$", brand, re.I):
            self._brand = brand
        else:
            raise ValueError("Invalid Brand")

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
    def rent_date(self):
        return self._rent_date

    @rent_date.setter
    def rent_date(self, rent_date):
        self._rent_date = rent_date

    @property
    def return_date(self):
        return self._return_date

    @return_date.setter
    def return_date(self, return_date):
        self._return_date = return_date

    @property
    def rent_price(self):
        return self._rent_price

    @rent_price.setter
    def rent_price(self, rent_price):
        # if isinstance(rent_price, str) and re.match("^[/d]{2,20}$", rent_price):
        self._rent_price = rent_price
        # else:
        #     raise ValueError("Invalid Price")

    # @property
    # def return_date(self):
    #     return self._return_date
    #
    # @return_date.setter
    # def return_date(self, return_date):
    #     if isinstance(return_date, str) and re.match("^[/d]{2,20}$", return_date):
    #         self._return_date = return_date
    #     else:
    #         raise ValueError("Invalid Date")

    @property
    def information(self):
        return self._information

    @information.setter
    def information(self, information):
        if isinstance(information, str) and re.match("\w+$", information):
            self._information = information
        else:
            raise ValueError("Invalid Information")
