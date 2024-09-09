import json


teams = []
with open('esport-data/teams.json') as f:
    teams = json.load(f)

def get_team_by_id(team_id):
    for team in teams:
        if team['id'] == team_id:
            return team
        
leaugues = []
with open('esport-data/leagues.json') as f:
    leaugues = json.load(f)

def get_league_by_id(league_id):
    for league in leaugues:
        if league['league_id'] == league_id:
            return league

players = []
with open('esport-data/players.json', encoding="utf8") as f:
    players = json.load(f)


def enrich_player_data(player):
    #team data
    team = get_team_by_id(player["home_team_id"])
    player["team"] = team["name"]

    # league data
    league = get_league_by_id(team["home_league_id"])
    player["league"] = league["name"]
    player["region"] = league["region"]

    #remove fields
    del player["home_team_id"]
    del player["photo_url"]

    return player

player_data = [enrich_player_data(player) for player in players]

for p in player_data:
    print(p)

with open('esport-data/players.csv', 'a', encoding="utf8") as f:
    f.write("id,handle,first_name,last_name,team_name,team_acronym,league,region")
    for player in player_data:
        csv_data = f"{player['id']},{player['handle']},{player['first_name']},{player['last_name']},{player['team']},{player['team']},{player['league']},{player['region']}"
        # print with utf-8 encoding
        with open('esport-data/players.csv', 'a', encoding="utf8") as f:
            f.write(csv_data + "\n")