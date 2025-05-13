PRS is a GUI medical record system that is built using Python. The main python application used to make this GUI is tkinter. PRS is designed to make sure that a hospitals database has a secure login window. Inside of the login window it lets users with the right credentials to be able to add new patients, remove patients, retrieve patients, view patient notes, and also generating patient record statistics. PRS uses JSON files to capture and manage patient and user credential data.

##Command Line for CMD terminal
python RACHEL_PAVEK_PROJECT.py 

##Usage

The GUI when launched through the main file of RACHEL_PAVEK_PROJECT.py buttons will only work based on the users role ID and the actions that they can perform with that ID
-Add Patient: User will input a new patients record details and also note information
-Remove patient will delete a record with the patient ID that the user provides
Retrieve patient will retrieve all patients information like gender, age, race, ethnicity, and insurance
-View note will find additional note data where the user inputs a patient ID and data
-Generate Statistics PRS statistic information will show a the user a statistic of all patient information that is inside of the system

##Documentation
Main file to be used is RACHEL_PAVEK_PROJECT.py

Main functions are:
Add_Patient():
Remove_Patient():
Retrieve_Patient():
Count_Visits():
View_Note():
Generate_Statistics():

##Dependencies
-tkinter
-json
-datetime
-os
-Record_Helper
-CSV_To_JSON_Converter
-File_Helper
-General_Helper


##PRS uses three JSON files
-PRSLoginCredentials.json the data inside of this JSON file is user credentials, roles, and system action mappings
-PRSPatientData.JSON the data inside of this JSON file is all patient, visit, and additional note records
-PRSUsageStatistics this JSON file will capture data for the usage of the users with designated roles and will keep track of their actions and the time that they performed that action and also keep track of what time they logged in


##Contributors
Rachel Pavek - Developer of PRS # RACHEL_PAVEK_PROJECT
Easy to use user interface for a clinical data warehouse
