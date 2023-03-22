# Get all live streams for a language
This is a clean, fast and simple script to get all live streams on Twitch and save data to a .csv file. You'll need a "client ID" and "client secret token" for API auth. Please, visit [Twitch Developers page](https://dev.twitch.tv/). 

**Important**
- To avoid overflow Twich API rate limits, don't modify time.sleep(0.12). 
- This script uses twitchAPI V2.5.7.1. You must install this specific version of the library:
```bash
pip install twitchAPI==2.5.7.1
```
- TwitchAPI Docs V2.5.7.1: [Read The Docs](https://pytwitchapi.readthedocs.io/en/v2.5.7/modules/twitchAPI.twitch.html)
- Twitch Official API Docs: [Read The Docs](https://dev.twitch.tv/docs/)
