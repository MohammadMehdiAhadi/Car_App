from model.da import *
from model.entity import *


class StuffController:
    @classmethod
    def save(cls, car_name, color, brand, year, price, information,car_image, status):
        try:
            stuff = Stuff(car_name, color, brand, year, price, information,car_image, status)
            da = StuffDa()
            da.save(stuff)
            return True, stuff
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, car_name, color, brand, year, price, information,car_image, status):
        try:
            stuff = Stuff(car_name, color, brand, year, price, information,car_image, status)
            stuff.id = id
            da = StuffDa()
            da.edit(stuff)
            return True, stuff
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit_car_image(cls, stuff):
        try:
            da = DatabaseManager()
            da.edit(stuff)
            return True, stuff
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = StuffDa()
            da.remove(id)
            return True, id
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = StuffDa()
            return True, da.find_all(Stuff)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_car_name(cls, car_name):
        try:
            da = StuffDa()
            result = da.find_by_car_name(car_name)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_brand(cls, brand):
        try:
            da = StuffDa()
            result = da.find_by_brand(brand)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = UserDa()
            result = da.find_by_id(Stuff, id)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_information(cls, information):
        try:
            da = StuffDa()
            result = da.find_by_information(information)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_price(cls, price):
        try:
            da = StuffDa()
            result = da.find_by_price(price)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_year(cls, year):
        try:
            da = StuffDa()
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
            da = StuffDa()
            result = da.find_by_color(color)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)
