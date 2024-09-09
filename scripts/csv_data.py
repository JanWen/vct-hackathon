import json

teams = []
with open('esport-data/teams.json') as f:
    teams = json.load(f)

def get_team_by_id(team_id):
    for team in teams:
        if team['id'] == team_id:
            return team


players = []
with open('esport-data/players.json', encoding="utf8") as f:
    players = json.load(f)


with open('esport-data/players.csv', 'a', encoding="utf8") as f:
    f.write("id,handle,first_name,last_name,team_name,team_acronym")
for player in players:
    team_id = player['home_team_id']
    team = get_team_by_id(team_id)
    team_name = team['name']
    team_acronym = team['acronym']

    csv_data = f"{player['id']},{player['handle']},{player['first_name']},{player['last_name']},{team_name},{team_acronym}"
    # print with utf-8 encoding
    with open('esport-data/players.csv', 'a', encoding="utf8") as f:
        f.write(csv_data + "\n")