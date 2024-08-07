from datetime import datetime
from controller.rent_controller import *
from model.entity import *

da = DatabaseManager()
da.make_engine()
print("hi")
# user = User("name","family","Male",datetime.now().date(),"email","state","city","address",23225,"username","password","user_id","role",True)
# da = UserDa()
# da.save(user)
# print(user)
#
# user = User("aaa","bbbb","Male",datetime.now().date(),"email","state","city","address",23225,"username","password","user_id","role",True)
# user.id = 1
# da.edit(user)
# print(user)
#
# print(da.remove_by_id(User,2))
#
# stuff1 = Stuff("name", "color", "brand", datetime.now().date(), "23f", 32000, "image", "rent_condition", 980000,
#                "description", True)
# stuff1.name = "stuff"
# da.save(stuff1)
# print(stuff1)

# buyer1 = User("name", "family", "Male", datetime.now().date(), "username", "password", "1234567890", True, None)
# buyer1.name = "buyer"
# da.save(buyer1)
#
# #
# # seller1 = User()
# # seller1.name = "seller"
# # da.save(seller1)
#
# # sell = Sell()
# # sell.buyer = buyer1
# # sell.seller = seller1
# # sell.stuff = stuff1
# # sell.car_price = 1000
# # da.save(sell)
#
# # rent = Rent()
# # rent.buyer = buyer1
# # rent.seller = seller1
# # rent.stuff = stuff1
# # rent.rent_price = 1000
# # da.save(rent)
# #
# # print(stuff1)
# # print(buyer1)
# # print(seller1)
# # print(rent)
# #
# # print(rent)
# # print(rent.seller)
# # print(rent.buyer)
# # print(rent.stuff)
