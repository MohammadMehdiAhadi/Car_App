import re
from model.da import *
from model.entity import *



class BuyController:
    @classmethod
    def save(cls, name, color, brand, year, city, car_id, seller_id, buyer_id, sell_date, buy_date, car_price,
             information, status):
        try:
            buy = Buy(name, color, brand, year, city, car_id, seller_id, buyer_id, sell_date, buy_date, car_price,
                      information, status)
            da = BuyDa()
            da.save(buy)
            return True, buy
        except Exception as e:
            # e.with_traceback()
            return False, str(e)

    @classmethod
    def edit(cls, id, name, color, brand, year, city, car_id, seller_id, buyer_id, sell_date, buy_date, car_price,
             information, status):
        try:
            buy = Buy(name, color, brand, year, city, car_id, seller_id, buyer_id, sell_date, buy_date, car_price,
                      information, status)
            buy.id = id
            da = BuyDa()
            da.edit(buy)
            return True, buy
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = BuyDa()
            da.remove(id)
            return True, id
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = BuyDa()
            return True, da.find_all(Buy)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = UserDa()
            result = da.find_by_id(User, id)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_seller_id(cls, seller_id):
        try:
            da = BuyDa()

            True, da.find_by_seller_id(seller_id)

        except Exception as e:
            False, str(e)

    @classmethod
    def find_by_buyer_id(cls, buyer_id):
        try:
            da = BuyDa()
            True, da.find_by_buyer_id(buyer_id)

        except Exception as e:
            False, str(e)

    @classmethod
    def find_by_car_id(cls, car_id):
        try:
            da = BuyDa()
            return True, da.find_by_car_id(car_id)

        except Exception as e:
            False, str(e)

    @classmethod
    def find_by_name(cls, name):
        try:
            da = BuyDa()
            result = da.find_by_name(name)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_brand(cls, brand):
        try:
            da = BuyDa()
            result = da.find_by_brand(brand)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    # def date_validator(start_date, end_date):
    #    re.match("^[2023/13/11,%s]" [start_date, end_date])
    @classmethod
    def find_by_sell_date_range(cls, start_date, end_date):
        try:

            if start_date and end_date > 0:
                return True, start_date(), end_date()
            else:
                return False, "invalid Date"
        except Exception as e:
            False, str(e)

    @classmethod
    def find_by_buy_date_range(cls, start_date, end_date):
        try:
            da = BuyDa()
            if start_date and end_date > 0:
                return True, start_date(), end_date()
            else:
                return False, "invalid Date"
        except Exception as e:
            False, str(e)

    @classmethod
    def car_price_validator(cls, price):
        return 1000 < price < 10000

    @classmethod
    def find_by_car_price_range(cls, start_price, end_price):
        try:
            da = BuyDa()
            if start_price and end_price > 0:
                return True, start_price(), end_price()
            else:
                return False, "Invalid Price"
        except Exception as e:
            False, str(e)

    @classmethod
    def valid_name(cls, text):
        return re.match('^[a-zA-Z\s]{500}$', text)

    @classmethod
    def find_by_information(cls, information):
        try:
            da = BuyDa()
            if cls.valid_name(information):
                return True, da.find_by_information(information)
            else:
                return False, 'invalid information'
        except Exception as e:
            False, str(e)

    @classmethod
    def find_by_status(cls, status):
        try:
            da = BuyDa()
            result = da.find_by_sell_status(status)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_year(cls, year):
        try:
            da = BuyDa()
            result = da.find_by_year(year)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_color(cls, color):
        try:
            da = BuyDa()
            result = da.find_by_color(color)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)
