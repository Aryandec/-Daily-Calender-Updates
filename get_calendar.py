import datetime
import os.path
import pywhatkit

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_todays_events():
    creds = None
   
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        target_calendar_id = "primary" # Change this to your specific calendar ID if needed    

        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        
        print("Fetching today's events...\n")
        events_result = service.events().list(
            calendarId=target_calendar_id, timeMin=now,
            maxResults=10, singleEvents=True,
            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found for today.')
            return "No events today! Relax."

        message = "📅 *Good Morning! Here is your schedule for today:*\n\n"
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            
            if 'T' in start:
                time_only = start.split('T')[1][:5]
            else:
                time_only = "All Day"
                
            message += f"• {time_only} - {event['summary']}\n"
            
        print(message)
        return message

    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == '__main__':
    agenda = get_todays_events()
    
    if agenda:
        print("Opening WhatsApp Web to send the message...")
        
        # Add your phone number here! Must include the country code
        my_phone_number = "+91XXXXXXXXXX"  
        
        pywhatkit.sendwhatmsg_instantly(
            phone_no=my_phone_number,
            message=agenda,
            wait_time=15,    
            tab_close=True,  
            close_time=3     
        )
        print("Message sent successfully!")