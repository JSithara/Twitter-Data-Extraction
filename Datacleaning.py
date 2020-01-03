import pandas as pd
import json


# f = "twit.csv"

# df = pd.read_csv(f)
f = "twitDB.json"

df = pd.read_json(f)
#print(df.head())
print(df.columns)
user = df.loc[:,'user']
df = df.drop(columns = ['contributors', 'coordinates', 'display_text_range', 'entities', 'extended_entities', 'extended_tweet',
'favorited', 'filter_level', 'geo', 'in_reply_to_screen_name', 'in_reply_to_status_id', 'in_reply_to_status_id_str',
'in_reply_to_user_id', 'is_quote_status', 'lang', 'place', 'possibly_sensitive', 'quoted_status', 'quoted_status_id',
'quoted_status_id_str', 'quoted_status_permalink', 'retweeted_status','source', 'retweeted', 'timestamp_ms', 'truncated','user'])

userData = pd.DataFrame(user.values)
UID = []
name = []
location = []
for userInfo in userData[0]:
    UID.append(userInfo['id'])
    location.append(userInfo['location'])
    name.append(userInfo['name'])

df = df.assign(name=name)
df = df.assign(location=location)
df = df.assign(UID=UID)
df["text"]=df["text"].replace(r'[^\x00-\x7F]+', '', regex=True).replace(r'http\S+', '', regex=True).replace(r'www\S+', '', regex=True).str.replace('[^A-Za-z\s]+','').str.replace('\n', '').str.replace('<[^<]+?>', '')
df['name'] = df['name'].replace(r'[^\x00-\x7F]+', '', regex=True).str.replace('[^A-Za-z\s]+','')
df['location'] = df['location'].replace(r'[^\x00-\x7F]+', '', regex=True).str.replace('[^A-Za-z\s]+','')
print(df.head())
df.to_csv("tweetlatest.csv")



