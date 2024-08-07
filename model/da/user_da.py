import mysql.connector
from sqlalchemy import and_

from model.da import *
from model.entity import *


class UserDa(DatabaseManager):
    def find_by_name(self, name, search_type=None):
        match search_type:
            case "contain":
                name = "%" + name + "%"
            case "start":
                name = name + "%"
            case "end":
                name = "%" + name
        self.make_engine()
        return self.session.query(User).filter(User.name.like(name))

    def find_by_family(self, family, search_type=None):
        match search_type:
            case "contain":
                family = "%" + family + "%"
            case "start":
                family = family + "%"
            case "end":
                family = "%" + family
        self.make_engine()
        return self.session.query(User).filter(User.family.like(family))

    # def find_by_id(self, id, search_type=None):
    #     match search_type:
    #         case "contain":
    #             id = "%" + id + "%"
    #         case "start":
    #             id = id + "%"
    #         case "end":
    #             id = "%" + id
    #     self.make_engine()
    #     return self.session.query(User).filter(User.id.like(id))

    def find_by_gender(self, gender, search_type=None):
        match search_type:
            case "man":
                return self.session.query(User).filter(User.gender == "man")
            case "woman":
                return self.session.query(User).filter(User.gender == "woman")
        self.make_engine()
        return self.session.query(User).filter(User.gender.like(gender))

    def find_by_email(self, email, search_type=None):
        match search_type:
            case "contain":
                email = "%" + email + "%"
            case "start":
                email = email + "%"
            case "end":
                email = "%" + email
                self.make_engine()
        return self.session.query(User).filter(User.email.like(email))

    def find_by_city(self, city, search_type=None):
        match search_type:
            case "contain":
                city = "%" + city + "%"
            case "start":
                city = city + "%"
            case "end":
                city = "%" + city
                self.make_engine()
        return self.session.query(User).filter(User.city.like(city))

    def find_by_address(self, address, search_type=None):
        match search_type:
            case "contain":
                address = "%" + address + "%"
            case "start":
                address = address + "%"
            case "end":
                address = "%" + address
                self.make_engine()
        return self.session.query(User).filter(User.address.like(address))

    def find_by_phone(self, phone, search_type=None):
        match search_type:
            case "contain":
                phone = "%" + phone + "%"
            case "start":
                phone = phone + "%"
            case "end":
                phone = "%" + phone
                self.make_engine()
        return self.session.query(User).filter(User.phone.like(phone))

    def find_by_username_password(self, username, password):
        self.make_engine()
        result = self.session.query(User).filter(
            and_(User._username == username, User._password == password)).all()
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
        return self.session.query(User).filter(User.username.like(username))

    def find_by_password(self, password, search_type=None):
        match search_type:
            case "contain":
                password = "%" + password + "%"
            case "start":
                password = password + "%"
            case "end":
                password = "%" + password
        self.make_engine()
        return self.session.query(User).filter(User.password.like(password))

    def find_by_role(self, role, search_type=None):
        match search_type:
            case "renter":
                return self.session.query(User).filter(User.role == "renter")
            case "sender":
                return self.session.query(User).filter(User.role == "sender")
        self.make_engine()
        return self.session.query(User).filter(User.role.like(role))

    def find_by_status(self, status, search_type=None):
        match search_type:
            case "inactive":
                return self.session.query(User).filter(User.status == 1)
            case "active":
                return self.session.query(User).filter(User.status == 0)
        self.make_engine()
        return self.session.query(User).filter(User.status.like(status))

    def find_by_user_id(self, user_id, search_type=None):
        match search_type:
            case "contain":
                user_id = "%" + user_id + "%"
            case "start":
                user_id = user_id + "%"
            case "end":
                user_id = "%" + user_id
        self.make_engine()
        return self.session.query(User).filter(User.user_id.like(user_id))
