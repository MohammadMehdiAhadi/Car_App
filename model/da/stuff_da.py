# import mysql.connector

from model.da import *
from model.entity import *


class StuffDa(DatabaseManager):
    def find_by_car_name(self, car_name):
        self.make_engine()
        result = self.session.query(Stuff).filter(Stuff._car_name == car_name)
        self.session.close()
        return result

    def find_by_brand(self, brand):
        self.make_engine()
        result = self.session.query(Stuff).filter(Stuff._brand == brand)
        self.session.close()
        return result

    def find_by_id(self, id, Stuff):
        self.make_engine()
        result = self.session.query(Stuff).filter(Stuff._id == id)
        self.session.close()
        return result

    def find_by_information(self, information):
        self.make_engine()
        result = self.session.query(Stuff).filter(Stuff._information == information)
        self.session.close()
        return result

    def find_by_price(self, price):
        self.make_engine()
        result = self.session.query(Stuff).filter(Stuff._price == price)
        self.session.close()
        return result

    def find_by_year(self, year):
        self.make_engine()
        result = self.session.query(Stuff).filter(Stuff._year == year)
        self.session.close()
        return result

    def find_by_color(self, color):
        self.make_engine()
        result = self.session.query(Stuff).filter(Stuff._color == color)
        self.session.close()
        return result

    def find_by_status(self, status):
        self.make_engine()
        result = self.session.query(Stuff).filter(Stuff._status == status)
        self.session.close()
        return result
