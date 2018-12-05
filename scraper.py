import requests
import json

baseUrl = 'https://www.thebluealliance.com/api/v3'

year = "2018"

config = json.loads(open("config.properties", "r").read())

authKey = config['authKey']

#all teams data
teams = []

#get all teams
#continue until it reaches the end of the robots that exist
pageNum = 0
while pageNum < 1:
    headers = {'X-TBA-Auth-Key': authKey}
    pulledData = requests.get(baseUrl + "/teams/" + year + "/" + str(pageNum), headers=headers).json();
    if len(pulledData) == 0:
        break
    teams.extend(pulledData)
    pageNum += 1


#get amount of championship wins this team has gotten
#this data is recieved from grabbing the awards from tha apo
#dictionary of number of wins
teamWins = []
teamFinalists = []
teamChairmans = []
#total awards
teamAwards = []

#Find wins from teams
for team in teams:
    headers = {'X-TBA-Auth-Key': authKey}
    awards = requests.get(baseUrl + "/team/" + team['key'] + "/awards", headers=headers).json()
    wins = 0
    finalists = 0
    chairmans = 0
    totalAwards = 0
    for award in awards:
        #only count 2018 data
        if award['year'] == 2018:
            if award['award_type'] == 1:
                wins += 1
            if award['award_type'] == 2:
                finalists += 1
            if award['award_type'] == 0:
                chairmans += 1
            totalAwards += 1
    teamWins.append(wins)
    teamFinalists.append(finalists)
    teamChairmans.append(chairmans)
    teamAwards.append(totalAwards)

#true or false
teamWorlds = []

for team in teams:
    headers = {'X-TBA-Auth-Key': authKey}
    events = requests.get(baseUrl + "/team/" + team['key'] + "/events/2018/keys", headers=headers).json()
    worlds = False
    for event in events:
        if (event.startswith("2018cmp")):
            worlds = True
            break
    teamWorlds.append(worlds)

# f = open("data.csv","w+")

# for i in range(len(teams)):
#     f.write()