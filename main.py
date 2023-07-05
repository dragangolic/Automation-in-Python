import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
now = datetime.datetime.now()

# EMAIL CONTENT PLACEHOLDER
content = ''

# Extracting Hacker News Stories

def extract_news(url):
    print('Extracting Hacker Stories...')
    cnt = ''
    cnt += ('<b>HN Top Stories:<b>\n'+'<b>'+'-'*50+'<b>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i+1)+' :: '+tag.text + "\n" + '<b>') if tag.text != 'More' else '')
        # Print(tag,prettify) # find_all('span', attrs={'class':'sitestr'}))
    return cnt

# Call the function
cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>-----<br>')
content += ('<br><br>End of Message')

# Send the email

# Update your email details

SERVER = 'smtp.gmail.com'  # your smtp server
PORT = 587  # your port number
FROM = 'golicdragan0@gmail.com'  # your from email id
TO = 'golicdragan0@gmail.com'  # your to email ids, it can be a list
PASS = 'chtgzvinstsvxhib'  # your email id's password

# fp = open(file_name, 'rb')
# Create a text/plain message
# msg = MIMEText('')
msg = MIMEMultipart()

# msg.add_header('Content-Disposition', 'attachment', file_name='empty.txt')
msg['Subject'] = 'Top News Stories HN [Automated Email]' + '' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))
# fp.close()

print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
# server = smtplib.SMTP SSL('smtp.gmail.com', 465)
server.set_debuglevel(1)  # 0 is not to see error messages, 1 is to see them
server.ehlo()
server.starttls()
# server.ehlo
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()