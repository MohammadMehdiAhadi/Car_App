from model.da import *
from model.entity import *


class DealsController:
    @classmethod
    def save(cls, name, family, gender, birth_date, email, city, address, phone, username, password,
             user_id, image, car_name, color, brand, year, price, information, car_image, role, date, status):
        try:
            deals = Deals(name, family, gender, birth_date, email, city, address, phone, username, password
                          , user_id, image, car_name, color, brand, year, price, information, car_image, role, date,
                          status)
            da = DatabaseManager()
            da.save(deals)
            return True, deals
        except Exception as e:
            e.with_traceback()
            return False, str(e)

    @classmethod
    def edit(cls, id, name, family, gender, birth_date, email, city, address, phone, username, password,
             user_id, image, car_name, color, brand, year, price, information, car_image, role, date, status):
        try:
            deals = Deals(name, family, gender, birth_date, email, city, address, phone, username, password,
                          user_id, image, car_name, color, brand, year, price, information, car_image, role, date,
                          status)
            deals.id = id
            da = DatabaseManager()
            da.edit(deals)
            return True, deals
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit_image(cls, deals):
        try:
            da = DatabaseManager()
            da.edit(deals)
            return True, deals
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit_car_image(cls, deals):
        try:
            da = DatabaseManager()
            da.edit(deals)
            return True, deals
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
            return True, da.find_all(Deals)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:

            da = DealsDa()
            result = da.find_by_id(User, id)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_name(cls, name):
        try:
            da = DealsDa()
            result = da.find_by_name(name)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_family(cls, family):
        try:
            da = DealsDa()
            result = da.find_by_family(family)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_gender(cls, gender):
        try:
            da = DealsDa()
            result = da.find_by_gender(gender)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_role(cls, role):
        try:
            da = DealsDa()
            result = da.find_by_role(role)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_email(cls, email):
        try:
            da = DealsDa()
            result = da.find_by_email(email)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_address(cls, address):
        try:
            da = DealsDa()
            result = da.find_by_address(address)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_phone(cls, phone):
        try:
            da = DealsDa()
            result = da.find_by_phone(phone)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_city(cls, city):
        try:
            da = DealsDa()
            result = da.find_by_city(city)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username(cls, username):
        try:
            da = DealsDa()
            result = da.find_by_username(username)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_user_password(cls, username, password):
        try:
            da = DealsDa()
            result = da.find_by_username_password(username, password)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_status(cls, status):
        try:
            da = DealsDa()
            result = da.find_by_status(status)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_user_id(cls, user_id):
        try:
            da = DealsDa()
            result = da.find_by_user_id(user_id)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_car_name(cls, car_name):
        try:
            da = DealsDa()
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
            da = DealsDa()
            result = da.find_by_brand(brand)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_information(cls, information):
        try:
            da = DealsDa()
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
            da = DealsDa()
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
            da = DealsDa()
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
            da = DealsDa()
            result = da.find_by_color(color)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)

    def login(cls, username, password):
        try:
            da = DealsDa()
            profile = da.find_by_username_password(username, password)
            if (profile):
                return True, profile
            else:
                raise ValueError("Wrong username/password")
        except Exception as e:
            return False, str(e)

    def logout(cls):
        exit()
