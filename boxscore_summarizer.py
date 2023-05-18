import os
import openai

def generate_all_summaries():
  # iterate through boxscores and return file name
  for file in os.listdir('boxscores'):
    if file.endswith('.txt'):
      print(file)
      generate_single_summary(file)

def generate_single_summary(file):
  # read text from table.txt
  data = ""
  with open(f'boxscores/{file}', 'r') as file:
      data = file.read()

  game_id = file.name.split('-')[0].split('/')[1]
  away_team = file.name.split('-')[2]
  home_team = file.name.split('-')[1]

  prompt = f"Give me a brief summary of a game between the {away_team} and {home_team} from the following box score. Avoid being overly verbose. Just provide a basic summary of the game, and some standout performers:\n\n"

  openai.api_key = os.getenv("OPENAI_API_KEY")

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
          {"role": "system", "content": "You are a helpful assistant that summarizes MLB boxscores."},
          {"role": "user", "content": prompt + data},
      ]
  )

  summary = response.choices[0].message['content']
  summary_file_name = f'summaries/{game_id}-{away_team}-{home_team}-summary.txt'
  with open(summary_file_name, 'w') as f:
    f.write(summary)

if __name__ == '__main__':
  generate_all_summaries()