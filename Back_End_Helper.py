import Record_Helper
import General_Helper
import File_Helper
from datetime import datetime
import CSV_To_JSON_Converter

class Log_Usage_Record:
    def __init__(self):
        self.jsonFilePaths = [".//PRSLoginCredentials.json", ".//PRSPatientData.json", ".//PRSUsageStatistics.json"]
        self.csvFilePaths = [".//PA3_Notes.csv", ".//PA3_data.csv", ".//PA3_credentials.csv" ]

    def Get_Role_Name(self, roleID):
        return Record_Helper.Get_User_Role(roleID, self.jsonFilePaths[0], "Role_ID")[0]["Role_Name"]

    def Get_Usage_Statistic_Data(self):
        return File_Helper.Read_Json_Usage_Statistic_File(self.jsonFilePaths[2])

    def Create_Login_Event(self, UserID, UserName, RoleID, Success):
        roleName = None
        if(RoleID != None):
            roleName = self.Get_Role_Name(RoleID)
        EventData = [UserID, UserName, roleName, Success]

        loginEventData = self.Get_Usage_Statistic_Data()
        loginEventData[1].append(General_Helper.Generate_Login_Events_Data_Json(EventData))
        File_Helper.Write_Json_File(self.jsonFilePaths[2], loginEventData[0])

    def Get_Login_Event_ID(self, UserID):
        return Record_Helper.Get_Login_Event(UserID, self.jsonFilePaths[2], "UserID")[-1]["EventID"]


    def Create_Preformed_Action_Record(self, UserID, ActionName):
        ActionData = []
        ActionData.append(self.Get_Login_Event_ID(UserID))
        ActionData.append(ActionName)

        actionPreformedData = self.Get_Usage_Statistic_Data()
        actionPreformedData[2].append(General_Helper.Generate_Actions_Preformed_Data_Json(ActionData))
        File_Helper.Write_Json_File(self.jsonFilePaths[2], actionPreformedData[0])
        
