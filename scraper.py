import requests
from bs4 import BeautifulSoup
import pandas as pd

test_file_name = 'table.txt'
test_boxscore_url = 'https://www.espn.com/mlb/boxscore/_/gameId/401471565'

def generate_team_mapping_csv():
    teams_url = "http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/teams"

    with open('team_mapping.csv', 'w') as csv:
        csv.write('Display Name,Abbreviation\n')
    
    response = requests.get(teams_url)
    data = response.json()

    for team in data['sports'][0]['leagues'][0]['teams']:
        # write displayName and abbreviation to csv
        displayName = team['team']['displayName']
        abbreviation = team['team']['abbreviation']
        
        with open('team_mapping.csv', 'a') as csv:
            csv.write(displayName + ',' + abbreviation + '\n')

def get_game_ids():
    scoreboard_url = "http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"

    response = requests.get(scoreboard_url)
    data = response.json()

    game_ids = []

    for event in data['events']:
        game_ids.append(event['id'])

    return game_ids

def save_boxscore_tables(game_id):
    url = f'https://www.espn.com/mlb/boxscore/_/gameId/{game_id}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    tables = soup.find_all('table')

    with open(test_file_name, 'w') as f:
        f.write('Test box score output\n\n')

    for i, table in enumerate(tables):
        if i == 0:
            continue
        elif i == 10:
            break

        columns = [th.text for th in table.find('tr').find_all('th')]

        data_rows = table.find_all('tr')[1:]
        data = [[td.text for td in row.find_all('td')] for row in data_rows]

        df = pd.DataFrame(data, columns=columns)
        print(df)
        print()

        # write the df to a single text file as previous iterations and do not overwrite
        with open(test_file_name, 'a') as f:
            f.write(df.to_string())
            f.write('\n\n')

if __name__ == "__main__":
    save_boxscore_tables('401471565')
    game_ids = get_game_ids()
    print(game_ids)