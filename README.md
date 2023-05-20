# SportsDigest-GPT POC

SportDigest-GPT is a project leverages the GPT-3.5 model to generate summaries of MLB box scores and sends them out as an email blast. As the project title suggests, this is only a proof-of-concept that I am using to validate that my larger project idea is feasible.

## Overview
This prototype has relatively basic functionality. It is made up of 3 different components:

1. The first component is a web scraper that calls the [ESPN Hidden API](https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b). The scraper pulls all of the MLB game ids for today's games and uses those game ids to retrieve the box score page on ESPN.com. The relevant box score tables are then scraped and outputted to a text file in the "boxscores" directory. The scraper only retrieves the box score for games that have been completed.
2. The second component reads the box score tables into a string and sends it, along with a prompt asking for a summary of the game, to the GPT-3.5 model. The model returns a game summary which is then saved into a separate text file in the "summaries" directory.
3. The final component takes all of the generated game summaries, assembles them into a single piece of text and then sends it to a given email address

## Using SportsDigest-GPT POC
To use the POC of my SportsDigest-GPT project, you will need to do the following pre-requisite tasks:
1. After cloning the repository, run `pip install -r requirements.txt` to download all the necessary dependencies.
2. Create a sender email address for the email summaries. You can do this in many ways. I chose to create a new Gmail account and generate an app password to use along with it. 
3. Next, you will need to define a `secret_keys.py` with the following variables:  `openai_api_key`, `from_email`, `from_email_password`, `to_email`.

Once you complete the pre-requisites, If you want to run the full flow of the POC, just run `python main.py`. This will run all 3 components together and send a summary email. You can also run the components individually. NOTE: If no games have completed on the day that you run the main script, then nothing will be generated.

Thanks to github user akeaswaran for his documentation on the ESPN Hidden API. You can view the documentation here: https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b
