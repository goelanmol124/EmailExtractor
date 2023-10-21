from bs4 import BeautifulSoup
import csv
import re
from selenium import webdriver
import time
import os


webfiles = 'weblinks.csv'
weblist = []
with open(webfiles,'r') as f:
    reader = csv.reader(f)
    for website in reader:
        weblist.append(website[0])
cwd = os.getcwd()
driver = webdriver.Chrome(executable_path=cwd + "\chromedriver.exe")

for website in weblist:
    print(website)
    driver.get(website)
    time.sleep(4)
    source_file = driver.page_source
    filename = "output\\" + website[8:15] + '.csv'

    def extract_email(text):
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_regex, text)
        return emails

    soup = BeautifulSoup(source_file, 'html.parser')

    with open(filename,'w') as outputfile:
        writer = csv.writer(outputfile)
        emails = extract_email(soup.prettify())
        for i in emails:
            writer.writerow([i])
            print(i)

driver.close()
