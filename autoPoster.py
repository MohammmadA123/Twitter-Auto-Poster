from selenium import webdriver
from selenium.webdriver.common.by import By
import time

USERNAME = "your username"
PASSWORD = "your password"
TWEET = "Your tweet"

driver = webdriver.Chrome()
driver.get("https://twitter.com/login")

elem = driver.find_element(By.XPATH,'//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
elem.send_keys(USERNAME)
elem = driver.find_element(By.XPATH,'//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
elem.send_keys(PASSWORD)
elem = driver.find_element(By.XPATH,'//*[@id="page-container"]/div/div[1]/form/div[2]/button')
elem.click()
time.sleep(1.5)
elem = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div[2]/div/div[1]/div/div/a/div[2]/div/div')
elem.click()
time.sleep(1.5)
elem = driver.find_element_by_css_selector('#react-root > div > div > div.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-184en5c > div > div > div > div > div.css-1dbjc4n.r-1habvwh.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-t23y2h.r-1wbh5a2.r-rsyp9y.r-1pjcn9w.r-htvplk.r-1udh08x.r-1potc6q > div > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-46vdb2.r-117bsoe.r-1ozfoo7.r-bcqeeo.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div > div > div > div.css-901oao.r-hkyrab.r-6koalj.r-16y2uox.r-1qd0xha.r-1b6yd1w.r-16dba41.r-ad9z0x.r-bcqeeo.r-qvutc0 > div > div > div > div.DraftEditor-editorContainer > div')
elem.send_keys(TWEET)
driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]').click()
