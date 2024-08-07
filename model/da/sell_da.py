from model.da import *
from model.entity import *

from sqlalchemy import between


class SellDa(DatabaseManager):
    def find_by_id(self, id, Sell):
        self.make_engine()
        result = self.session.query(Sell).filter(Sell.id == id)
        self.session.close()
        return result


    def find_by_name(self, name):
        self.make_engine()
        result = self.session.query(Sell).filter(Sell._name == name)
        self.session.close()
        return result

    def find_by_brand(self, brand):
        self.make_engine()
        result = self.session.query(Sell).filter(Sell._brand == brand)
        self.session.close()
        return result

    def find_by_seller_id(self, seller_id):
        self.make_engine()
        result = self.session.query(Sell).filter(Sell._seller_id == seller_id)
        self.session.close()
        return result

    def find_by_buyer_id(self, buyer_id):
        self.make_engine()
        result = self.session.query(Sell).filter(Sell._buyer_id == buyer_id)
        self.session.close()
        return result

    def find_by_car_id(self, car_id):
        self.make_engine()
        result = self.session.query(Sell).filter(Sell._car_id == car_id)
        self.session.close()
        return result

    def find_by_sell_date_range(self, start_date, end_date):
        self.make_engine()
        result = self.session.query(Sell).filter(between(Sell._sell_date, start_date, end_date))
        self.session.close()
        return result

    def find_by_buy_date_range(self, start_date, end_date):
        self.make_engine()
        result = self.session.query(Sell).filter(between(Sell._buy_date, start_date, end_date))
        self.session.close()
        return result

    def find_by_car_price_range(self, start_price, end_price):
        self.make_engine()
        result = self.session.query(Sell).filter(between(Sell._car_price, start_price, end_price))
        self.session.close()
        return result

    def find_by_information(self, information):
        self.make_engine()
        result = self.session.query(Sell).filter(Sell._information == information)
        self.session.close()
        return result

    def find_by_sell_status(self, status):
        self.make_engine()
        result = self.session.query(Sell).filter(Sell._status == status)
        self.session.close()
        return result

    def find_by_year(self, year):
        self.make_engine()
        result = self.session.query(Sell).filter(Sell._year == year)
        self.session.close()
        return result

    def find_by_color(self, color):
        self.make_engine()
        result = self.session.query(Sell).filter(Sell._color == color)
        self.session.close()
        return result

