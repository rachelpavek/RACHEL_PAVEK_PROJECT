import tkinter as tk
import Login_Menu_Helper
import Back_End_Helper

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

def Add_Patient():
    def Get_Patient(frame):
        global backEndClass
        def Create_Visit_Record(addPatientSubMenuFrame):
            def Create_Record():
                global backEndClass
                print("")
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
            


        
    customActionFrame = Add_Action_Frame("Add Patient")
    patientIdLabel = tk.Label(customActionFrame, text= "Enter Patient ID: ", bg='#FFD1DC', font=("Roboto", 12))
    patientIdEntry = tk.Entry(customActionFrame, font=("Roboto", 12),)
    patientIdLabel.place(x= 5, y=5)
    patientIdEntry.place(x= 5, y=35)
    searchButton = tk.Button(customActionFrame, text="Search", bg="#C11C84", command= lambda v= customActionFrame: Get_Patient(v))
    searchButton.place(x= 70, y=65)

def Remove_Patient():
    customActionFrame = Add_Action_Frame("Remove Patient")

    

def Retrieve_Patient():
    customActionFrame = Add_Action_Frame("Retrieve Patient")

   

def Count_Visits():
    customActionFrame = Add_Action_Frame("Count Visits")
    

def View_Note():
    customActionFrame = Add_Action_Frame("View Note")
    

def Generate_Statistics():
    customActionFrame = Add_Action_Frame("Generate Statistics")
    

def Dynamic_Action(buttonId):
    global actionAreaFrame
    Clear_Frame(actionAreaFrame)
    print(f"Button with ID {buttonId} clicked!")
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
            
actionWindow = tk.Tk()
actionWindow.title("Action Window")
actionWindow.geometry('600x385')
actionWindow.configure(bg='#FC6C85')
actionWindow.resizable(False, False)

actionButtonFrame = tk.Frame(actionWindow, width=600, height=30)
actionButtonFrame.pack(padx=10, pady=10)
actionButtonFrame.grid_propagate(False)

actionAreaFrame = tk.Frame(actionWindow, width=600, height=300)
actionAreaFrame.pack(padx=10, pady=10)
actionAreaFrame.grid_propagate(False)

#customActionFrame = tk.Frame(actionAreaFrame, highlightbackground="black", bd = 1, relief="solid", width=550, height=250)
#customActionFrame.place(x=15, y=30)
#customActionFrame.place_propagate(False)

#actionTypeLabel = tk.Label(actionAreaFrame, text="Action: ", bg='#FFD1DC', font=("Roboto", 12))
#actionTypeLabel.place(x = 0, y = 0)

Add_Action_Frame("")

#loginData = Login_Menu_Helper.Login_Window()
loginData = {'username': 'DU2OEEI', 'roleId': 2}
print(loginData)
actionData = []
backEndClass = Back_End_Helper.Action_Mapping(loginData["roleId"])
actionData = backEndClass.Execute_Command()
columnNo = 0
for action in actionData:
    button = tk.Button(actionButtonFrame, text=action["ActionName"], bg="#FFC1CC", command=lambda id=action["ActionID"]: Dynamic_Action(id))
    button.grid(row=0, column= columnNo, pady=2, padx=5)
    columnNo = columnNo +1

    



