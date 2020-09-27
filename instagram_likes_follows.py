from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class LikesAndFollows:

    def __init__(self, username, password, comment):
        self.username = username
        self.password = password
        self.comment = comment
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        button_elem = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button")
        passworword_elem.send_keys(self.password)
        button_elem.click()
        time.sleep(2)


    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        #Get the first picture which has the given hashtag
        post = driver.find_element_by_xpath("//html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]")
        post.click()
        time.sleep(2)
        #like the selected picture
        like_button = driver.find_element_by_xpath("//html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")
        like_button.click()
        print("Photo Liked Successfully")
        comment_button = driver.find_element_by_xpath("//html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[2]/button")
        comment_button.click()
        text_area = driver.find_element_by_xpath("//html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea")
        text_area.clear()
        text_area.send_keys(self.comment)
        time.sleep(2)
        comment_post = driver.find_element_by_xpath("//html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button")
        comment_post.click()
        time.sleep(2)



username = "***********"
password = "***********"
comment = "beautiful <3"

ig = LikesAndFollows(username, password, comment)
ig.login()

hashtags = ['beach','lake']

#for loop to iterate through the hashtags list
for hashtag in hashtags:
    try:
        ig.like_photo(hashtag)
    except Exception:
        time.sleep(2)