class Create_Json:
    def __init__(self):
        self.jsonFilePaths = [".//PRSLoginCredentials.json", ".//PRSPatientData.json", ".//PRSUsageStatistics.json"]
        self.csvFilePaths = [".//PA3_Notes.csv", ".//PA3_data.csv", ".//PA3_credentials.csv" ]

        
    def Check_For_Json_File(self):
        if(File_Helper.Check_For_Json_File(self.jsonFilePaths[1], None, True) == False):
           return CSV_To_JSON_Converter.Convert_CSV_To_JSON(self.csvFilePaths, self.jsonFilePaths)
        else:
            return True


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
            return userData[0]
        
    def Execute_Command(self):
        return self.Get_Role_ID()


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

    def Add_Record_To_File(self, jsonFile, patientData, visitData, noteData, additionalNoteData, mode):
        jsonObjects = File_Helper.Read_Json_Patient_File(jsonFile)#get data to append new record too
        #this logic makes sure that only the records captured are appended
        if (mode == None):
            jsonObjects[1].append(General_Helper.Generate_Patient_Data_Json(self.patientId, patientData))#append patientData
        if (mode == 1 or mode == None):
            jsonObjects[2].append(General_Helper.Generate_Visit_Data_Json(self.patientId, visitData))#append visitData
        if (mode == 2 or mode == None):
            jsonObjects[3].append(General_Helper.Generate_Note_Data_Json(self.patientId, noteData, visitData))#append noteData and needs visitData for Visit ID
            jsonObjects[4].append(General_Helper.Generate_Additional_Information_Note_Data_Json(self.patientId, visitData, additionalNoteData))
        File_Helper.Write_Json_File(jsonFile, jsonObjects[0])

    def Get_Most_Recent_Visit_Record(self, visitRecords):
        #get the most recent visit for patient
        mostRecentVisitDate = "01/01/1970"  #epoch date: earliest data that can be found for a record on computer
        dateFormat = "%m/%d/%Y"
        recentRecord = []
        for visitRecord in visitRecords:
            if (datetime.strptime(visitRecord["Visit_time"], dateFormat) > datetime.strptime(mostRecentVisitDate, dateFormat)):#checks if record Visit_time is newer then most recent visit date
                mostRecentVisitDate = visitRecord["Visit_time"]
                recentRecord.clear()#remove old record and replace with newer visit
                recentRecord.append(visitRecord)
        return recentRecord
    
    def Get_Most_Recent_Visit_ID(self):
        visitRecords = Record_Helper.Get_Patient_Visit_Records(self.patientId,  self.filePaths[1], "Patient_ID")#search PatientVisitRecord for Patient ID using json element name Patient_ID

        recentRecord = []
        if (len(visitRecords) > 1):#if only one record exists that record is the most recent record
            recentRecord = (self.Get_Most_Recent_Visit_Record(visitRecords)[0])
        else:
            recentRecord = visitRecords[0]
        #return list of record values
        return [recentRecord["Patient_ID"], recentRecord["Visit_ID"], recentRecord["Visit_time"], recentRecord["Visit_department"], recentRecord["ZipCode"]]

    def Create_Patient_Record(self, patientData, visitData, noteData, additionalNoteData):
        visitData.insert(0, None)
        visitData.insert(1, General_Helper.Generate_ID())
        visitData.insert(2, General_Helper.Generate_Visit_Time())
        noteData.insert(0, General_Helper.Generate_ID())
        additionalNoteData.insert(0, General_Helper.Generate_ID())
        self.Add_Record_To_File(self.filePaths[1], patientData, visitData, noteData, additionalNoteData, None)
        
    def Create_Visit_Record(self, visitDepartment, zipCode):
        visitId = General_Helper.Generate_ID()
        visitTime = General_Helper.Generate_Visit_Time()
        visitData = [None, visitId, visitTime, visitDepartment, zipCode]
        self.Add_Record_To_File(self.filePaths[1], None, visitData, None, None, 1)

    def Create_Note_Record(self, chiefComplaint, additionalInfo, noteType):
        noteId = General_Helper.Generate_ID()
        visitData = self.Get_Most_Recent_Visit_ID()#get most recent visit to link note data too
        noteData = [noteId, chiefComplaint, noteType]
        additionalNoteData = [noteId, additionalInfo]
        self.Add_Record_To_File(self.filePaths[1], None, visitData, noteData, additionalNoteData, 2)

class Remove_Patient:
    def __init__(self, patientId):
        self.patientId = patientId
        self.filePaths = [".//PRSLoginCredentials.json", ".//PRSPatientData.json"]

    def Get_Patient_Record(self):
        return Record_Helper.Get_Patient_Record(self.patientId, self.filePaths[1], "Patient_ID")
    
    def Remove_Patient_Records(self):
        jsonObjects = File_Helper.Read_Json_Patient_File(self.filePaths[1])
        jsonObjects[4] = Record_Helper.Remove_Additional_Information_Note_Data(self.patientId, jsonObjects[4], "Patient_ID")
        jsonObjects[3] = Record_Helper.Remove_Patient_Visit_Notes(self.patientId, jsonObjects[3], "Patient_ID")
        jsonObjects[2] = Record_Helper.Remove_Patient_Visit_Records(self.patientId, jsonObjects[2], "Patient_ID")
        jsonObjects[1] = Record_Helper.Remove_Patient_Record(self.patientId, jsonObjects[1], "Patient_ID")
        File_Helper.Write_Json_File(self.filePaths[1], jsonObjects[0])

class Retrieve_Patient:
    def __init__(self, patientId):
        self.patientId = patientId
        self.filePaths = [".//PRSLoginCredentials.json", ".//PRSPatientData.json"]    


    def Get_Patient_Record(self):
        return Record_Helper.Get_Patient_Record(self.patientId, self.filePaths[1], "Patient_ID")

