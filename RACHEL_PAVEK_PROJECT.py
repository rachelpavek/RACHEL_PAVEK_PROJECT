import tkinter as tk
import Login_Menu_Helper
import Back_End_Helper

def Clear_Action_Area_Frame():
    global actionAreaFrame
    for widget in actionAreaFrame.winfo_children():  # Get all child widgets
        widget.destroy()

def Add_Patient():
    global actionAreaFrame
    addPatientLabel = tk.Label(actionAreaFrame, text="Add Patient", bg='#FFD1DC', font=("Roboto", 12))
    addPatientLabel.place(x = 0, y = 0)
   

def Remove_Patient():
    global actionAreaFrame
    removePatientLabel = tk.Label(actionAreaFrame, text="Remove Patient", bg='#FFD1DC', font=("Roboto", 12))
    removePatientLabel.place(x = 0, y = 0)

def Retrieve_Patient():
    global actionAreaFrame
    retrievePatientLabel = tk.Label(actionAreaFrame, text="Retrieve Patient", bg='#FFD1DC', font=("Roboto", 12))
    retrievePatientLabel.place(x = 0, y = 0)

def Count_Visits():
    global actionAreaFrame
    countVisitsLabel = tk.Label(actionAreaFrame, text="Count Visits", bg='#FFD1DC', font=("Roboto", 12))
    countVisitsLabel.place(x = 0, y = 0)

def View_Note():
    global actionAreaFrame
    viewNoteLabel = tk.Label(actionAreaFrame, text="View Note", bg='#FFD1DC', font=("Roboto", 12))
    viewNoteLabel.place(x = 0, y = 0)

def Generate_Statistics():
    global actionAreaFrame
    generateStatisticsLabel = tk.Label(actionAreaFrame, text="Generate Statistics", bg='#FFD1DC', font=("Roboto", 12))
    generateStatisticsLabel.place(x = 0, y = 0)

def Dynamic_Action(buttonId):
    Clear_Action_Area_Frame()
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

    



