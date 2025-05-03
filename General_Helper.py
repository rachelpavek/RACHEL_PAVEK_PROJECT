'''
===========================================================================
    General_Helper
===========================================================================
    Created By		Rachel pavek
    Created Date	12/03/2025
    Description		General Helper for multiple use cases
---------------------------------------------------------------------------
===========================================================================
    General_Helper
===========================================================================
'''
import random
from datetime import datetime

def Generate_System_Actions_Data_Json(actionData):
        return {
                "ActionID": actionData[1],
                "ActionName": actionData[0]
                }

def Generate_Action_Mapping_Data_Json(actionMappingData):
        return {
                "RoleID": actionMappingData[0],
                "ActionID": actionMappingData[1]
                }

def Generate_Role_Data_Json(roleData):
        return {
                "Role_ID": roleData[0],
                "Role_Name": roleData[1]
                }

def Generate_User_Data_Json(userData):
        return {
                "Username": userData[0],
                "Password": userData[1],
                "Role_ID": userData[2]
                }
def Generate_Patient_Note_Data_Json(patientNoteData):
        return {
                "Patient_ID": patientNoteData[0],
                "Visit_ID": patientNoteData[1],
                "Note_ID": patientNoteData[2],
                "Note_text": patientNoteData[3]
                }

def Generate_Patient_Data_Json(patientID, patientData):
        return {
                    "Patient_ID": patientID,
                    "Gender": patientData[0],
                    "Race": patientData[1],
                    "Age": patientData[2],
                    "Ethnicity": patientData[3],
                    "Insurance": patientData[4],
                }#form json patient record object from a list of data

def Generate_Visit_Data_Json(patientID, visitData):
        return {
                    "Patient_ID": patientID,
                    "Visit_ID": visitData[0],
                    "Visit_time": visitData[1],
                    "Visit_department": visitData[2],
                    "ZipCode": visitData[3]
                } #form json visit object from a list of data

def Generate_Note_Data_Json(patientID, noteData, visitData):
        return {
                    "Patient_ID": patientID,
                    "Visit_ID": visitData[1],
                    "Note_ID": noteData[0],
                    "Chief_complaint": noteData[1],
                    "Note_type": noteData[2]
                } #form json note object from a list of data

def Generate_Additional_Information_Note_Data_Json(patientID, visitData, noteData):
        return {
                    "Patient_ID": patientID,
                    "Visit_ID": visitData[0],
                    "Note_ID": noteData[0],
                    "Note_text": noteData[2],
                }

def Generate_ID(): #generate six-digit ID
        return str(random.randrange(100000,999999))
        
def Generate_Visit_Time(): #get current date 
        currentDateTime = datetime.now()
        return currentDateTime.strftime("%d/%m/%Y")

def Get_Role_ID(roleName, roleData):
        for role in roleData:
                if(role["Role_Name"] == roleName):
                        return (role["Role_ID"])

        print ("Failed to return role ID")      
