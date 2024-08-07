import re
from model.da import *
from model.entity import *


class LessorController:
    @classmethod
    def save(cls,name, color, brand, year,city, car_id, renter_id, sender_id, rent_date, return_date, rent_price,
             information, status):
        try:
            lessor = Lessor(name, color, brand, year,city, car_id, renter_id, sender_id, rent_date, return_date, rent_price,
             information, status)
            da = DatabaseManager()
            da.save(lessor)
            return True, lessor
        except Exception as e:
            # e.with_traceback()
            return False, str(e)

    @classmethod
    def edit(cls, id, name, color, brand, year,city, car_id, renter_id, sender_id, rent_date, return_date, rent_price,
             information, status):
        try:
            lessor = Lessor(name, color, brand, year,city, car_id, renter_id, sender_id, rent_date, return_date, rent_price,
             information, status)

            lessor.id = id
            da = DatabaseManager()
            da.edit(lessor)
            return True, lessor
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = DatabaseManager()
            da.remove(id)
            return True, id
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = DatabaseManager()
            return True, da.find_all(Lessor)
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
    def find_by_sender_id(cls, sender_id):
        try:
            da = LessorDa()
            True, da.find_by_sender_id(sender_id)
        except Exception as e:
            False, str(e)



    @classmethod
    def find_by_renter_id(cls, renter_id):
        try:
            da = LessorDa()

            True, da.find_by_renter_id(renter_id)

        except Exception as e:
            False, str(e)


    @classmethod
    def find_by_car_id(cls, car_id):
        try:
            da = LessorDa()

            return True, da.find_by_car_id(car_id)

        except Exception as e:
            False, str(e)



    @classmethod
    def find_by_name(cls, name):
        try:
            da = LessorDa()
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
            da = LessorDa()
            result = da.find_by_brand(brand)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_rent_date_range(cls, start_date, end_date):
        try:

            if start_date and end_date > 0:
                return True, start_date(), end_date()
            else:
                return False, "invalid Date"
        except Exception as e:
            False, str(e)

    @classmethod
    def find_by_return_date_range(cls, start_date, end_date):
        try:

            if start_date and end_date > 0:
                return True, start_date(), end_date()
            else:
                return False, "invalid Date"
        except Exception as e:
            False, str(e)


    @classmethod
    def find_by_rent_price_range(cls, start_price, end_price):
        try:
            da = LessorDa()
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
            da = LessorDa()
            if cls.valid_name(information):
                return True, da.find_by_information(information)
            else:
                return False, 'invalid information'
        except Exception as e:
            False, str(e)

    @classmethod
    def find_by_status(cls, status):
        try:
            result = cls.find_by_status(status)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_year(cls, year):
        try:
            da = LessorDa()
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
            da = LessorDa()
            result = da.find_by_color(color)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)