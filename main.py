# NOTE: All of our code will need to be put into a "while True" loop once we finish with it.

# At the beginning of the program, enter this into the terminal: pip install gspread oauth2client



######## TIME STAMPING AND BARCODE READING WORK ########



########## SPREADSHEET WORK ##########


## NOTE: WE WILL NEED TO CHANGE THE credits.json FILE AND THE sheet_name VARIABLE TO GET THE PROGRAM TO WORK AS WE WANT IT TOO. WE WILL ALSO NEED TO CHANGE THE SHEET AND IT'S SHARING PERMISSIONS SO THAT IT IS SHARED WITH THIS EAMIL: tech-club@techclubtest.iam.gserviceaccount.com. ##


#time tracking program. Functions are first_scan() 
#second_scan() [this would be used in we wanted to get an exact time, both when entering and exiting]
# total_time() same as above
#
import scanTimer


# Import dependencies and set up sheet:
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"] 

creds = ServiceAccountCredentials.from_json_keyfile_name("credits.json", scope) # Going to need to change JSON file.

client = gspread.authorize(creds)

# Open spreadsheet:
sheet_name = "Copy of Weight Room Spreadsheet" # Going to need to change the sheet name.

sheet = client.open(sheet_name).sheet1 

# Get sheet:
data = sheet.get_all_records()

# Find the student based on their ID:
student_id = 54527 # Milo Banks

for entry in data:
  if entry['Person ID'] == student_id:
    index = data.index(entry)
    break
    # There should never be an instance in which the student ID isn't found because we are scraping the google sheet and there isn't a way for a student ID to be entered incorrectly.

index += 2

# Update the student's total hours:

workout_hours = 0 # Change this value accordingly.
total_hours = sheet.cell(index,4).value 

sheet.update_cell(index, 4, int(total_hours) + workout_hours)