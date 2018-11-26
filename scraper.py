import requests
import json

baseUrl = 'https://www.thebluealliance.com/api/v3'

year = "2018"

config = json.loads(open("config.properties", "r").read())

authKey = config['authKey']

#all teams data
teams = []

#get all teams
#continue forever until it reaches the end of the robots
pageNum = 0
#only to 5 now for testing
while pageNum < 5:
    headers = {'X-TBA-Auth-Key': authKey}
    teams.extend(requests.get(baseUrl + "/teams/" + year + "/" + str(pageNum), headers=headers).json())
    pageNum += 1

print(teams)