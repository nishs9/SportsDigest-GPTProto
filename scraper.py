import requests
from bs4 import BeautifulSoup
import pandas as pd

test_file_name = 'table.txt'
test_url = 'https://www.espn.com/mlb/boxscore/_/gameId/401471565'

def save_boxscore_tables(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

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
        print(df)
        print()

        # write the df to a single text file as previous iterations and do not overwrite
        with open(test_file_name, 'a') as f:
            f.write(df.to_string())
            f.write('\n\n')

if __name__ == "__main__":
    save_boxscore_tables(test_url)