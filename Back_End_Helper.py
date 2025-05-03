import Record_Helper


class Validate_Credentials:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.filePaths = [".//PRSLoginCredentials.json", ".//PRSPatientData.json"]

    def Get_Role_ID(self):
        userData = Record_Helper.Get_User_Record(self.username, self.password, self.filePaths[0], "Username", "Password")

        if (len(userData)==0):
            return False
        else:
            return userData[0]["Role_ID"]
        
    def Execute_Command(self):
        roleId = self.Get_Role_ID()

        return roleId

class Action_Mapping:
    def __init__(self, roleID):
        self.roleID = roleID
        self.filePaths = [".//PRSLoginCredentials.json", ".//PRSPatientData.json"]

    def Get_Action_Mapping(self):
        return Record_Helper.Get_Action_Mapping(self.roleID, self.filePaths[0], "RoleID")

    def Get_Action(self, actionID):
        return Record_Helper.Get_Action(actionID, self.filePaths[0], "ActionID")

    def Get_All_Actions(self, actionsMappingData):
        actionData = []

        for actionMappingData in actionsMappingData:
            actionData.append(self.Get_Action(actionMappingData["ActionID"]))

        return actionData
            
    def Execute_Command(self):
        actionsMappingData = self.Get_Action_Mapping()
        actionData = self.Get_All_Actions(actionsMappingData)
        

        return actionData

