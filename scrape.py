from bs4 import BeautifulSoup
import csv
import time
from selenium import webdriver
url = 'http://media.lesechos.fr/infographie/champions_croissance_2019/'
driver = webdriver.Chrome('./chromedriver') 
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

csv_columns = [x.text for x in soup.find_all('tr')[1].find_all('th') ]
corpus = []

for i in range(5):
    
    html = driver.page_source
    soup = BeautifulSoup(html)
    tbody = soup.find('tbody')
    trs= tbody.find_all('tr')
    for tr in trs:
        row = [x.text for x in tr.find_all('td') ]
        print(row)
        corpus.append(row)
    
    driver.find_element_by_id('tableau_next').click()
    time.sleep(3)

csv_file = "./result.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.writer(csvfile) 
        writer.writerow(csv_columns)
        writer.writerows(corpus)
except IOError:
    print("I/O error")
