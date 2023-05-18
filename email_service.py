import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def generate_combined_summaries():
    # iterate through files in sumaries directory and combine them into one string and return it
    combined_summaries = ""
    for file in os.listdir('summaries'):
        if file.endswith('.txt'):
            with open(f'summaries/{file}', 'r') as f:
                combined_summaries += f.read()
                combined_summaries += "\n\n"

    print(combined_summaries)
    return combined_summaries

def send_summary_email(email_contents):
    # Email configuration details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    username = 'SportsDigestGPT@gmail.com'
    password = os.getenv("SDGPT_APP_PW")
    from_addr = 'SportsDigestGPT@gmail.com'
    to_addrs = ['snishk@gmail.com']

    # Setup message
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = ', '.join(to_addrs)
    msg['Subject'] = 'SportsDigest-GPT Summary'
    msg.attach(MIMEText(email_contents, 'plain'))

    # Send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addrs, text)
    server.quit()

if __name__ == '__main__':
    email_contents = generate_combined_summaries()
    send_summary_email(email_contents)