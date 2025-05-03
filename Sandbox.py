import CSV_To_JSON_Converter

csvFilePaths = ["C:\\Users\\lexi7\\Downloads\\PA3_Notes.csv", "C:\\Users\\lexi7\\Downloads\\PA3_data.csv", "C:\\Users\\lexi7\\Downloads\\PA3_credentials.csv" ]

jsonFilePaths = [".//PRSLoginCredentials.json", ".//PRSPatientData.json"]

CSV_To_JSON_Converter.Convert_CSV_To_JSON(csvFilePaths, jsonFilePaths)
