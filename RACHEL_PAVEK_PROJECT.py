import tkinter as tk
import Login_Menu_Helper
import Back_End_Helper
from tkinter import messagebox

def show_error(errorMessage, ErrorMessageTitle = "Error"):
    messagebox.showerror(ErrorMessageTitle, errorMessage)


def Add_Action_Frame(actionName):
    global actionAreaFrame
    actionTypeLabel = tk.Label(actionAreaFrame, text= "Action: " + actionName, bg='#FFD1DC', font=("Roboto", 12))
    actionTypeLabel.place(x = 0, y = 0)
    
    customActionFrame = tk.Frame(actionAreaFrame, highlightbackground="black", bd = 1, relief="solid", width=550, height=250)
    customActionFrame.place(x=15, y=30)

    return customActionFrame
   
def Clear_Frame(frame):
    for widget in frame.winfo_children():  # Get all child widgets
        widget.destroy()

def Create_Preformed_Action_Record(ActionName):
    backEndClass = Back_End_Helper.Log_Usage_Record()
    backEndClass.Create_Preformed_Action_Record(loginData["UserID"], ActionName)

def Add_Patient():
    Create_Preformed_Action_Record("Add Patient")
    def Get_Patient(frame):
        global backEndClass
        def Capture_Patient_Data(frame):
            genderLabel = tk.Label(frame, text= "Enter Gender: ", bg='#FFD1DC', font=("Roboto", 12))
            genderEntry = tk.Entry(frame, font=("Roboto", 12),)
            raceLabel = tk.Label(frame, text= "Enter Race: ", bg='#FFD1DC', font=("Roboto", 12))
            raceEntry = tk.Entry(frame, font=("Roboto", 12),)
            ageLabel = tk.Label(frame, text= "Enter Age: ", bg='#FFD1DC', font=("Roboto", 12))
            ageEntry = tk.Entry(frame, font=("Roboto", 12),)
            ethnicityLabel = tk.Label(frame, text= "Enter Ethnicity: ", bg='#FFD1DC', font=("Roboto", 12))
            ethnicityEntry = tk.Entry(frame, font=("Roboto", 12),)
            insuranceLabel = tk.Label(frame, text= "Enter Insurance: ", bg='#FFD1DC', font=("Roboto", 12))
            insuranceEntry = tk.Entry(frame, font=("Roboto", 12),)
            nextButton = tk.Button(frame, text="Next", bg="#C11C84", command= lambda v= frame:Capture_Visit_Data(v))

            genderLabel.place(x=5, y=5)
            genderEntry.place(x=200, y=5)
            raceLabel.place(x=5, y=35)
            raceEntry.place(x=200, y=35)
            ageLabel.place(x=5, y=65)
            ageEntry.place(x=200, y=65)
            ethnicityLabel.place(x=5, y=95)
            ethnicityEntry.place(x=200, y=95)
            insuranceLabel.place(x=5, y=125)
            insuranceEntry.place(x=200, y=125)
            nextButton.place(x=5, y=155)
            
            def Capture_Visit_Data(frame):
                global patientData
                patientData = [genderEntry.get(), raceEntry.get(), ageEntry.get(), ethnicityEntry.get(), insuranceEntry.get()]
                Clear_Frame(frame)
                visitDepartmentLabel = tk.Label(frame, text= "Enter Visit Department: ", bg='#FFD1DC', font=("Roboto", 12))
                visitDepartmentEntry = tk.Entry(frame, font=("Roboto", 12),)
                zipcodeLabel = tk.Label(frame, text= "Enter Zipcode: ", bg='#FFD1DC', font=("Roboto", 12))
                zipcodeEntry = tk.Entry(frame, font=("Roboto", 12),)
                nextButton = tk.Button(frame, text="Next", bg="#C11C84", command= lambda v= frame:Capture_Note_Data(v))
                
                visitDepartmentLabel.place(x=5, y=5)
                visitDepartmentEntry.place(x=200, y=5)
                zipcodeLabel.place(x=5, y=35)
                zipcodeEntry.place(x=200, y=35)
                nextButton.place(x=5, y=65)

                def Capture_Note_Data(frame):
                    global visitData
                    def Create_Patient_Record(frame):
                        global patientData, visitData, backEndClass
                        noteData = [chiefComplaintEntry.get(), noteTypeEntry.get()]
                        additionalNoteData = [additionalInfoEntry.get()]
                        Clear_Frame(frame)
                        backEndClass.Create_Patient_Record(patientData, visitData, noteData, additionalNoteData)
                    visitData = [visitDepartmentEntry.get(), zipcodeEntry.get()]
                    Clear_Frame(frame)
                    chiefComplaintLabel = tk.Label(frame, text= "Enter Chief Complaint: ", bg='#FFD1DC', font=("Roboto", 12))
                    chiefComplaintEntry = tk.Entry(frame, font=("Roboto", 12),)
                    additionalInfoLabel = tk.Label(frame, text= "Enter Additional Information: ", bg='#FFD1DC', font=("Roboto", 12))
                    additionalInfoEntry = tk.Entry(frame, font=("Roboto", 12),)
                    noteTypeLabel = tk.Label(frame, text= "Enter Note Type: ", bg='#FFD1DC', font=("Roboto", 12))
                    noteTypeEntry = tk.Entry(frame, font=("Roboto", 12),)
                    enterButton = tk.Button(frame, text="Enter", bg="#C11C84", command= lambda v= frame:Create_Patient_Record(v))

                    chiefComplaintLabel.place(x=5, y=5)
                    chiefComplaintEntry.place(x=220, y=5)
                    additionalInfoLabel.place(x=5, y=35)
                    additionalInfoEntry.place(x=220, y=35)
                    noteTypeLabel.place(x=5, y=65)
                    noteTypeEntry.place(x=220, y=65)
                    enterButton.place(x=5, y=95)

        def Create_Visit_Record(addPatientSubMenuFrame):
            def Create_Record():
                global backEndClass
                backEndClass.Create_Visit_Record(visitDepartmentEntry.get(), hospitalZipcodeEntry.get())
            Clear_Frame(addPatientSubMenuFrame)
            visitDepartmentLabel = tk.Label(addPatientSubMenuFrame, text= "Enter Visit Department: ", bg='#FFD1DC', font=("Roboto", 12))
            visitDepartmentEntry = tk.Entry(addPatientSubMenuFrame, font=("Roboto", 12),)
            hospitalZipcodeLabel = tk.Label(addPatientSubMenuFrame, text= "Enter Hospital Zipcode: ", bg='#FFD1DC', font=("Roboto", 12))
            hospitalZipcodeEntry = tk.Entry(addPatientSubMenuFrame, font=("Roboto", 12),)
            enterButton = tk.Button(addPatientSubMenuFrame, text="Enter", bg="#C11C84", command=Create_Record)
            visitDepartmentLabel.place(x=5, y=5)
            visitDepartmentEntry.place(x=200, y=5)
            hospitalZipcodeLabel.place(x=5, y=35)
            hospitalZipcodeEntry.place(x=200, y=35)
            enterButton.place(x=100, y=65)
            
        def Create_Note(addPatientSubMenuFrame):
            def Create_Record():
                global backEndClass
                backEndClass.Create_Note_Record(chiefComplaintEntry.get(), additionalInformationEntry.get(), noteTypeEntry.get())
            Clear_Frame(addPatientSubMenuFrame)
            chiefComplaintLabel = tk.Label(addPatientSubMenuFrame, text= "Enter Chief Complaint: ", bg='#FFD1DC', font=("Roboto", 12))
            chiefComplaintEntry = tk.Entry(addPatientSubMenuFrame, font=("Roboto", 12),)
            additionalInformationLabel = tk.Label(addPatientSubMenuFrame, text= "Enter Additional Information: ", bg='#FFD1DC', font=("Roboto", 12))
            additionalInformationEntry = tk.Entry(addPatientSubMenuFrame, font=("Roboto", 12),)
            noteTypeLabel = tk.Label(addPatientSubMenuFrame, text= "Enter Note Type: ", bg='#FFD1DC', font=("Roboto", 12))
            noteTypeEntry = tk.Entry(addPatientSubMenuFrame, font=("Roboto", 12),)
            enterButton = tk.Button(addPatientSubMenuFrame, text="Enter", bg="#C11C84", command=Create_Record)
            chiefComplaintLabel.place(x=5, y=5)
            chiefComplaintEntry.place(x=225, y=5)
            additionalInformationLabel.place(x=5, y=35)
            additionalInformationEntry.place(x=225, y=35)
            noteTypeLabel.place(x=5, y=65)
            noteTypeEntry.place(x=225, y=65)
            enterButton.place(x=125, y=95)

            
        backEndClass = Back_End_Helper.Add_Patient(patientIdEntry.get())
        patientRecord = backEndClass.Get_Patient_Record()
        if(len(patientRecord) == 1):
            Clear_Frame(frame)
            actionSubButtonFrame = tk.Frame(frame, width=540, height=30)
            actionSubButtonFrame.place(x=5, y=5)
            addPatientSubMenuFrame = tk.Frame(frame, highlightbackground="black", bd = 1, relief="solid", width=540, height=205)
            addPatientSubMenuFrame.place(x=5, y=40)
            createVisitRecordButton = tk.Button(customActionFrame, text="Create Visit Record", bg="#C11C84", command= lambda v= addPatientSubMenuFrame: Create_Visit_Record(v))
            createNoteButton = tk.Button(customActionFrame, text="Create Note", bg="#C11C84", command= lambda v= addPatientSubMenuFrame: Create_Note(v))
            createVisitRecordButton.place(x=5, y=5)
            createNoteButton.place(x=130, y=5)
        else:
            Clear_Frame(frame)
            Capture_Patient_Data(frame)
            

        
    customActionFrame = Add_Action_Frame("Add Patient")
    patientIdLabel = tk.Label(customActionFrame, text= "Enter Patient ID: ", bg='#FFD1DC', font=("Roboto", 12))
    patientIdEntry = tk.Entry(customActionFrame, font=("Roboto", 12),)
    patientIdLabel.place(x= 5, y=5)
    patientIdEntry.place(x= 5, y=35)
    searchButton = tk.Button(customActionFrame, text="Search", bg="#C11C84", command= lambda v= customActionFrame: Get_Patient(v))
    searchButton.place(x= 70, y=65)

