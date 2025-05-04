import Record_Helper
import General_Helper
import File_Helper


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

class Add_Patient:
    def __init__(self, patientId):
        self.patientId = patientId
        self.filePaths = [".//PRSLoginCredentials.json", ".//PRSPatientData.json"]

    def Get_Patient_Record(self):
        return Record_Helper.Get_Patient_Record(self.patientId, self.filePaths[1], "Patient_ID")

    def Add_Record_To_File(self, jsonFile, patientData, visitData, noteData, mode):
        jsonObjects = File_Helper.Read_Json_Patient_File(jsonFile)#get data to append new record too
        #this logic makes sure that only the records captured are appended
        if (mode == None):
            jsonObjects[1].append(General_Helper.Generate_Patient_Data_Json(self.patientId, patientData))#append patientData
        if (mode == 1 or mode == None):
            jsonObjects[2].append(General_Helper.Generate_Visit_Data_Json(self.patientId, visitData))#append visitData
        if (mode == 2 or mode == None):
            jsonObjects[3].append(General_Helper.Generate_Note_Data_Json(self.patientId, noteData, visitData))#append noteData and needs visitData for Visit ID
            jsonObjects[4].append(General_Helper.Generate_Additional_Information_Note_Data_Json(self.patientId, visitData, noteData))
        File_Helper.Write_Json_File(jsonFile, jsonObjects[0])
        print("done")

    def Get_Most_Recent_Visit_Record(self, visitRecords):
        #get the most recent visit for patient
        mostRecentVisitDate = "1970-01-01"  #epoch date: earliest data that can be found for a record on computer
        recentRecord = []
        print("1")
        for visitRecord in visitRecords:
            print("2")
            if (visitRecord["Visit_time"] > mostRecentVisitDate):#checks if record Visit_time is newer then most recent visit date
                print("3")
                mostRecentVisitDate = visitRecord["Visit_time"]
                recentRecord.clear()#remove old record and replace with newer visit
                recentRecord.append(visitRecord)
                print("4")
        print("5")
        return recentRecord
    
    def Get_Most_Recent_Visit_ID(self):
        visitRecords = Record_Helper.Get_Patient_Visit_Records(self.patientId,  self.filePaths[1], "Patient_ID")#search PatientVisitRecord for Patient ID using json element name Patient_ID

        recentRecord = []
        print(visitRecords[0])
        if (len(visitRecords) != 1):#if only one record exists that record is the most recent record
            recentRecord = (self.Get_Most_Recent_Visit_Record(visitRecords)[0])
        else:
            recentRecord = visitRecords[0]
        #return list of record values
        return [recentRecord["Patient_ID"], recentRecord["Visit_ID"], recentRecord["Visit_time"], recentRecord["Visit_department"], recentRecord["ZipCode"]]

    def Create_Record(self):
        Add_Record_To_File(self.filePaths[1])
        
    def Create_Visit_Record(self, visitDepartment, zipCode):
        visitId = General_Helper.Generate_ID()
        visitTime = General_Helper.Generate_Visit_Time()
        visitData = [visitId, visitTime, visitDepartment, zipCode]
        self.Add_Record_To_File(self.filePaths[1], None, visitData, None, 1)

    def Create_Note_Record(self, chiefComplaint, additionalInfo, noteType):
        noteId = General_Helper.Generate_ID()
        visitData = self.Get_Most_Recent_Visit_ID()#get most recent visit to link note data too
        noteData = [noteId, chiefComplaint, additionalInfo, noteType]
        self.Add_Record_To_File(self.filePaths[1], None, visitData, noteData, 2)
        

