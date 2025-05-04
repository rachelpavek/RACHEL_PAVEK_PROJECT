'''
===========================================================================
    Record_Helper
===========================================================================
    Created By		Rachel pavek
    Created Date	12/03/2025
    Description		To help with all record collection associated tasks
---------------------------------------------------------------------------
===========================================================================
    Record_Helper
===========================================================================
'''
import File_Helper
import json



def Remove_Patient_Record(searchValue, jsonObject, jsonElementName):
    originalJsonObject = jsonObject[:]
    for patientRecord in originalJsonObject:
        if (patientRecord[jsonElementName]== searchValue):
            jsonObject.remove(patientRecord)
    return jsonObject
    
def Remove_Patient_Visit_Records(searchValue, jsonObject, jsonElementName):
    originalJsonObject = jsonObject[:]
    for visitRecord in originalJsonObject:
        if (visitRecord[jsonElementName]== searchValue):
            jsonObject.remove(visitRecord)
    return jsonObject
    
def Remove_Patient_Visit_Notes(searchValue, jsonObject, jsonElementName):
    originalJsonObject = jsonObject[:]
    for patientVisitNote in originalJsonObject:
        if (patientVisitNote[jsonElementName]== searchValue):
            jsonObject.remove(patientVisitNote)
    return jsonObject
    
def Remove_Additional_Information_Note_Data(searchValue, jsonObject, jsonElementName):
    originalJsonObject = jsonObject[:]
    for additionalInformationNote in originalJsonObject:
        if (additionalInformationNote[jsonElementName]== searchValue):
            jsonObject.remove(additionalInformationNote)
    return jsonObject
    
def Get_Patient_Record(searchValue, filePath, jsonElementName, overRide = False):
    fileData = File_Helper.Read_Json_Patient_File(filePath)

    searchedPatientRecords = []

    for patientRecord in fileData[1]:#loop through PatientRecord json object for each patient record
        if(patientRecord[jsonElementName]== searchValue or overRide == True): #generic if statement that searches by element for search value
            searchedPatientRecords.append(patientRecord)
            
    return searchedPatientRecords

def Get_Patient_Visit_Records(searchValue, filePath, jsonElementName, overRide = False):
    fileData = File_Helper.Read_Json_Patient_File(filePath)
    
    patientVisitRecords = []
    
    for patientVisitRecord in fileData[2]:#loop through PatientVisitRecord json object for each visit record
        if(patientVisitRecord[jsonElementName]== searchValue or overRide == True): #generic if statement that searches by element for search value
            patientVisitRecords.append(patientVisitRecord)
            
    return patientVisitRecords
        
def Get_Patient_Visit_Notes(searchValue, filePath, jsonElementName, overRide = False):
    fileData = File_Helper.Read_Json_Patient_File(filePath)
    
    patientVisitNotes = []
    
    for patientVisitNote in fileData[3]:#loop through PatientVisitNotes json object for each note record
        if(patientVisitNote[jsonElementName]== searchValue or overRide == True): #generic if statement that searches by element for search value
            patientVisitNotes.append(patientVisitNote)

    return patientVisitNotes

def Get_User_Record(searchValue, secondarySearchValue, filePath, jsonElementName, secondaryJsonElementName):
    fileData = File_Helper.Read_Json_Credential_File(filePath)

    userRecords = []

    for userRecord in fileData[1]:
        if (userRecord[jsonElementName]== searchValue and userRecord[secondaryJsonElementName]== secondarySearchValue):
            userRecords.append(userRecord)

    return userRecords

def Get_User_Role(searchValue, filePath, jsonElementName):
    fileData = File_Helper.Read_Json_File(filePath)

    userRoles = []

    for userRole in fileData[6]:
        if (userRole[jsonElementName]== searchValue):
            userRoles.append(userRole)

    return userRoles

def Get_Action_Mapping(searchValue, filePath, jsonElementName):
    fileData = File_Helper.Read_Json_Credential_File(filePath)

    actionsMapping = []

    for actionMapping in fileData[4]:
        if (actionMapping[jsonElementName]== searchValue):
            actionsMapping.append(actionMapping)

    return actionsMapping

def Get_Action(searchValue, filePath, jsonElementName):
    fileData = File_Helper.Read_Json_Credential_File(filePath)

    userActions = []

    for userAction in fileData[3]:
        if(userAction[jsonElementName]== searchValue):
            userActions.append(userAction)

    return userActions[0]



            
