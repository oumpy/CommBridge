#!/usr/bin/env python3

# emails2mattermost.py
# @2023 AtamaokaC
# Python Party of Osaka University Medical School, Japan
# License: GNU General Public License v3

import requests
import yaml
import sys
import os

def main():
    # Load YAML configuration file
    with open(os.path.expanduser("~/.emails2mattermost/config.yaml"), "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    server_url = config.get("server_url", "http://localhost")
    port = config.get("port", 8065)
    api_token = config["api_token"]
    team_name = config["team_name"]
    channel_name = config["channel_name"]

    base_url = f"{server_url}:{port}/api/v4"
    headers = {"Authorization": f"Bearer {api_token}"}

    # Get team ID from team name
    response = requests.get(f"{base_url}/teams/name/{team_name}", headers=headers)
    if response.status_code != 200:
        print(f"Failed to get team ID: {response.json().get('message')}", file=sys.stderr)
        return
    team_id = response.json()["id"]

    # Get channel ID from channel name
    response = requests.get(f"{base_url}/teams/{team_id}/channels/name/{channel_name}", headers=headers)
    if response.status_code != 200:
        print(f"Failed to get channel ID: {response.json().get('message')}", file=sys.stderr)
        return
    channel_id = response.json()["id"]

    emails_text = sys.stdin.read().split("\v")

    for email in emails_text:
        payload = {'channel_id': channel_id, 'message': email}
        response = requests.post(f"{server_url}:{port}/api/v4/posts", headers=headers, json=payload)
        if response.status_code != 201:
            print(f"Failed to post message: {response.content}")

if __name__ == "__main__":
    main()
