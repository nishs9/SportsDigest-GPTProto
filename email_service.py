import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email details
smtp_server = 'smtp.example.com'
smtp_port = 587  # typically 587 for TLS, or 465 for SSL
username = 'SportsDigestGPT@gmail.com'
password = 'qqbltuscuvyezppa'
from_addr = 'SportsDigestGPT@gmail.com'
to_addrs = ['snishk@gmail.com']

# Read the contents of the text file
with open('yourfile.txt', 'r') as f:
    message_body = f.read()

# Create message
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = ', '.join(to_addrs)
msg['Subject'] = 'Your subject here'
msg.attach(MIMEText(message_body, 'plain'))

# Send the email
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)
text = msg.as_string()
server.sendmail(from_addr, to_addrs, text)
server.quit()