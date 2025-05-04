'''
===========================================================================
    CSV_To_JSON_Converter
===========================================================================
    Created By		Rachel pavek
    Created Date	12/03/2025
    Description		Convert CSV To Json for easier management of data
---------------------------------------------------------------------------
===========================================================================
    CSV_To_JSON_Converter
===========================================================================
'''

import os
import json
import File_Helper
import General_Helper
import csv

def checkObjectForValue(listObject, value):
    for item in listObject:
        if (item == value):
            return True
    return False

def Get_Json_Patient_Data(filePath):
    return File_Helper.Read_Json_Patient_File(filePath)

def Get_Json_Credential_Data(filePath):
    print(filePath[1])
    return File_Helper.Read_Json_Credential_File(filePath) #get json from file

def Create_User_Role_Json_Data(jsonObjects, listOfRecordElements):
    roles = []

    roleID = 1

    for element in listOfRecordElements:
        if (len(element)== 1): #check for empty row
            break

        if (checkObjectForValue(roles, element[3]) == False):
            roles.append(element[3])

            roleData = [roleID, element[3]]
            jsonObjects[2].append(General_Helper.Generate_Role_Data_Json(roleData))
            roleID = roleID + 1
             
    return jsonObjects

def Create_User_Json_Data(jsonObjects, listOfRecordElements):
    usernames = []

    for element in listOfRecordElements:
        if (len(element)== 1): 
            break

        if (checkObjectForValue(usernames, element[1]) == False):
            usernames.append(element[1])
            userData = [element[1], element[2], General_Helper.Get_Role_ID(element[3], jsonObjects[2])]
        
            jsonObjects[1].append(General_Helper.Generate_User_Data_Json(userData))

    return jsonObjects

def Create_System_Action_Json_Data(jsonObjects):
    systemActions = [["Add_patient", 1], ["Remove_patient", 2], ["Retrieve_patient", 3], ["Count_visits", 4], ["View_note",  5], ["Generate_Statistics", 6]]

    for systemAction in systemActions:
        jsonObjects[3].append(General_Helper.Generate_System_Actions_Data_Json(systemAction))

    return jsonObjects

def Create_Action_Mapping_Json_Data(jsonObjects):
    for role in jsonObjects[2]:
        if (role["Role_Name"] == "nurse" or role["Role_Name"] == "clinician"):
            jsonObjects[4].append(General_Helper.Generate_Action_Mapping_Data_Json([role["Role_ID"], 1]))
            jsonObjects[4].append(General_Helper.Generate_Action_Mapping_Data_Json([role["Role_ID"], 2]))
            jsonObjects[4].append(General_Helper.Generate_Action_Mapping_Data_Json([role["Role_ID"], 3]))
            jsonObjects[4].append(General_Helper.Generate_Action_Mapping_Data_Json([role["Role_ID"], 4]))
            jsonObjects[4].append(General_Helper.Generate_Action_Mapping_Data_Json([role["Role_ID"], 5]))
            jsonObjects[4].append(General_Helper.Generate_Action_Mapping_Data_Json([role["Role_ID"], 6]))
        elif (role["Role_Name"] == "admin"):
            jsonObjects[4].append(General_Helper.Generate_Action_Mapping_Data_Json([role["Role_ID"], 4]))
        elif (role["Role_Name"] == "management"):
            jsonObjects[4].append(General_Helper.Generate_Action_Mapping_Data_Json([role["Role_ID"], 6]))

    return jsonObjects

def Create_Patient_Note_Json_Data(jsonObjects, listOfRecordElements):
    noteIds = []

    for element in listOfRecordElements:
        if (len(element)== 1): 
            break

        if (checkObjectForValue(noteIds, element[3]) == False):
            noteIds.append(element[3])

            patientNoteData = [element[1], element[2], element[3], element[4]]

            jsonObjects[4].append(General_Helper.Generate_Patient_Note_Data_Json(patientNoteData))

    return jsonObjects
                        
