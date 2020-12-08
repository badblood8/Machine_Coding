from Splitwise.services.user_service_interface import UserServiceInterface
from Splitwise.models.user import User

class UserService(UserServiceInterface):
    userDetails = {}
    def addBill(self,id,name):
        user=User()
        user.setId(id)
        user.setName(name)
        self.__class__.userDetails[id] = user
        return user
