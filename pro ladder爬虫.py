# -*- coding: utf-8 -*-


import requests
import numpy as np
 
factions = ['Monsters', 'Skellige', 'N. Realms', 'Scoia&#039;tael', 'Nilfgaard']
scores = {faction:[] for faction in factions}
num_pages = 300
min_games = 20
 
def get_page(num):
    text = requests.get(f'https://masters.playgwent.com/en/rankings/pro-ladder/{num}').text
    return text.split('class="btn">Next</a></div></div></div></div>')[0]
 
def get_players(text):
    return text.split('<div class="c-ranking-details">')[1:]
 
def parse_player(text):
    for faction in factions:
        text, faction_text = text.split(faction)
        score = parse_faction_score(faction_text)
        if score != 0:
            games = parse_faction_games(faction_text)
            scores[faction].append((games, score))
 
 
def parse_faction_games(faction_text):
    faction_text = faction_text.split(' matches</span>')[0]
    faction_text = faction_text.split('</strong><span>')[1]
    faction_text = faction_text.split('/')[0]
    return int(faction_text)
 
def parse_faction_score(faction_text):
    if "Real score:" not in faction_text:
        pre = '<div class="c-ranking-details__content"><strong>'
        post = '</strong><span>'
    else:
        pre = 'Real score:</span><strong>'
        post = '</strong></div>'
    return int(faction_text.split(pre)[1].split(post)[0].replace(',',''))
 
pages = [get_page(n) for n in range(num_pages)]
 
for page in pages[0:10]:    
    players = get_players(page)
    for player in players:
        parse_player(player)
 
import datetime
print(f'Updated: {datetime.datetime.now()}')
 
print("Percentage of total games by faction (no minimum)")
print('Faction|Percentage of Total Games')
print(':--|:--')
total_games_by_faction = {f:0 for f in factions}
for k, v in scores.items():
    s = int(np.mean([score[1] for score in v]))
    N = np.sum([score[0] for score in v])
    total_games_by_faction[k] = N
   
divisor = np.sum([v for v in total_games_by_faction.values()])
 
for k, v in total_games_by_faction.items():
    p = round(total_games_by_faction[k] / divisor, 3)
    print(f'{k.replace("&#039;","")}|{p}')
 
print('Faction|Average fMMR|Total Games')
print(':--|:--|:--')
for k, v in scores.items():
    s = int(np.mean([score[1] for score in v if score[0] > min_games]))
    N = np.sum([score[0] for score in v if score[0] > min_games])
    print(f'{k.replace("&#039;","")}|{s}|{N}')
 
ys = {f:[] for f in factions}
for min_games in np.arange(50):
    for k, v in scores.items():
        s = int(np.mean([score[1] for score in v if score[0] > min_games]))
        N = np.sum([score[0] for score in v if score[0] > min_games])
        ys[k].append(s)        
 
