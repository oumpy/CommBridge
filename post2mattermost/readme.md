# post2mattermost

Takes plain text information and posts it to a designated Mattermost channel.
It can handle multiple texts separated by the escape sequence `\v`.

## Initial Setup

1. Obtain a Mattermost API token from your Mattermost server.
2. Place this token into a file named `mm_token.json` in the `$HOME/.post2mattermost/` directory.
3. Add your Mattermost server URL and port number to a `config.yaml` file in the same directory.

```yaml
server_url: "http://localhost"
port: 8065
api_token: "your_api_token_here"
team_name: "your_team_name_here"
channel_name: "your_channel_name_here"
```

4. Run the script to validate the settings.

## Usage

The script accepts emails in plain text format separated by \v from stdin:

```bash
$ cat messages.txt | emails2mattermost
```

## Input Format

The script expects multiple texts to be separated by the escape sequence \v.

## Copyright & License

@2023 AtamaokaC  
Python Party of Osaka University Medical School, Japan

License: GNU General Public License v3
