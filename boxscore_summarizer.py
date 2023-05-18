import os
import openai 

# read text from table.txt
data = ""
with open('table.txt', 'r') as file:
    data = file.read()

prompt = "Give me a brief summary of a game between the Boston Red Sox and Atlanta Braves from the following box score. Avoid being overly verbose. Just provide a basic summary of the game, and some standout performers:\n\n"

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant that summarizes MLB boxscores."},
        {"role": "user", "content": prompt + data},
    ]
)

print(response.choices[0].message['content'])