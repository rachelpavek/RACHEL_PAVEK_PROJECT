'''
===========================================================================
    File_Helper
===========================================================================
    Created By		Rachel pavek
    Created Date	12/03/2025
    Description		Used to interact with all file associated tasks
---------------------------------------------------------------------------
===========================================================================
    File_Helper
===========================================================================
'''
import sys
import json
import os

def Generate_Json_Credential_Template():
    return {
        "PRSloginCredentials": [
            {
                "Users":[],
                "UserRoles":[],
                "SystemActions":[],
                "ActionToRoleMapping":[]
            }
        ]
    }

def Generate_Json_Patient_Template():
    jsonData = {
    "PRSData": [
        {
            "PatientRecord": [],
            "PatientVisitRecord": [],
            "PatientVisitNotes": [],
            "PatientNotes": []
        }
    ]
} #default json format
    return jsonData

def Create_Json_File(fileName, fileType):#populating json file after creation
    if (fileType == 1):
        jsonTemplate = Generate_Json_Credential_Template()
    elif(fileType == 2):
        jsonTemplate = Generate_Json_Patient_Template()
    
    with open(fileName, "w") as patientFileWrite:
        json.dump(jsonTemplate, patientFileWrite, indent=4)
        patientFileWrite.close()            #Save Json

def Check_For_Json_File(fileName, fileType, override = False):          #Creating json file when file does not exist on computer
    fileExisted = True
    fileExits = os.path.isfile(fileName)
    fileExisted = fileExits
    if(fileExits == False and override == False):
        patientFileWrite = open(fileName, "w")
        patientFileWrite.close()            
        Create_Json_File(fileName, fileType)
        
    return fileExisted

def Extract_Json_Credential_Data(data):
    jsonObjects = []
    PRSData = data["PRSloginCredentials"]
    jsonObjects.append(data)
    jsonObjects.append(PRSData[0]["Users"])
    jsonObjects.append(PRSData[0]["UserRoles"])
    jsonObjects.append(PRSData[0]["SystemActions"])
    jsonObjects.append(PRSData[0]["ActionToRoleMapping"])

    return jsonObjects

def Extract_Json_Patient_Elements(data):
    jsonObjects = []
    PRSData = data["PRSData"]
    jsonObjects.append(data)
    jsonObjects.append(PRSData[0]["PatientRecord"])
    jsonObjects.append(PRSData[0]["PatientVisitRecord"])
    jsonObjects.append(PRSData[0]["PatientVisitNotes"])
    jsonObjects.append(PRSData[0]["PatientNotes"])
    
    return jsonObjects

def Read_Json_Credential_File(filePath):
    Check_For_Json_File(filePath, 1)
    with open(filePath, "r") as patientfile:
        data = json.load(patientfile)
      
    return Extract_Json_Credential_Data(data)

def Read_Json_Patient_File(filePath):
    Check_For_Json_File(filePath, 2)
    with open(filePath, "r") as patientfile:
        data = json.load(patientfile)
      
    return Extract_Json_Patient_Elements(data)

def Write_Json_File(filePath, data):
    Check_For_Json_File(filePath, 2)
    with open(filePath, "w") as patientFileWrite:
        json.dump(data, patientFileWrite, indent=4)
        

