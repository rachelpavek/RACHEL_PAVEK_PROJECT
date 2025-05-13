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

def Generate_Login_Events_Data_Json(EventData):
        userID = "Unknown"
        roleName = "Unknown"
        if(EventData[0] != None):
                userID = EventData[0]
        if(EventData[2] != None):
                roleName = EventData[2]
        return{
                "EventID": Generate_ID(),
                "UserID": userID,
                "UserName": EventData[1],
                "RoleName": roleName,
                "LoginTime": Generate_Event_Time(),
                "Success": EventData[3]
                }

def Generate_Actions_Preformed_Data_Json(ActionData):
        return {
                "ActionsPreformedID": Generate_ID(),
                "EventID": ActionData[0],
                "ActionPreformed": ActionData[1],
                "ActionPreformedTime": Generate_Event_Time()
                }

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
                "UserID": Generate_ID(),
                "Username": userData[0],
                "Password": userData[1],
                "Role_ID": userData[2]
                }
def Generate_Patient_Note_Data_Json(patientNoteData):
        return {
                "Patient_ID": patientNoteData[1],
                "Visit_ID": patientNoteData[2],
                "Note_ID": patientNoteData[3],
                "Note_text": patientNoteData[4]
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
                    "Visit_ID": visitData[1],
                    "Visit_time": Generate_Visit_Time(visitData[2]),
                    "Visit_department": visitData[3],
                    "ZipCode": visitData[4]
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
                    "Visit_ID": visitData[1],
                    "Note_ID": noteData[0],
                    "Note_text": noteData[1],
                }

def Generate_ID(): #generate six-digit ID
        return str(random.randrange(100000,999999))
        
def Generate_Visit_Time(recordDateTime = None): #get current date
        if (recordDateTime == None):
                recordDateTime = datetime.now()
        else:
                recordDateTime = datetime.strptime(recordDateTime, "%m/%d/%Y")
        return recordDateTime.strftime("%m/%d/%Y")

def Generate_Event_Time():
        recordDateTime = datetime.now()
        return recordDateTime.strftime("%m/%d/%Y %H:%M:%S")

def Get_Role_ID(roleName, roleData):
        for role in roleData:
                if(role["Role_Name"] == roleName):
                        return (role["Role_ID"])

        return False     
