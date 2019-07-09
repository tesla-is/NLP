#Importing Lib's
from selenium import webdriver # For accessing the Web and that Page
import pandas as pd # for Data Manipulation
from bs4 import BeautifulSoup # for extracting data from html pages 
driver = webdriver.Chrome("/usr/bin/chromedriver") # object for dealing with browser


#creating Empty lists for storing data
about = []
titles = []
combinedlist = []
body = []
datepublished = []

# we want to exrect data from all the pages of the website so we have to change the page number in the url
#This url has 76 reviews
for i in range(1,9):
    url = "https://www.gartner.com/reviews/market/network-services/vendor/att?pageNum={}".format(i)
    driver.get(url)
    content = driver.page_source

    # Getting data of all the P tags which itemprop = datepublished this will return the list of Date 
    soup = BeautifulSoup(content)
    for v in soup.findAll('p',attrs={'itemprop':'datePublished'}):
        datepublished.append(v.text)
    
    #For getting the combinedlist(h3 and Itemprop title and about both have same properties so both about and titles are in combined list)

    for v in soup.findAll('h3',attrs={'itemprop':'name'}):
        combinedlist.append(v.text)
    # for getting the reviews 
    for v in soup.findAll('p',attrs ={'class':'snippetSummary'}):
        body.append(v.text)

#For Another Url(there are 3 url's but only 2 are working 1 is just the same verson of another)
#This url has 32 reviews
for i in range(1,5):
    url = "https://www.gartner.com/reviews/market/meeting-solutions-web-conferencing/vendor/att/product/att-connect?pageNum={}".format(i)
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content)
    for v in soup.findAll('p',attrs={'itemprop':'datePublished'}):
        datepublished.append(v.text)
    

    for v in soup.findAll('h3',attrs={'itemprop':'name'}):
        combinedlist.append(v.text)

    for v in soup.findAll('p',attrs ={'class':'snippetSummary'}):
        body.append(v.text)


#This is a small trick to extract about and titles correctly from combined list
about.append(combinedlist[0])
for z in range(1,len(combinedlist)+ 1):
    if z%2 == 0:
        about.append(combinedlist[z])
    else:
        titles.append(combinedlist[z])

#storing scraped data into the CSV file.
dataset = pd.DataFrame({'About':about,'Date':datepublished,'Titles':titles,'Reviews': body})
dataset.to_csv('Data.csv',index=False,encoding='utf-8')


    