def Remove_Patient():
    Create_Preformed_Action_Record("Remove Patient")
    def Get_Patient(frame):
        backEndClass = Back_End_Helper.Remove_Patient(patientIdEntry.get())
        patientRecord = backEndClass.Get_Patient_Record()
        if(len(patientRecord) == 1):
            Clear_Frame(frame)
            backEndClass.Remove_Patient_Records()
        else:
            show_error("No patient found matching the patient ID: "+patientIdEntry.get(), "No Record")
    customActionFrame = Add_Action_Frame("Remove Patient")
    patientIdLabel = tk.Label(customActionFrame, text= "Enter Patient ID: ", bg='#FFD1DC', font=("Roboto", 12))
    patientIdEntry = tk.Entry(customActionFrame, font=("Roboto", 12),)
    patientIdLabel.place(x= 5, y=5)
    patientIdEntry.place(x= 5, y=35)
    searchButton = tk.Button(customActionFrame, text="Search", bg="#C11C84", command= lambda v= customActionFrame: Get_Patient(v))
    searchButton.place(x= 70, y=65)
    

def Retrieve_Patient():
    Create_Preformed_Action_Record("Retrieve Patient")
    def Get_Patient(frame):
        global retrievePatientSubMenuFrame
        def Display_Selected_Value(jsonElementName, patientRecord):
            global retrievePatientSubMenuFrame
            Clear_Frame(retrievePatientSubMenuFrame)
            displayValueLabel = tk.Label(retrievePatientSubMenuFrame, text= "The Patient's "+ jsonElementName + " is " + patientRecord[0][jsonElementName], bg='#FFD1DC', font=("Roboto", 12))
            displayValueLabel.place(x=0, y=0)
            
        backEndClass = Back_End_Helper.Retrieve_Patient(patientIdEntry.get())
        patientRecord = backEndClass.Get_Patient_Record()
        if(len(patientRecord) == 1):
            Clear_Frame(frame)

            actionSubButtonFrame = tk.Frame(frame, width=540, height=30)
            actionSubButtonFrame.place(x=5, y=5)
            retrievePatientSubMenuFrame = tk.Frame(frame, highlightbackground="black", bd = 1, relief="solid", width=540, height=205)
            retrievePatientSubMenuFrame.place(x=5, y=40)
            getGenderValueButton = tk.Button(actionSubButtonFrame, text="Gender", bg="#C11C84", command= lambda v= "Gender", v2 = patientRecord: Display_Selected_Value(v, v2))
            getRaceValueButton = tk.Button(actionSubButtonFrame, text="Race", bg="#C11C84", command= lambda v= "Race", v2 = patientRecord: Display_Selected_Value(v, v2))
            getAgeValueButton = tk.Button(actionSubButtonFrame, text="Age", bg="#C11C84", command= lambda v= "Age", v2 = patientRecord: Display_Selected_Value(v, v2))
            getEthnicityValueButton = tk.Button(actionSubButtonFrame, text="Ethnicity", bg="#C11C84", command= lambda v= "Ethnicity", v2 = patientRecord: Display_Selected_Value(v, v2))
            getInsuranceValueButton = tk.Button(actionSubButtonFrame, text="Insurance", bg="#C11C84", command= lambda v= "Insurance", v2 = patientRecord: Display_Selected_Value(v, v2))
            getGenderValueButton.grid(row=0, column=0, padx= 5)
            getRaceValueButton.grid(row=0, column=1, padx= 5)
            getAgeValueButton.grid(row=0, column=2, padx= 5)
            getEthnicityValueButton.grid(row=0, column=3, padx= 5)
            getInsuranceValueButton.grid(row=0, column=4, padx= 5)
        else:
            show_error("No patient found matching the patient ID: "+patientIdEntry.get(), "No Record")
    customActionFrame = Add_Action_Frame("Retrieve Patient")
    patientIdLabel = tk.Label(customActionFrame, text= "Enter Patient ID: ", bg='#FFD1DC', font=("Roboto", 12))
    patientIdEntry = tk.Entry(customActionFrame, font=("Roboto", 12),)
    patientIdLabel.place(x= 5, y=5)
    patientIdEntry.place(x= 5, y=35)
    searchButton = tk.Button(customActionFrame, text="Search", bg="#C11C84", command= lambda v= customActionFrame: Get_Patient(v))
    searchButton.place(x= 70, y=65)
   

