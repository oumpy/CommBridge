import os
import json
import datetime
import sys
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_service(token_path, creds_path):
    creds = None
    if os.path.exists(token_path):
        with open(token_path, 'r') as token:
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def main():
    home_dir = os.path.expanduser("~")
    token_path = os.path.join(home_dir, ".fetchgmail", "token.json")
    creds_path = os.path.join(home_dir, ".fetchgmail", "credentials.json")
    last_time_path = os.path.join(home_dir, ".fetchgmail", "last_received_time.json")

    # Initialize Gmail API
    service = get_service(token_path, creds_path)

    try:
        with open(last_time_path, 'r') as f:
            last_received_time = json.load(f).get('last_received_time', '')
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("Invalid or missing last_received_time.json. Fetching will be skipped. Resetting to current time.", file=sys.stderr)
        last_received_time = str(int(datetime.datetime.utcnow().timestamp() * 1000))
        with open(last_time_path, 'w') as f:
            json.dump({'last_received_time': last_received_time}, f)
        return

    query = f"after:{int(last_received_time)//1000}"
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])

    all_messages = []
    if messages:
        for msg_id in messages['messages']:
            msg = service.users().messages().get(userId='me', id=msg_id['id'], format='full').execute()
            all_messages.append(msg)

        last_received_time = max(message['internalDate'] for message in all_messages)
        with open(last_time_path, 'w') as f:
            json.dump({'last_received_time': last_received_time}, f)

    print(json.dumps(all_messages, indent=4))

if __name__ == '__main__':
    main()
