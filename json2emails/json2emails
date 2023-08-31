#!/usr/bin/env python3

# json2emails.py
# @2023 AtamaokaC
# Python Party of Osaka University Medical School, Japan
# License: GNU General Public License v3

import json
import sys

def main():
    json_data = json.load(sys.stdin)
    emails_text = []

    for email in json_data:
        email_text = []
        email_text.append(f"Date: {email['date']}")
        email_text.append(f"From: {email['from']}")
        email_text.append(f"To: {email['to']}")
 
        if 'cc' in email and email['cc']:
            email_text.append(f"Cc: {email['cc']}")

        email_text.append(f"Subject: {email['subject']}")
        email_text.append(email['body'].replace("\v", "\n"))

        emails_text.append("\n".join(email_text))

    print("\v".join(emails_text))

if __name__ == "__main__":
    main()
