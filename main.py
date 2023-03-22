from twitchAPI.twitch import Twitch
import datetime
import pandas as pd
import time

now = datetime.datetime.now() # Get the actual date and time to know when you make the API request.

# Define your Twitch API credentials
twitch = Twitch('app_id', 'secret')

# Define a list of langs to limit your query to certain language.
langs = ["es","ca"]
cursor_dummy = None # This is a Dummy variable used on the first API query.

llista_dataframes = [] # Each API query loop will be saved in this list

# Main Function
def query(cursor, lang):
  
    # Max items on get_streams = 100. Loop needed to get all using cursor
    streams = twitch.get_streams(first=100, language=lang, after=cursor) # Funció "get_streams()"
    dades = streams["data"] 

    for dada in dades: 
        captured_at = now
        user_id = dada["user_id"]
        user_name = dada["user_name"]
        game_id = dada["game_id"]
        game_name = dada["game_name"]
        title = dada["title"]
        viewer_count = dada["viewer_count"]
        started_at = dada["started_at"]
        is_mature = dada["is_mature"]
        language = dada["language"]

        # Les dades de la variable, les volquem en un dataframe.
        df = pd.DataFrame({
            "captured_at": captured_at,
            "user_id": user_id,
            "user_name": user_name,
            "game_id": game_id,
            "game_name": game_name,
            "title": title,
            "viewer_count": viewer_count,
            "started_at": started_at,
            "is_mature":is_mature,
            "lang": language,
        }, index=[0])
        llista_dataframes.append(df)
        
    try:
        cursor = streams["pagination"]["cursor"] # Get pagination cursor
        print(f"New API request: {lang} - Total Streams: {len(llista_dataframes)}")
        time.sleep(0.12)
        query(cursor, lang)

    # Last page exception
    except KeyError:
      
        print("Last Page")
        print(f"Total Captured Streams {len(llista_dataframes)}")
        pass

for lang in langs:
  
    llista_dataframes.clear() # Clean All lists in each lang loop!
    query(cursor_dummy, lang)

    # Data export for each lang
    
    final_dataframe = pd.concat(llista_dataframes)
    final_dataframe.to_csv(f"twitch-live-export_{lang}.csv", index=False)
