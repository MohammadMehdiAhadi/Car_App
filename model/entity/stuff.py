import re

from sqlalchemy.orm import relationship

from model.entity import *
from sqlalchemy import Column, Integer, String, Boolean, Date


class Stuff(Base):
    __tablename__ = "stuff_tbl"

    _id = Column("id", Integer, primary_key=True)
    _car_name = Column("name", String(30))
    _color = Column("color", String(20))
    _brand = Column("brand", String(30))
    _year = Column("year", Date)
    _price = Column("price", Integer)
    _information = Column("information", String(200))
    _car_image = Column("car_image" , String(100))
    _status = Column("status", Boolean)

    def __init__(self, car_name, color, brand, year, price, information,car_image, status):
        self.car_name = car_name
        self.color = color
        self.brand = brand
        self.year = year
        self.price = price
        self.information = information
        self._car_image = car_image
        self.status = status

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def car_name(self):
        return self._car_name

    @car_name.setter
    def car_name(self, car_name):
        self._car_name = car_name

    # props
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str) and re.match("\w+$", brand):
            self._brand = brand
        else:
            raise ValueError("Invalid Brand")

    @property
    def information(self):
        return self._information

    @information.setter
    def information(self, information):
        if isinstance(information, str) and re.match("\w+$", information):
            self._information = information
        else:
            raise ValueError("Invalid information")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, bool):
            self._status = status
        else:
            raise ValueError("Invalid status")

    # @property
    # def deleted(self):
    #     return self._deleted
    #
    # @deleted.setter
    # def deleted(self, deleted):
        # if isinstance(deleted, bool):
        # self._deleted = deleted
        # else:
        #     raise ValueError("Invalid Deleted")

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
    def car_image(self):
        return self._car_image

    @car_image.setter
    def car_image(self, car_image):
        self._car_image = car_image
