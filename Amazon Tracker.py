from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
import requests
import datetime
import os


def amazon_tracker(product, index=1):
    '''
    Amazon Price Tracker.
    Enter name of product. 
    '''

    #Using Selenium Without opening browser
    url_keyword = product.replace(' ', '+')

    opt = Options()
    opt.add_argument('--headless')
    driver = webdriver.Chrome(options=opt)

    #Setting up driver
    driver.get(f'https://www.amazon.in/s?k={url_keyword}')
    sleep(5)
    search_results = driver.find_element_by_class_name("s-search-results")
    links = search_results.find_elements_by_xpath(f"//a[contains(@href, '&keywords={url_keyword}&qid')]")

    sleep(5)

    link = links[index-1]
    sleep(3)

    href = link.get_attribute('href')
    driver.get(href)

    #Getting elements
    name = driver.find_element_by_id("productTitle")
    price = driver.find_element_by_id("priceblock_ourprice")
    rating = driver.find_element_by_class_name("a-icon-alt")
    no_of_ratings = driver.find_element_by_id("acrCustomerReviewText")

    #Parsing Data
    soup_name = BeautifulSoup(name.get_attribute('innerHTML'), 'html.parser').text
    soup_price = BeautifulSoup(price.get_attribute('innerHTML'), 'html.parser').encode()
    soup_rating = BeautifulSoup(rating.get_attribute('innerHTML'), 'html.parser').text
    soup_no_of_ratings = BeautifulSoup(no_of_ratings.get_attribute('innerHTML'), 'html.parser').text

    info = {"Name":soup_name.strip(),
            "Price":soup_price,
            "Rating":soup_rating,
            "Number of ratings":soup_no_of_ratings,
            "URL":href}

    #Creating Directory
    BASE_DIR = os.path.dirname(__file__)
    path = os.path.join(BASE_DIR, "Amazon Files")
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join(path, f"{info['Name']} {index}.txt")
    #filepath = os.path.join(path, f"{keyword}")

    #Writing data to a file
    now = datetime.datetime.now()
    with open(filepath, 'a') as f:
        f.write("\n\n")
        f.write(f"Date : {now.day}/{now.month}/{now.year}, Time : {now.hour}:{now.minute}:{now.second}")
        f.write(f"\nKeyword : {url_keyword}")
        for i in info.keys():
            if i == "Price":
                continue
            f.write("\n")
            f.write(f"{i} : {info[i]}")
            
    with open(filepath, 'ab') as f:
        f.write(b"\n")
        f.write(b"Price : %b"%(info['Price']))

try:
    amazon_tracker("Apple iPhone Xs Max 64GB - Gold")  
except:
    print("Try again.")
else:
    print("Successfully Tracked.")    