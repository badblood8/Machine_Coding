from Splitwise.services.group_service_interface import GroupServiceInterface
from Splitwise.models.group import Group

class GroupService(GroupServiceInterface):
    groupDetails = {}
    def addBill(self,id,name,members):
        group=Group()
        group.setId(id)
        group.setName(name)
        group.setMembers(members)
        self.__class__.groupDetails[id] = group
        return group
