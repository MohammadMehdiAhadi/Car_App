from sqlalchemy import between

from model.da import *
from model.entity import *


class RentDa(DatabaseManager):

    def find_by_id(self, id, Rent):
        self.make_engine()
        result = self.session.query(Rent).filter(Rent.id == id)
        self.session.close()
        return result

    def find_by_name(self, name):
        self.make_engine()
        result = self.session.query(Rent).filter(Rent._name == name)
        self.session.close()
        return result

    def find_by_brand(self, brand):
        self.make_engine()
        result = self.session.query(Rent).filter(Rent._brand == brand)
        self.session.close()
        return result

    def find_by_sender_id(self, sender_id):
        self.make_engine()
        result = self.session.query(Rent).filter(Rent._sender_id == sender_id)
        self.session.close()
        return result

    def find_by_renter_id(self, renter_id):
        self.make_engine()
        result = self.session.query(Rent).filter(Rent._renter_id == renter_id)
        self.session.close()
        return result

    def find_by_car_id(self, car_id):
        self.make_engine()
        result = self.session.query(Rent).filter(Rent._car_id == car_id)
        self.session.close()
        return result

    def find_by_rent_date_range(self, start_date, end_date):
        self.make_engine()
        result = self.session.query(Rent).filter(between(Rent._rent_date, start_date, end_date))
        self.session.close()
        return result

    def find_by_return_date_range(self, start_date, end_date):
        self.make_engine()
        result = self.session.query(Rent).filter(between(Rent._return_date, start_date, end_date))
        self.session.close()
        return result

    def find_by_rent_price_range(self, start_price, end_price):
        self.make_engine()
        result = self.session.query(Rent).filter(between(Rent._rent_price, start_price, end_price))
        self.session.close()
        return result

    def find_by_information(self, information):
        self.make_engine()
        result = self.session.query(Rent).filter(Rent._information == information)
        self.session.close()
        return result

    def find_by_rent_status(self, status):
        self.make_engine()
        result = self.session.query(Rent).filter(Rent._status == status)
        self.session.close()
        return result


    def find_by_year(self, year):
        self.make_engine()
        result = self.session.query(Rent).filter(Rent._year == year)
        self.session.close()
        return result

    def find_by_color(self, color):
        self.make_engine()
        result = self.session.query(Rent).filter(Stuff._color == color)
        self.session.close()
        return result

