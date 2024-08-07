# import re
#
# from sqlalchemy import Column, Integer, String
#
# from model.entity import *
#
#
# class UserContact(Base):
#     __tablename__ = "user_contact_tbl"
#     _id = Column("id", Integer, primary_key=True)
#     _email = Column("email", String(30), nullable=False)
#     _state = Column("state", String(30), nullable=False)
#     _city = Column("city", String(30), nullable=False)
#     _address = Column("address", String(30), nullable=False)
#     _phone = Column("phone", Integer, nullable=False)
#     _photo = Column("photo", String(30), nullable=True)
#
#     def __init__(self, email, state, city, address, phone, photo, contact_id):
#         self.email = email
#         self.state = state
#         self.city = city
#         self.address = address
#         self.phone = phone
#         self.photo = photo
#         self.contact_id = contact_id
#
#     @property
#     def id(self):
#         return self._id
#
#     @id.setter
#     def id(self, id):
#         self._id = id
#
#     @property
#     def email(self):
#         return self._email
#
#     @email.setter
#     def email(self, email):
#         if isinstance(email, str) and re.match("\w+$", email):
#             self._email = email
#         else:
#             raise ValueError("Invalid email")
#
#     @property
#     def state(self):
#         return self._state
#
#     @state.setter
#     def state(self, state):
#         if isinstance(state, str):
#             self._state = state
#         else:
#             raise ValueError("Invalid state")
#
#     @property
#     def city(self):
#         return self._city
#
#     @city.setter
#     def city(self, city):
#         if isinstance(city, str):
#             self._city = city
#         else:
#             raise ValueError("Invalid city")
#
#     @property
#     def address(self):
#         return self._address
#
#     @address.setter
#     def address(self, address):
#         if isinstance(address, str) and re.match("^\w+$", address):
#             self._address = address
#         else:
#             raise ValueError("Invalid address")
#
#     @property
#     def phone(self):
#         return self._phone
#
#     @phone.setter
#     def phone(self, phone):
#         # if isinstance(phone, str) and re.match(("^0-9\d{11}$"), phone):
#         self._phone = phone
#         # else:
#         #     raise ValueError("Invalid phone")
#
#     @property
#     def photo(self):
#         return self._photo
#
#     @photo.setter
#     def photo(self, photo):
#         if isinstance(photo, str):
#             self._photo = photo
#         else:
#             raise ValueError("Invalid photo")
