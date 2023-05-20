import os
import openai
import secret_keys

# Generate summaries for all boxscores
def generate_all_summaries():
  for file in os.listdir('boxscores'):
    if file.endswith('.txt'):
      generate_single_summary(file)

# Helper method to generate individual game summaries
def generate_single_summary(file):
  data = ""
  with open(f'boxscores/{file}', 'r') as file:
      data = file.read()

  game_id = file.name.split('-')[0].split('/')[1]
  away_team = file.name.split('-')[2]
  home_team = file.name.split('-')[1]

  print(f"Generating summary for {away_team} vs {home_team}...")

  prompt = f"Give me a brief summary of a game between the {away_team} and {home_team} from the following box score. Avoid being overly verbose. Just provide a basic summary of the game, and some standout performers:\n\n"

  openai.api_key = secret_keys.openai_api_key

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
    f.write(f'{away_team} vs {home_team} Summary\n\n')
    f.write(summary)

if __name__ == '__main__':
  generate_all_summaries()