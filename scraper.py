import requests
import json

baseUrl = 'https://www.thebluealliance.com/api/v3'

year = "2018"

config = json.loads(open("config.properties", "r").read())

authKey = config['authKey']

headers = {'X-TBA-Auth-Key': authKey}

#all teams data
teams = []

#get all teams
#continue until it reaches the end of the robots that exist
pageNum = 0
while pageNum < 1:
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


def getEventData(teamKey, eventKey):
    eventData = requests.get(baseUrl + "/team/" + teamKey + "/event/" + eventKey + "/status", headers=headers).json()
    return eventData

teamWorldsRank = []
teamEventData = []
teamHighestRank = []
#true or false
teamWorlds = []
teamEinstiens = []

for team in teams:
    events = requests.get(baseUrl + "/team/" + team['key'] + "/events/" + year + "/keys", headers=headers).json()
    worlds = False
    einstien = False
    worldsRank = -1
    allEventData = []
    highestRank = -1
    for event in events:
        eventData = getEventData(team['key'], event)
        allEventData.append(eventData)
        #normal worlds
        if (event.startswith("2018dal") or event.startswith("2018arc") or event.startswith("2018cars") or event.startswith("2018cur") or event.startswith("2018dar") or event.startswith("2018tes") or event.startswith("2018tur") or event.startswith("2018new") or event.startswith("2018roe") or event.startswith("2018hop") or event.startswith("2018gal") or event.startswith("2018carv")):
            worlds = True
            worldsRank = eventData['qual']['ranking']['rank']
        #einstein
        elif (event.startswith("2018cmp")):
            einstien = True
        else (eventData['qual']['ranking']['rank'] < highestRank or highestRank == -1):
            highestRank = eventData['qual']['ranking']['rank']
    teamWorlds.append(worlds)
    teamWorldsRank.append(worldsRank)
    teamEventData.append(allEventData)
    teamHighestRank.append(highestRank)

# f = open("data.csv","w+")

# for i in range(len(teams)):
#     f.write()