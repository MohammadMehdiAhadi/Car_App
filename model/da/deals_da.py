# import mysql.connector
from sqlalchemy import and_

from model.da import *
from model.entity import *


class DealsDa(DatabaseManager):
    def find_by_name(self, name, search_type=None):
        match search_type:
            case "contain":
                name = "%" + name + "%"
            case "start":
                name = name + "%"
            case "end":
                name = "%" + name
        self.make_engine()
        return self.session.query(Deals).filter(Deals.name.like(name))

    def find_by_family(self, family, search_type=None):
        match search_type:
            case "contain":
                family = "%" + family + "%"
            case "start":
                family = family + "%"
            case "end":
                family = "%" + family
        self.make_engine()
        return self.session.query(Deals).filter(Deals.family.like(family))

    # def find_by_id(self, id, search_type=None):
    #     match search_type:
    #         case "contain":
    #             id = "%" + id + "%"
    #         case "start":
    #             id = id + "%"
    #         case "end":
    #             id = "%" + id
    #     self.make_engine()
    #     return self.session.query(Deals).filter(Deals.id.like(id))

    def find_by_gender(self, gender, search_type=None):
        match search_type:
            case "man":
                return self.session.query(Deals).filter(Deals.gender == "man")
            case "woman":
                return self.session.query(Deals).filter(Deals.gender == "woman")
        self.make_engine()
        return self.session.query(Deals).filter(Deals.gender.like(gender))

    def find_by_email(self, email, search_type=None):
        match search_type:
            case "contain":
                email = "%" + email + "%"
            case "start":
                email = email + "%"
            case "end":
                email = "%" + email
                self.make_engine()
        return self.session.query(Deals).filter(Deals.email.like(email))

    def find_by_city(self, city, search_type=None):
        match search_type:
            case "contain":
                city = "%" + city + "%"
            case "start":
                city = city + "%"
            case "end":
                city = "%" + city
                self.make_engine()
        return self.session.query(Deals).filter(Deals.city.like(city))

    def find_by_address(self, address, search_type=None):
        match search_type:
            case "contain":
                address = "%" + address + "%"
            case "start":
                address = address + "%"
            case "end":
                address = "%" + address
                self.make_engine()
        return self.session.query(Deals).filter(Deals.address.like(address))

    def find_by_phone(self, phone, search_type=None):
        match search_type:
            case "contain":
                phone = "%" + phone + "%"
            case "start":
                phone = phone + "%"
            case "end":
                phone = "%" + phone
                self.make_engine()
        return self.session.query(Deals).filter(Deals.phone.like(phone))

    def find_by_username_password(self, username, password):
        self.make_engine()
        result = self.session.query(Deals).filter(
            and_(Deals._username == username, Deals._password == password)).all()
        if result:
            return result[0]

    def find_by_username(self, username, search_type=None):
        match search_type:
            case "contain":
                username = "%" + username + "%"
            case "start":
                username = username + "%"
            case "end":
                username = "%" + username
        self.make_engine()
        return self.session.query(Deals).filter(Deals.username.like(username))

    def find_by_password(self, password, search_type=None):
        match search_type:
            case "contain":
                password = "%" + password + "%"
            case "start":
                password = password + "%"
            case "end":
                password = "%" + password
        self.make_engine()
        return self.session.query(Deals).filter(Deals.password.like(password))
    
    def find_by_user_id(self, user_id, search_type=None):
        match search_type:
            case "contain":
                user_id = "%" + user_id + "%"
            case "start":
                user_id = user_id + "%"
            case "end":
                user_id = "%" + user_id
        self.make_engine()
        return self.session.query(Deals).filter(Deals.user_id.like(user_id))


    
    def find_by_car_name(self, car_name):
        self.make_engine()
        result = self.session.query(Deals).filter(Deals._car_name == car_name)
        self.session.close()
        return result

    def find_by_brand(self, brand):
        self.make_engine()
        result = self.session.query(Deals).filter(Deals._brand == brand)
        self.session.close()
        return result

    def find_by_id(self, id, Deals):
        self.make_engine()
        result = self.session.query(Deals).filter(Deals._id == id)
        self.session.close()
        return result

    def find_by_information(self, information):
        self.make_engine()
        result = self.session.query(Deals).filter(Deals._information == information)
        self.session.close()
        return result

    def find_by_price(self, price):
        self.make_engine()
        result = self.session.query(Deals).filter(Deals._price == price)
        self.session.close()
        return result

    def find_by_year(self, year):
        self.make_engine()
        result = self.session.query(Deals).filter(Deals._year == year)
        self.session.close()
        return result
    
    def find_by_date(self, date):
        self.make_engine()
        result = self.session.query(Deals).filter(Deals._date == date)
        self.session.close()
        return result

    def find_by_color(self, color):
        self.make_engine()
        result = self.session.query(Deals).filter(Deals._color == color)
        self.session.close()
        return result

    def find_by_role(self, role, search_type=None):
        match search_type:
            case "renter":
                return self.session.query(Deals).filter(Deals.role == "renter")
            case "sender":
                return self.session.query(Deals).filter(Deals.role == "sender")
        self.make_engine()
        return self.session.query(Deals).filter(Deals.role.like(role))

    def find_by_status(self, status, search_type=None):
        match search_type:
            case "inactive":
                return self.session.query(Deals).filter(Deals.status == 1)
            case "active":
                return self.session.query(Deals).filter(Deals.status == 0)
        self.make_engine()
        return self.session.query(Deals).filter(Deals.status.like(status))
    

