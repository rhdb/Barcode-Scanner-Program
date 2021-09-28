

# At the beginning of the program, enter this into the terminal: pip install gspread oauth2client


#time tracking program. Functions are first_scan() 
#second_scan() [this would be used in we wanted to get an exact time, both when entering and exiting]
# total_time() [same as above]
#
import scanTimer


# Import dependencies and set up sheet:
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"] 

creds = ServiceAccountCredentials.from_json_keyfile_name("credits.json", scope)

client = gspread.authorize(creds)

# Open spreadsheet:
sheet_name = "Weight Room Spreadsheet"

sheet = client.open(sheet_name).sheet1 

# Get sheet:
data = sheet.get_all_records()

# Find the student based on their ID:
student_id = 54527 # Milo Banks

#Scanned Before?
trackingTime=False


for entry in data:
  if entry['Person ID'] == student_id:
    if trackingTime==True:
      index = data.index(entry)
      break
    
    elif trackingTime==False:
      trackingTime=True
      startingTime=datetime.datetime.now()
      startingTime="{}".format(startingTime)
      startingHour1= startingTime[10:13]
      startingMin1 = startingTime[14:16]
      startingHour1=int(startingHour1)-6

    # There should never be an instance in which the student ID isn't found because we are scraping the google sheet and there isn't a way for a student ID to be entered incorrectly.

index += 2

# Update the student's total hours:

workout_hours = 1 # Change this value accordingly.
total_hours = sheet.cell(index,4).value 

sheet.update_cell(index, 4, int(total_hours) + workout_hours)
trackingTime= False