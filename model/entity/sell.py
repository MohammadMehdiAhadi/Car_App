import re
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship

from model.entity import *


class Sell(Base):
    __tablename__ = "sell_tbl"

    _id = Column("id", Integer, primary_key=True)
    _name = Column("name", String(30))
    _color = Column("color", String(20))
    _brand = Column("brand", String(30))
    _year = Column("year", Date)
    _city = Column("city", String(30))
    _car_id = Column("stuff_id", Integer, ForeignKey("stuff_tbl.id"))
    _seller_id = Column("seller_id", Integer, ForeignKey("user_tbl.id"))
    _buyer_id = Column("buyer_id", Integer, ForeignKey("user_tbl.id"))
    _sell_date = Column("sell_date", Date)
    _buy_date = Column("buy_date", Date)
    _car_price = Column("car_price", Integer)
    _information = Column("information", String(255))
    _status = Column("status", Boolean)

    stuff = relationship("Sell")
    buyer = relationship("User", foreign_keys=[_buyer_id])
    seller = relationship("User", foreign_keys=[_seller_id])

    def __init__(self, name, color, brand, year, city, car_id, seller_id, buyer_id, sell_date, buy_date, car_price,
                 information, status):

        self.name = name
        self.color = color
        self.brand = brand
        self.year = year
        self.city = city
        self.car_id = car_id
        self.seller_id = seller_id
        self.buyer_id = buyer_id
        self.sell_date = sell_date
        self.buy_date = buy_date
        self.car_price = car_price
        self.information = information
        self.status = status

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, buyer):
        self._buyer = buyer

    @property
    def stuff(self):
        return self._stuff

    @stuff.setter
    def stuff(self, stuff):
        self._stuff = stuff

    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, seller):
        self._seller = seller

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
    def information(self):
        return self._information

    @information.setter
    def information(self, information):
        if isinstance(information, str) and re.match("\w+$", information):
            self._information = information
        else:
            raise ValueError("Invalid Information")

    @property
    def car_price(self):
        return self._car_price

    @car_price.setter
    def car_price(self, car_price):
        # if isinstance(car_price, str) and re.match("^[/d]{2,20}$", car_price):
        self._car_price = car_price
        # else:
        #     raise ValueError("Invalid Price")

    # @property
    # def sell_date(self):
    #     return self._sell_date
    #
    # @sell_date.setter
    # def sell_date(self, sell_date):
    #     if isinstance(sell_date, str) and re.match("^[/d]{2,20}$", sell_date):
    #         self._sell_date = sell_date
    #     else:
    #         raise ValueError("Invalid Date")
    #
    # @property
    # def buy_date(self):
    #     return self._buy_date
    #
    # @buy_date.setter
    # def buy_date(self, buy_date):
    #     if isinstance(buy_date, str) and re.match("^[/d]{2,20}$", buy_date):
    #         self._buy_date = buy_date
    #     else:
    #         raise ValueError("Invalid Date")
