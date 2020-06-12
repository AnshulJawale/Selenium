from selenium import webdriver
import time

insta_username = '<<username>>'
insta_password = '<<password>>'

#? https://www.instagram.com/accounts/login/?next=/nextactivity/
#* format of xpath = "{type of element}[conditions]"
#* login, get page, like, follow(public, private), send message

class InstagramActivity():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()        
        self.url = 'https://www.instagram.com'
        self.driver.get(self.url)
        self.page_source = self.driver.page_source


    def login(self):
        time.sleep(3)
        #self.driver.get('https://www.instagram.com')
        username = self.driver.find_element_by_name('username').send_keys(self.username)
        password = self.driver.find_element_by_name('password').send_keys(self.password)

        time.sleep(2)
        submit_button = self.driver.find_element_by_css_selector("button[type='submit']").click()


    def turn_off_if_asked(self):
        time.sleep(2)
        if len(self.driver.find_elements_by_class_name("piCib")) > 1:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now'])").click()


    def get_homepage(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(2)
        self.login()


    def follow_public_user(self, to_follow_username):
        self.driver.get(f"https://www.instagram.com/accounts/login/?next=/{to_follow_username}/") 
        time.sleep(2)
        self.login()
        time.sleep(5)

        follow_button = self.driver.find_elements_by_xpath("//*[contains(text(), 'Follow')][not(contains(text(), 'Followers'))][not(contains(text(), 'Following'))][not(contains(text(), 'Follows'))]")[0]
        follow_button.click()


    def follow_private_user(self, to_follow_username):
        self.driver.get(f"https://www.instagram.com/accounts/login/?next=/{to_follow_username}/")
        time.sleep(2)
        self.login()
        time.sleep(5)

        follow_button = self.driver.find_elements_by_css_selector("button[type='button']")[0]
        follow_button.click()


    def send_message(self, to_send_user, message):
        self.driver.get('https://www.instagram.com/accounts/login/?next=/direct/inbox/')
        self.login()

        time.sleep(10)

        send_message_btn = self.driver.find_element_by_css_selector("button[type='button']").click()

        search_bar = self.driver.find_element_by_name("queryBox").send_keys(to_send_user)

        time.sleep(3)

        select_user = self.driver.find_element_by_class_name("dCJp8").click()

        time.sleep(3)

        next_button = self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div:nth-child(1) > div > div:nth-child(3) > div > button").click()
        
        time.sleep(10)

        text_area = self.driver.find_element_by_css_selector("textarea[placeholder='Message...']").send_keys(message)
        
        send_button = self.driver.find_element_by_css_selector("#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk > div.uueGX > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.Igw0E.IwRSH.eGOV_._4EzTm.JI_ht > button").click()


    def like(self, to_like_username, i=0):
        self.driver.get(f"https://www.instagram.com/accounts/login/?next=/{to_like_username}/")
        self.login()
        time.sleep(7)

        posts = self.driver.find_elements_by_class_name("v1Nh3")
        post = posts[i]
        
        link = post.find_element_by_css_selector(f"#react-root > section > main > div > div._2z6nI > article > div:nth-child(1) >div> div:nth-child({(i+1)//3}) > div:nth-child({i%3 + 1}) > a")   #get link of post
        href = link.get_attribute('href')
        self.driver.get(href)
        time.sleep(3)

        like_button = self.driver.find_element_by_class_name("wpO6b").click()

s = InstagramActivity(insta_username, insta_password)