class Count_Visits:
    def __init__(self, date):
        self.date = date
        self.filePaths = [".//PRSLoginCredentials.json", ".//PRSPatientData.json"]

    def Get_Visit_Records(self):
        return Record_Helper.Get_Patient_Visit_Records(self.date, self.filePaths[1], "Visit_time")#search PatientVisitRecord for Visit Time using json element name Visit_time

            
class View_Note:
    def __init__(self, patientId):
        self.patientId = patientId
        self.filePaths = [".//PRSLoginCredentials.json", ".//PRSPatientData.json"]

    def Get_Patient_Record(self):
        return Record_Helper.Get_Patient_Record(self.patientId, self.filePaths[1], "Patient_ID")

    def Get_Visit_ID(self, visitDate):
        visitRecords = Record_Helper.Get_Patient_Visit_Records(self.patientId, self.filePaths[1], "Patient_ID")
        visitId = False
        for visitRecord in visitRecords:
            if(visitRecord["Visit_time"] == visitDate):
                visitId = visitRecord["Visit_ID"]
        return visitId

    def Get_Patient_Notes(self, visitDate):
        visitId = self.Get_Visit_ID(visitDate)
        if(visitId == False):
            return False
        else:
            fullNoteData = []
            fullNoteData.append(Record_Helper.Get_Patient_Visit_Notes(visitId, self.filePaths[1], "Visit_ID")[-1])
            fullNoteData.append(Record_Helper.Get_Additional_Visit_Notes(visitId, self.filePaths[1], "Visit_ID")[-1])
        return fullNoteData

