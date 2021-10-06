

# At the beginning of the program, enter this into the terminal: pip install gspread oauth2client


#time tracking program. Functions are first_scan() 
#second_scan() [this would be used in we wanted to get an exact time, both when entering and exiting]
# total_time() [same as above]
#
import scanTimer
import datetime
import json 

# Import dependencies and set up sheet:
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"] 

creds = ServiceAccountCredentials.from_json_keyfile_name("credits.json", scope)

client = gspread.authorize(creds)

# Open spreadsheet:
sheet_name = "Weight Room Spreadsheet"

sheet = client.open(sheet_name).sheet1 

data = sheet.get_all_records()
# Find the student based on their ID:

index = 0
#Tracking Dictionaries 
trackingDict = {}

for row in data:
  trackingDict[row['Person ID']] = [False, 0]


running = True

while running == True:
  currentTime = datetime.datetime.now()
  currentTime = "{}".format(currentTime)

  ## We need to iterate through the dictionary and put the conditional below in the loop.
  for id in trackingDict:
    if trackingDict[id][0] == True:
      if int(currentTime[11:13]) - int(trackingDict[id][1]) >=3:
        trackingDict[id] = [False, 0]
    
  student_id = int(input("Student ID: "))

  for entry in data:
    if entry['Person ID'] == student_id:
      if trackingDict[student_id][0] == False:
        index = data.index(entry)
        firstScan = datetime.datetime.now()
        firstScan = "{}".format(firstScan)
        startingHour = firstScan[11:13]
        trackingDict[student_id][1] = startingHour
        trackingDict[student_id][0] = True
        
        index += 2
        # Update the student's total hours:
        total_credits = sheet.cell(index, 4).value 
        sheet.update_cell(index, 4, int(total_credits) + 1) 
        break
