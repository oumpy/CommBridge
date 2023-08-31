# fetchgmail

Fetches new emails from a Gmail account and outputs them in JSON format.

## Initial Setup

1. Go to the [Google Developers Console](https://console.developers.google.com/).
2. Create a new project and enable the Gmail API.
3. Download the `credentials.json` file and place it in the `$HOME/.fetchgmail/` directory.
4. Run `fetchgmail` once to complete the authentication process.
This will generate a `token.json` and `last_received_time.json` files in `$HOME/.fetchgmail/`.

## Usage

Run the script without any arguments:

```bash
$ fetchgmail
```

### Options

#### --include-sent

Include this flag to also fetch sent emails alongside the received ones.

```bash
$ fetchgmail --include-sent
```

## Copyright & License
@2023 AtamaokaC  
Python Party of Osaka University Medical School, Japan

License: GNU General Public License v3
