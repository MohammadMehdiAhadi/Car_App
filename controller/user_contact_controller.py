# from model.da import *
# from model.entity import *
#
# class UserContactController:
#     def save(cls,id, name, family, gender, age, username, password, email, role, state):
#         try:
#             user = User(None,id,  name, family, gender, age, username, password, email, role, state)
#             da = DatabaseManager()
#             da.save(user)
#             return True, user
#         except Exception as e:
#             return False, str(e)
#
#     def edit(cls, id, name, family, gender, age, username, password, email, role, state):
#         try:
#             user = User(None,id, name, family, gender, age, username, password, email, role, state)
#             da = DatabaseManager()
#             da.edit(user)
#             return True, user
#         except Exception as e:
#             return False, str(e)
#
#     def remove(cls, id):
#         try:
#             da = DatabaseManager()
#             da.remove(id)
#             return True, id
#         except Exception as e:
#             return False, str(e)
#
#     def find_all(cls,class_name):
#         try:
#             da = DatabaseManager()
#             return True, da.find_all(class_name)
#         except Exception as e:
#             return False, str(e)
#
#     def find_by_email(cls, email):
#         try:
#             da = UserContactDa()
#             result = da.find_by_email(email)
#             if result:
#                 return True, result
#             else:
#                 raise ValueError("No Content")
#         except Exception as e:
#             return False, str(e)
#
#     def find_by_state(cls, state):
#         try:
#             da = UserContactDa()
#             result = da.find_by_state(state)
#             if result:
#                 return True, result
#             else:
#                 raise ValueError("No Content")
#         except Exception as e:
#             return False, str(e)
#
#     def find_by_address(cls, address):
#         try:
#             da = UserContactDa()
#             result = da.find_by_address(address)
#             if result:
#                 return True, result
#             else:
#                 raise ValueError("No Content")
#         except Exception as e:
#             return False, str(e)
#
#     def find_by_phone(cls, phone):
#         try:
#             da = UserContactDa()
#             result = da.find_by_phone(phone)
#             if result:
#                 return True, result
#             else:
#                 raise ValueError("No Content")
#         except Exception as e:
#             return False, str(e)
#
#     def find_by_city(cls, city):
#         try:
#             da = UserContactDa()
#             result = da.find_by_city(city)
#             if result:
#                 return True, result
#             else:
#                 raise ValueError("No Content")
#         except Exception as e:
#             return False, str(e)