class Generate_Statistics:
    def __init__(self):
        self.filePaths = [".//PRSLoginCredentials.json", ".//PRSPatientData.json"]

    def Get_Patient_Records(self):
        return Record_Helper.Get_Patient_Record("Null", self.filePaths[1], "Patient_ID", True)

    def Get_Visit_Records(self, patientID):
        return Record_Helper.Get_Patient_Visit_Records(patientID,self.filePaths[1],"Patient_ID")


    def Get_Unique_List_Of_Gender(self, patientRecords):
        UniqueOfGender = []
        for patientRecord in patientRecords:
            if (patientRecord["Gender"] not in UniqueOfGender):
                UniqueOfGender.append(patientRecord["Gender"])
                
        return UniqueOfGender
    
    def Get_Unique_List_Of_Age(self, patientRecords):
        UniqueOfAge = []
        for patientRecord in patientRecords:
            if (patientRecord["Age"] not in UniqueOfAge):
                UniqueOfAge.append(patientRecord["Age"])
                
        return UniqueOfAge

    def Get_Unique_List_Of_Race(self, patientRecords):
        UniqueOfRace = []
        for patientRecord in patientRecords:
            if (patientRecord["Race"] not in UniqueOfRace):
                UniqueOfRace.append(patientRecord["Race"])
                
        return UniqueOfRace

    def Get_Unique_List_Of_Ethnicity(self, patientRecords):
        UniqueOfEthnicity = []
        for patientRecord in patientRecords:
            if (patientRecord["Ethnicity"] not in UniqueOfEthnicity):
                UniqueOfEthnicity.append(patientRecord["Ethnicity"])
                
        return UniqueOfEthnicity

    def Get_Unique_List_Of_Insurance(self, patientRecords):
        UniqueOfInsurance = []
        for patientRecord in patientRecords:
            if (patientRecord["Insurance"] not in UniqueOfInsurance):
                UniqueOfInsurance.append(patientRecord["Insurance"])
                
        return UniqueOfInsurance


    def Get_All_Unique_Lists(self, patientRecords):
        UniqueList = []
        UniqueList.append(self.Get_Unique_List_Of_Gender(patientRecords))
        UniqueList.append(self.Get_Unique_List_Of_Age(patientRecords))
        UniqueList.append(self.Get_Unique_List_Of_Race(patientRecords))
        UniqueList.append(self.Get_Unique_List_Of_Ethnicity(patientRecords))
        UniqueList.append(self.Get_Unique_List_Of_Insurance(patientRecords))

        return UniqueList
    
    def Count_Number_Of_Gender_Visits(self, UniqueListItems, patientRecords):
        listGenderCount = []
        for UniqueListItem in UniqueListItems:
            count = 0
            for patientRecord in patientRecords:
                if (patientRecord["Gender"]== UniqueListItem):
                    count = count + 1
            listGenderCount.append([UniqueListItem, count])

        return listGenderCount
    
    def Count_Number_Of_Age_Visits(self, UniqueListItems, patientRecords):
        listAgeCount = []
        ageClassifications = [[1,12],[13,19],[20,44],[45,64],[65,100]]
        ageNameClassifications = ["childhood 1 -> 12", "adolescence 13 -> 19", "young adulthood 20 -> 44", "middle adulthood 45 -> 64", "older adulthood 65+"]
        for ageNameClassification in ageNameClassifications:
            count = 0
            for UniqueListItem in UniqueListItems:
                if(int(UniqueListItem) >= ageClassifications[ageNameClassifications.index(ageNameClassification)][0] and int(UniqueListItem) <= ageClassifications[ageNameClassifications.index(ageNameClassification)][1]):
                    for patientRecord in patientRecords:
                        if (patientRecord["Age"]== UniqueListItem):
                            count = count + 1
            listAgeCount.append([ageNameClassification, count])

        return listAgeCount

    def Count_Number_Of_Race_Visits(self, UniqueListItems, patientRecords):
        listRaceCount = []
        for UniqueListItem in UniqueListItems:
            count = 0
            for patientRecord in patientRecords:
                if (patientRecord["Race"]== UniqueListItem):
                    count = count + 1
            listRaceCount.append([UniqueListItem, count])

        return listRaceCount

    def Count_Number_Of_Ethnicity_Visits(self, UniqueListItems, patientRecords):
        listEthnicityCount = []
        for UniqueListItem in UniqueListItems:
            count = 0
            for patientRecord in patientRecords:
                if (patientRecord["Ethnicity"]== UniqueListItem):
                    count = count + 1
            listEthnicityCount.append([UniqueListItem, count])

        return listEthnicityCount

    def Count_Number_Of_Insurance_Visits(self, UniqueListItems, patientRecords):
        listInsuranceCount = []
        for UniqueListItem in UniqueListItems:
            count = 0
            for patientRecord in patientRecords:
                if (patientRecord["Insurance"]== UniqueListItem):
                    count = count + 1
            listInsuranceCount.append([UniqueListItem, count])

        return listInsuranceCount


    def Count_All_Statisic_Attributes(self, uniqueListItems, patientRecords):
        countedListOfUniqueListItems = []
        countedListOfUniqueListItems.append(self.Count_Number_Of_Gender_Visits(uniqueListItems[0], patientRecords))
        countedListOfUniqueListItems.append(self.Count_Number_Of_Age_Visits(uniqueListItems[1], patientRecords))
        countedListOfUniqueListItems.append(self.Count_Number_Of_Race_Visits(uniqueListItems[2], patientRecords))
        countedListOfUniqueListItems.append(self.Count_Number_Of_Ethnicity_Visits(uniqueListItems[3], patientRecords))
        countedListOfUniqueListItems.append(self.Count_Number_Of_Insurance_Visits(uniqueListItems[4], patientRecords))

        return countedListOfUniqueListItems
    
    def Get_Statistics_Data(self):
        patientRecords = self.Get_Patient_Records()
        uniqueListItems = self.Get_All_Unique_Lists(patientRecords)
        countedListOfUniqueListItems = self.Count_All_Statisic_Attributes(uniqueListItems, patientRecords)
        return countedListOfUniqueListItems

        
            
        

    
