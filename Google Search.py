from selenium import webdriver
import time

browser = webdriver.Chrome()  #launches driver in Chrome
url = 'https://google.com'
browser.get(url)

name = 'q'
search = browser.find_element_by_name(name)  #find element class 
time.sleep(3)
search.send_keys("weather in pune")               #sends input to element

submit_button = browser.find_element_by_css_selector("input[type='submit'")     #finds button
print(submit_button.get_attribute('value'))         #returns any given attribute
time.sleep(2)
submit_button.click()      #clicks button if it is interactive