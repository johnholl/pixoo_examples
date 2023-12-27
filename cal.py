import datetime
import googleapiclient.discovery
import google.auth
from pixoo import Pixoo

# figure out your PIXOOs ip address
PIXOO_IP = '192.168.1.128'

# replace with calendar of your choice
CALENDAR_ID = 'jholler423@gmail.com'

pixoo = Pixoo(PIXOO_IP, 64, True)
 
# Preparation for Google API
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


calendar_id = 'jholler423@gmail.com'

# follow steps to create a service account on GCP, enable calendar api, copy in credentials. Also don't forget to give permissions to the service account on the calendar
gapi_creds = google.auth.load_credentials_from_file('credentials.json', SCOPES)[0]

service = googleapiclient.discovery.build('calendar', 'v3', credentials=gapi_creds)
 
# Get events from Google Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z'
events_result = service.events().list(
     calendarId=CALENDAR_ID, timeMin=now,
     maxResults=3, singleEvents=True,
     orderBy='startTime').execute()
 
# Pick up only start time, end time and summary info
events = events_result.get('items', [])
 
i = 0
for event in events:
    start = datetime.datetime.strptime(event['start'].get('dateTime', event['start'].get('date')), '%Y-%m-%d')
    days_until = (start - datetime.datetime.now()).days
    if days_until < 10:
        color = (255, 0, 0)
    else:
        color = (255, 255, 255)
              
    pixoo.draw_text(event['summary'] + ":", (0, i*20), color)
    pixoo.draw_text(str(days_until) + " days", (0, i*20 + 8), color)
    pixoo.draw_text("-----------------------------", (0, i*20 + 14), (255, 255, 255))

    i+= 1

pixoo.push()    
