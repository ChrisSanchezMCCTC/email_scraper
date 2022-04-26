from bs4 import BeautifulSoup
import requests
import schedule
import time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os

url = "https://teachers.mahoningctc.com/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

print(soup.title.text)

# temp = soup.find_all('div', attrs={'class': 'one-third columns'})
for link in soup.find_all('div', attrs={'class':'one-third columns'}):
    print(link.find('a')['href'])
    print(link.find('a').contents)
    
    # print(link.get('href'))

# print(temp[1].text)
# print(temp[2].text)