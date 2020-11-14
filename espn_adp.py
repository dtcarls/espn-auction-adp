import urllib.request
import json 
import csv

with urllib.request.urlopen("https://fantasy.espn.com/apis/v3/games/ffl/seasons/2020/segments/0/leaguedefaults/3?view=kona_player_info") as url:
    data = json.loads(url.read().decode())

with open('adp.txt','w') as outfile:
    json.dump(data,outfile)

with open('adp.txt') as json_file:
    with open('aucionval.csv', mode='w') as auction_file:
        auction_file.write("Name,Value")
        auction_file.write('\n')
        data = json.load(json_file)
        for person in data['players']:
            if person['player']['ownership']['auctionValueAverage'] > 1:
                auction_file.write(person['player']['fullName']+","+str(person['player']['ownership']['auctionValueAverage']))
                auction_file.write('\n')