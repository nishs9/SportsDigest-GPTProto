# SportsDigest-GPT POC

SportDigest-GPT is a project leverages the GPT-3.5 model to generate summaries of MLB box scores and sends them out as an email blast. As the project title suggests, this is only a proof-of-concept that I am using to validate that my larger project idea is feasible.

## Overview
This prototype has relatively basic functionality. It is made up of 3 different components:

1. The first component is a web scraper that calls the [ESPN Hidden API](https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b). The scraper pulls all of the game ids for today's games and uses those game ids to retrieve the box score page on ESPN.com. The relevant box score tables are then scraped and outputted to a text file for later processing.
