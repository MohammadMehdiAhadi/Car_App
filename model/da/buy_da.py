from model.da import *
from model.entity import *

from sqlalchemy import between


class BuyDa(DatabaseManager):
    def find_by_id(self, id, Buy):
        self.make_engine()
        result = self.session.query(Buy).filter(Buy.id == id)
        self.session.close()
        return result


    def find_by_name(self, name):
        self.make_engine()
        result = self.session.query(Buy).filter(Buy._name == name)
        self.session.close()
        return result

    def find_by_brand(self, brand):
        self.make_engine()
        result = self.session.query(Buy).filter(Buy._brand == brand)
        self.session.close()
        return result

    def find_by_seller_id(self, seller_id):
        self.make_engine()
        result = self.session.query(Buy).filter(Buy._seller_id == seller_id)
        self.session.close()
        return result

    def find_by_buyer_id(self, buyer_id):
        self.make_engine()
        result = self.session.query(Buy).filter(Buy._buyer_id == buyer_id)
        self.session.close()
        return result

    def find_by_car_id(self, car_id):
        self.make_engine()
        result = self.session.query(Buy).filter(Buy._car_id == car_id)
        self.session.close()
        return result

    def find_by_sell_date_range(self, start_date, end_date):
        self.make_engine()
        result = self.session.query(Buy).filter(between(Buy._sell_date, start_date, end_date))
        self.session.close()
        return result

    def find_by_buy_date_range(self, start_date, end_date):
        self.make_engine()
        result = self.session.query(Buy).filter(between(Buy._buy_date, start_date, end_date))
        self.session.close()
        return result

    def find_by_car_price_range(self, start_price, end_price):
        self.make_engine()
        result = self.session.query(Buy).filter(between(Buy._car_price, start_price, end_price))
        self.session.close()
        return result

    def find_by_information(self, information):
        self.make_engine()
        result = self.session.query(Buy).filter(Buy._information == information)
        self.session.close()
        return result

    def find_by_sell_status(self, status):
        self.make_engine()
        result = self.session.query(Buy).filter(Buy._status == status)
        self.session.close()
        return result

    def find_by_year(self, year):
        self.make_engine()
        result = self.session.query(Buy).filter(Buy._year == year)
        self.session.close()
        return result

    def find_by_color(self, color):
        self.make_engine()
        result = self.session.query(Buy).filter(Buy._color == color)
        self.session.close()
        return result

