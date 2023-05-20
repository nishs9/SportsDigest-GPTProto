import smtplib
import os
import secret_keys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Generate combined summary for the email
def generate_combined_summaries():
    combined_summaries = ""
    for file in os.listdir('summaries'):
        if file.endswith('.txt'):
            with open(f'summaries/{file}', 'r') as f:
                combined_summaries += f.read()
                combined_summaries += "\n\n"

    return combined_summaries

# Send summary email
def send_summary_email(email_contents):
    # Email configuration details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    username = 'SportsDigestGPT@gmail.com'
    password = secret_keys.from_email_password
    from_addr = 'SportsDigestGPT@gmail.com'
    to_addrs = [secret_keys.to_email]

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