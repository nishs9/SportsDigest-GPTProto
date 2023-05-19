import requests
from bs4 import BeautifulSoup
import pandas as pd

# Retrieves the ESPN game id of all finished MLB games of the current day
def get_completed_games():
    scoreboard_url = "http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"

    response = requests.get(scoreboard_url)
    data = response.json()

    game_ids = []
    away_teams = []
    home_teams = []

    for event in data['events']:
        if (event['status']['type']['completed'] == True):
            game_ids.append(event['id'])
            home_teams.append(event['competitions'][0]['competitors'][0]['team']['displayName'])
            away_teams.append(event['competitions'][0]['competitors'][1]['team']['displayName'])

    if len(game_ids) == 0:
        print('No games have finished today.')
        return game_ids
    
    return (game_ids, home_teams, away_teams)

def save_boxscore_tables(game_id, home_team, away_team):
    url = f'https://www.espn.com/mlb/boxscore/_/gameId/{game_id}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    file_name = f"boxscores/{game_id}-{away_team}-{home_team}-boxscore.txt"
    with open(file_name, 'w') as f:
        f.write(f'{away_team} vs {home_team} Box Score\n\n')

    tables = soup.find_all('table')

    for i, table in enumerate(tables):
        if i == 0:
            continue
        elif i == 10:
            break

        columns = [th.text for th in table.find('tr').find_all('th')]

        data_rows = table.find_all('tr')[1:]
        data = [[td.text for td in row.find_all('td')] for row in data_rows]

        df = pd.DataFrame(data, columns=columns)

        # write the df to a single text file as previous iterations and do not overwrite
        with open(file_name, 'a') as f:
            f.write(df.to_string())
            f.write('\n\n')

if __name__ == "__main__":
    games_info = get_completed_games()
    for id, home_team, away_team in zip(games_info[0], games_info[1], games_info[2]):
        save_boxscore_tables(id, home_team, away_team)