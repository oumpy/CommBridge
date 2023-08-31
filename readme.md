# CommBridge

A modular toolset designed to fetch, convert, and post email messages from various sources to different communication platforms.
Initially supporting Gmail and Mattermost.

## Usage Example

You can pipe the outputs of these scripts as follows:

```bash
$ fetchgmail | json2emails | emails2mattermost
```

## Components

- **fetchgmail**: Fetches emails from a Gmail account
- **json2emails**: Converts JSON email data to plain text
- **emails2mattermost**: Posts plain text emails to a Mattermost channel

## Installation and Configuration

1. Clone the repository.
2. Follow the setup instructions for each script, located in their respective directories.
3. Install required Python packages, usually listed in a `requirements.txt` file.

### Copyright & License
@2023 AtamaokaC  
Python Party of Osaka University Medical School, Japan

License: GNU General Public License v3