def Count_Visits():
    Create_Preformed_Action_Record("Count Visits")
    customActionFrame = Add_Action_Frame("Count Visits")

    def Count_Patient_Visits(frame):
        backEndClass = Back_End_Helper.Count_Visits(dateEntry.get())
        Clear_Frame(frame)
        visitRecords = backEndClass.Get_Visit_Records()
        displayValueLabel = tk.Label(frame, text= "Total Visits: " +str(len(visitRecords)), bg='#FFD1DC', font=("Roboto", 12))
        displayValueLabel.place(x=0, y=0)
        
    dateLabel = tk.Label(customActionFrame, text= "Enter Date: MM/DD/YYYY ", bg='#FFD1DC', font=("Roboto", 12))
    dateEntry = tk.Entry(customActionFrame, font=("Roboto", 12),)
    dateLabel.place(x= 5, y=5)
    dateEntry.place(x= 5, y=35)
    searchButton = tk.Button(customActionFrame, text="Search", bg="#C11C84", command= lambda v= customActionFrame: Count_Patient_Visits(v))
    searchButton.place(x= 70, y=65)
    

def View_Note():
    Create_Preformed_Action_Record("View Note")
    def Get_Patient(frame):
        backEndClass = Back_End_Helper.View_Note(patientIdEntry.get())
        patientRecord = backEndClass.Get_Patient_Record()
        if(len(patientRecord) == 1):
            fullNoteData = backEndClass.Get_Patient_Notes(dateEntry.get())
            if (fullNoteData != False):
                Clear_Frame(frame)
                chiefComplaintLabel = tk.Label(frame, text= "Chief Complaint: " + fullNoteData[0]["Chief_complaint"], bg='#FFD1DC', font=("Roboto", 12))
                noteTypeLabel = tk.Label(frame, text= "Note Type: "+ fullNoteData[0]["Note_type"], bg='#FFD1DC', font=("Roboto", 12))
                noteTextScrollFrame = tk.Frame(frame, width=100, height=30)
                additionalNoteLabel = tk.Text(noteTextScrollFrame, wrap="word", height=9, width=57, bg='#FFD1DC', font=("Roboto", 12))
                scrollbar = tk.Scrollbar(noteTextScrollFrame, orient="vertical", width=20, command= additionalNoteLabel.yview)

                additionalNoteLabel.configure(yscrollcommand=scrollbar.set)
                additionalNoteLabel.insert("1.0", fullNoteData[1]["Note_text"])
                additionalNoteLabel.configure(state = "disabled")
                
                chiefComplaintLabel.place(x= 5, y=5)
                noteTypeLabel.place(x= 5, y=35)
                noteTextScrollFrame.place(x= 5, y=65)
                additionalNoteLabel.pack(side="left", fill="both", expand=True)
                scrollbar.pack(side="right", fill="y")

            else:
                show_error("Unable to retrieve note data for date: "+dateEntry.get(), "Record Recovery Failure")
        else:
            show_error("No patient found matching the patient ID: "+patientIdEntry.get(), "No Record")
            
    customActionFrame = Add_Action_Frame("View Note")
    patientIdLabel = tk.Label(customActionFrame, text= "Enter Patient ID: ", bg='#FFD1DC', font=("Roboto", 12))
    patientIdEntry = tk.Entry(customActionFrame, font=("Roboto", 12),)
    dateLabel = tk.Label(customActionFrame, text= "Enter Date: MM/DD/YYYY ", bg='#FFD1DC', font=("Roboto", 12))
    dateEntry = tk.Entry(customActionFrame, font=("Roboto", 12),)
    
    
    patientIdLabel.place(x= 5, y=5)
    patientIdEntry.place(x= 5, y=35)
    dateLabel.place(x= 5, y=65)
    dateEntry.place(x= 5, y=95)
    searchButton = tk.Button(customActionFrame, text="Search", bg="#C11C84", command= lambda v= customActionFrame: Get_Patient(v))
    searchButton.place(x= 70, y=125)
    

