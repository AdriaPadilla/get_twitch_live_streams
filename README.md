# Get all TWITCH live streams for a language
This is a clean, fast and simple script to get all live streams on Twitch and save data to a .csv file. You'll need a "client ID" and "client secret token" for API auth. Please, visit [Twitch Developers page](https://dev.twitch.tv/). 

**Info**

You can define up to 100 languages to get all streams on Twitch within this language. See list of langs in line 12.

**The Script**

See [main.py](https://github.com/AdriaPadilla/get_twitch_live_streams/blob/main/main.py)

**Important**
- To avoid overflow Twich API rate limits, don't modify time.sleep(0.12). 
- This **script uses twitchAPI V2.5.7.1**. You **must** install this specific version of the library:
```bash
pip install twitchAPI==2.5.7.1
```

**Docs**
- TwitchAPI Docs V2.5.7.1: [get_streams()](https://pytwitchapi.readthedocs.io/en/v2.5.7/modules/twitchAPI.twitch.html#twitchAPI.twitch.Twitch.get_streams)
- Twitch Official API Docs: [Get Streams](https://dev.twitch.tv/docs/api/reference/#get-streams)

**Academic paper**

[Audiences and streamers on Twitch: consumption and production patterns in the Spanish-speaking world](https://www.cac.cat/sites/default/files/2022-11/Q48_Padilla_Navarro_EN.pdf)

Citation (APA): Padilla Molina, A. & Navarro Bosch, C. (2022). "Audiences and streamers on Twitch: consumption and production patterns". Quaderns del CAC 25(48), p.67-77. https://ddd.uab.cat/record/268821