def Create_Patient_Json_Data(jsonObjects, listOfRecordElements):
    #declare lists of new records
    patientIds = []
    visitIds = []
    visitNoteIds = []

    for element in listOfRecordElements:
        if (len(element)== 1): #check for empty row
            break
        if (checkObjectForValue(patientIds, element[0]) == False):#check patientIds for patientId if it doesnt exist create a new patient record
            patientIds.append(element[0])#add patientId to list to stop duplicates
        
            patientData = [element[5], element[4], element[7], element[6], element[9]]#create list of patient data
            newPatientRecord = General_Helper.Generate_Patient_Data_Json(element[0], patientData)
        
            jsonObjects[1].append(newPatientRecord)#add new record to PatientRecord json object
        
        if (checkObjectForValue(visitIds, element[1]) == False): #check visitIds for visitId if it doesnt exist create a new visit record
            visitIds.append(element[1])#add visitId to list to stop duplicates
        
            visitData = [element[1], element[2], element[3], element[8]]#create list of visit data
            newPatientVisitRecord = General_Helper.Generate_Visit_Data_Json(element[0], visitData)
        
            jsonObjects[2].append(newPatientVisitRecord)#add new record to PatientVisitRecord json object

        if (checkObjectForValue(visitNoteIds, element[11]) == False): #check visitNoteIds for visitNoteId if it doesnt exist create a new note record
            visitNoteIds.append(element[11])#add NoteId to list to stop duplicates
            noteData = [element[10], element[11], element[12]]#create list of note data
            newPatientVisitNote = General_Helper.Generate_Note_Data_Json(element[0], noteData, visitData)
            
            jsonObjects[3].append(newPatientVisitNote)#add new record to PatientVisitNotes json object

    return jsonObjects
    
def Append_Json_Credential_Objects(credentialData, filePath, override = False):
    if (override == False):
        jsonObjects = Get_Json_Credential_Data(filePath)
        jsonObjects = Create_User_Role_Json_Data(jsonObjects, credentialData[0])
        jsonObjects = Create_User_Json_Data(jsonObjects, credentialData[0])
        jsonObjects = Create_System_Action_Json_Data(jsonObjects)
        jsonObjects = Create_Action_Mapping_Json_Data(jsonObjects)
    
        File_Helper.Write_Json_File(filePath,jsonObjects[0])
        return True
    else:
        return False
    
def Append_Json_Patient_Objects(csvsFileData, filePath, override = False):
    if (override == False):
        jsonObjects = Get_Json_Patient_Data(filePath)
        jsonObjects = Create_Patient_Json_Data(jsonObjects, csvsFileData[1])
        jsonObjects = Create_Patient_Note_Json_Data(jsonObjects, csvsFileData[0])
    
        File_Helper.Write_Json_File(filePath,jsonObjects[0])
        return True
    else:
        return False
    
def Convert_Patient_Data(csvFilePaths, filePath):
    patientData = []
    
    for csvFilePath in csvFilePaths:
        listOfRecordElements = []
        try:
            with open(csvFilePath, mode='r', newline='', encoding='utf-8', errors='replace') as fileData:
                records = csv.reader(fileData)
                #records.pop(0) #remove header from patient records
                firstLine = True
                for record in records:
                    if (firstLine == False):
                        #elements = record.split(",")
                        listOfRecordElements.append(record)
                    else: firstLine = False
                
                patientData.append(listOfRecordElements)
    
        except Exception as e:
            override = True
            print(e)
            print("Unable to load file: "+csvFilePath)
            return False

    Append_Json_Patient_Objects(patientData, filePath)

def Convert_User_Credential_Data(csvFilePath, filePath):
    
    credentialData = []
    listOfRecordElements = []
    
    try:
        with open(csvFilePath, mode='r', newline='', encoding='utf-8', errors='replace') as fileData:
            records = csv.reader(fileData)
                #records.pop(0) #remove header from patient records
            firstLine = True
            for record in records:
                if (firstLine == False):
                        #elements = record.split(",")
                    listOfRecordElements.append(record)
                else: firstLine = False
                
            credentialData.append(listOfRecordElements)

    except Exception as e:
        override = True
        print(e)
        print("Unable to load file: "+csvFilePath)
        return False
    
    Append_Json_Credential_Objects(credentialData, filePath)
    
def Convert_CSV_To_JSON(csvFilePaths, filePaths):
    override = False

    csvsFileData = []
    print(filePaths[0])
    Convert_User_Credential_Data(csvFilePaths[2], filePaths[0])
    Convert_Patient_Data(csvFilePaths[0:2], filePaths[1])
