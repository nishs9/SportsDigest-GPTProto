import scraper
import boxscore_summarizer
import email_service
import os

# Delete previously generated boxscores and summaries
def delete_old_files():
    for file in os.listdir('boxscores'):
        if file.endswith('.txt'):
            os.remove(f'boxscores/{file}')
    for file in os.listdir('summaries'):
        if file.endswith('.txt'):
            os.remove(f'summaries/{file}')

if __name__ == "__main__":
    games_info = scraper.get_completed_games()
    if len(games_info) == 0:
        print("No games have been completed today so no email will be sent...")
    else:
        delete_old_files()
        for id, home_team, away_team in zip(games_info[0], games_info[1], games_info[2]):
            scraper.save_boxscore_tables(id, home_team, away_team)
        boxscore_summarizer.generate_all_summaries()
        email_contents = email_service.generate_combined_summaries()
        email_service.send_summary_email(email_contents)