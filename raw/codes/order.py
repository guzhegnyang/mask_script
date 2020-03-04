# coding = utf-8
import json
import time
from selenium import webdriver
chrome_driver = "../chromedriver_win32/chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_driver)
url1 = 'http://kzyynew.qingdao.gov.cn:81/authPage/page#'
browser.get(url1)
with open("../data.txt") as f:
    data = json.loads(f.read())
    while True:
        try:
            have_read = browser.find_element_by_xpath('//*[@id="mzsm"]/div/form/div')
            order = browser.find_element_by_xpath('//*[@data-name="'+data[0]+'"]/div[3]/a')
            break
        except:
            browser.refresh()
    while True:
        try:
            have_read.click()
        except:
            break
    while True:
        try:
            order.click()
        except:
            break
    name = browser.find_element_by_xpath('/html/body/form/div[1]/div/input[3]')
    name.click()
    name.send_keys(data[1])
    tele = browser.find_element_by_xpath('/html/body/form/div[2]/div/input')
    tele.click()
    tele.send_keys(data[2])
    idcard = browser.find_element_by_xpath('/html/body/form/div[3]/div/input')
    idcard.click()
    idcard.send_keys(data[3])
    CAPTCHA = browser.find_element_by_xpath('/html/body/form/div[6]/div/input')
    CAPTCHA.click()
    #button = browser.find_element_by_xpath('/html/body/form/div[7]/button')