def Generate_Statistics():
    Create_Preformed_Action_Record("Generate Statistics")
    global countedListOfUniqueListItems
    def Gender_Statistics(frame):
        Clear_Frame(frame)
        rowNo = 0
        for genderStatistic in countedListOfUniqueListItems[0]:     
            statisticsLabel = tk.Label(frame, text= "Number of "+ genderStatistic[0]+"s that visited: "+str(genderStatistic[1]), bg='#FFD1DC', font=("Roboto", 12))
            statisticsLabel.grid(row=rowNo, column= 0, pady=2, padx=5)
            rowNo = rowNo +1

    def Age_Statistics(frame):
        Clear_Frame(frame)
        rowNo = 0
        for ageStatistic in countedListOfUniqueListItems[1]:     
            statisticsLabel = tk.Label(frame, text= "Number of "+ ageStatistic[0]+"s that visited: "+str(ageStatistic[1]), bg='#FFD1DC', font=("Roboto", 12))
            statisticsLabel.grid(row=rowNo, column= 0, pady=2, padx=5)
            rowNo = rowNo +1

    def Race_Statistics(frame):
        Clear_Frame(frame)
        rowNo = 0
        for raceStatistic in countedListOfUniqueListItems[2]:     
            statisticsLabel = tk.Label(frame, text= "Number of "+ raceStatistic[0]+"s that visited: "+str(raceStatistic[1]), bg='#FFD1DC', font=("Roboto", 12))
            statisticsLabel.grid(row=rowNo, column= 0, pady=2, padx=5)
            rowNo = rowNo +1
    
    def Ethnicity_Statistics(frame):
        Clear_Frame(frame)
        rowNo = 0
        for ethnicityStatistic in countedListOfUniqueListItems[3]:     
            statisticsLabel = tk.Label(frame, text= "Number of "+ ethnicityStatistic[0]+"s that visited: "+str(ethnicityStatistic[1]), bg='#FFD1DC', font=("Roboto", 12))
            statisticsLabel.grid(row=rowNo, column= 0, pady=2, padx=5)
            rowNo = rowNo +1

    def Insurance_Statistics(frame):
        Clear_Frame(frame)
        rowNo = 0
        for insuranceStatistic in countedListOfUniqueListItems[4]:     
            statisticsLabel = tk.Label(frame, text= "Number of "+ insuranceStatistic[0]+"s that visited: "+str(insuranceStatistic[1]), bg='#FFD1DC', font=("Roboto", 12))
            statisticsLabel.grid(row=rowNo, column= 0, pady=2, padx=5)
            rowNo = rowNo +1

    backEndClass = Back_End_Helper.Generate_Statistics()
    countedListOfUniqueListItems = backEndClass.Get_Statistics_Data()
    
    customActionFrame = Add_Action_Frame("Generate Statistics")
    actionSubButtonFrame = tk.Frame(customActionFrame, width=500, height=30)
    actionSubButtonFrame.place(x=5, y=5)
    statisticsSubMenuFrame = tk.Frame(customActionFrame, highlightbackground="black", bd = 1, relief="solid", width=500, height=205)
    statisticsSubMenuFrame.place(x=5, y=40)
    statisticsSubMenuFrame.grid_propagate(False)
    genderButton = tk.Button(actionSubButtonFrame, text="Gender Statistics", bg="#C11C84", command= lambda v= statisticsSubMenuFrame: Gender_Statistics(v))
    ageButton = tk.Button(actionSubButtonFrame, text="Age Statistics", bg="#C11C84", command= lambda v= statisticsSubMenuFrame: Age_Statistics(v))
    raceButton = tk.Button(actionSubButtonFrame, text="Race Statistics", bg="#C11C84", command= lambda v= statisticsSubMenuFrame: Race_Statistics(v))
    ethnicityButton = tk.Button(actionSubButtonFrame, text="Ethnicity Statistics", bg="#C11C84", command= lambda v= statisticsSubMenuFrame: Ethnicity_Statistics(v))
    insuranceButton = tk.Button(actionSubButtonFrame, text="Insurance Statistics", bg="#C11C84", command= lambda v= statisticsSubMenuFrame: Insurance_Statistics(v))

    genderButton.grid(row=0, column=0, padx=5)
    ageButton.grid(row=0, column=1, padx=5)
    raceButton.grid(row=0, column=2, padx=5)
    ethnicityButton.grid(row=0, column=3, padx=5)
    insuranceButton.grid(row=0, column=4, padx=5)




