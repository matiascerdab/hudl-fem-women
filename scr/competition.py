import pandas as pd
from statsbombpy import sb

target_leagues=[
    {'competition_id': 37,'season_id':281},
    #{'competition_id':131,'season_id':281},
    #{'competition_id':135,'season_id':281},
    #{'competition_id':182,'season_id':281},
    #{'competition_id':49,'season_id':107},
    ]

all_matches=[]

for league in target_leagues:
    matches_df=sb.matches(competition_id=league['competition_id'],season_id=league['season_id'])
    all_matches.append(matches_df)

combined_matches=pd.concat(all_matches,ignore_index=True)

#print(combined_matches.head(10))

all_events=[]
id_match_ex=list([3913082,3913155])

#for match_id in combined_matches['match_id']:
for match_id in id_match_ex:
    try:
        match_events=sb.events(match_id=match_id)
        all_events.append(match_events)
    except Exception as e:
        print(f'Error fetching match {match_id}: {e}')

combined_events=pd.concat(all_events,ignore_index=True)

#print(combined_events.info())
#print(combined_events.head(10))

print(combined_events['ball_receipt_outcome'].dropna().unique())