# At the beginning of the program, enter this into the terminal: pip install gspread oauth2client

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


# NOTE: WE WILL NEED TO CHANGE THE credits.json FILE AND THE sheet_name VARIABLE TO GET THE PROGRAM TO WORK AS WE WANT IT TOO.

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credits.json", scope)

client = gspread.authorize(creds)

# Open spreadsheet:
sheet_name = "Copy of Weight Room Spreadsheet"
sheet = client.open(sheet_name).sheet1 

# Full sheet:
data = sheet.get_all_records()

stud_id = 54527

for entry in data:
  if entry['Person ID'] == stud_id:
    index = data.index(entry)



##row = sheet.row_values(5)  # Get a specific row 
##col = sheet.col_values(1)  # Get a specific column

# Get a specific cell value:
cell = sheet.cell(2,1).value  
# Note that the first value in the coordinate pair above stands for the columns (so the cell takes column 1) while the second value stands for the row (so the cell also takes column 1).

##### sheet.update_cell(2,10, int(cell) + hours) ## The cell specified now holds the value cell + hours



''''
# Add row (adds the row to the end of the sheet):
insertRow = ["hello", 5, "red", "blue"]
sheet.append_row(insertRow) # Adds the values stored in insertRow


numRows = sheet.row_count  # Get the number of rows in the sheet
'''