def Dynamic_Action(buttonId):
    global actionAreaFrame
    Clear_Frame(actionAreaFrame)
    if(buttonId == 1):
        Add_Patient()
        
    elif(buttonId == 2):
        Remove_Patient()
        
    elif(buttonId == 3):
        Retrieve_Patient()
        
    elif(buttonId == 4):
         Count_Visits()
         
    elif(buttonId == 5):
        View_Note()
        
    elif(buttonId == 6):
        Generate_Statistics()
        
def Create_Action_Window():
    actionWindow = tk.Tk()
    actionWindow.title("Action Window")
    actionWindow.geometry('600x385')
    actionWindow.configure(bg='#FC6C85')
    actionWindow.resizable(False, False)

    return actionWindow

#customActionFrame = tk.Frame(actionAreaFrame, highlightbackground="black", bd = 1, relief="solid", width=550, height=250)
#customActionFrame.place(x=15, y=30)
#customActionFrame.place_propagate(False)

#actionTypeLabel = tk.Label(actionAreaFrame, text="Action: ", bg='#FFD1DC', font=("Roboto", 12))
#actionTypeLabel.place(x = 0, y = 0)
backEndClass = Back_End_Helper.Create_Json()
if(backEndClass.Check_For_Json_File()== True):
    global loginData
    loginData = Login_Menu_Helper.Login_Window()
    actionData = []
    backEndClass = Back_End_Helper.Action_Mapping(loginData["roleId"])
    actionData = backEndClass.Execute_Command()
    columnNo = 0
    actionWindow = Create_Action_Window()
    actionButtonFrame = tk.Frame(actionWindow, width=600, height=30)
    actionButtonFrame.pack(padx=10, pady=10)
    actionButtonFrame.grid_propagate(False)

    actionAreaFrame = tk.Frame(actionWindow, width=600, height=300)
    actionAreaFrame.pack(padx=10, pady=10)
    actionAreaFrame.grid_propagate(False)
    Add_Action_Frame("")

    for action in actionData:
        button = tk.Button(actionButtonFrame, text=action["ActionName"], bg="#FFC1CC", command=lambda id=action["ActionID"]: Dynamic_Action(id))
        button.grid(row=0, column= columnNo, pady=2, padx=5)
        columnNo = columnNo +1
else:
    show_error("Unable to load csv files","Conversion failure")
    

actionWindow.mainloop()



