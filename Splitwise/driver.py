#author: raghava mahanthi
#badblood8


import sys
sys.path.append('C:/Users/DELL/Desktop/Machine_Coding')

from Splitwise.controllers.user_controller import UserController
from Splitwise.controllers.group_controller import GroupController
from Splitwise.controllers.bill_controller import BillController

from Splitwise.services.bill_service import BillService
from Splitwise.services.group_service import GroupService
from Splitwise.services.user_service import UserService

userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())

user1 = userController.addUser('user1','raghava')
user2 = userController.addUser('user2','pavani')
user3 = userController.addUser('user3','vijay')
user4 = userController.addUser('user4','kumari')
user5 = userController.addUser('user5','Narsing')

members = [user1,user2,user3,user4,user5]

group1 = groupController.addGroup('group1','Mahanthi',members)

paidBy = {'user1': 100 , 'user2': 200, 'user3': 300, 'user4': 400,'user1': 500}

contribution = {'user1': 500 , 'user2': 400, 'user3': 200, 'user4': 300,'user1': 100}

bill1 = billController.addBill('bill1','group1',1500,contribution,paidBy)

balance1 = billController.getBalance('user1')
balance2 = billController.getBalance('user2')
print(balance1,balance2)
