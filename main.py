
PATHS = {
    "captchaImage":"/html/body/div[5]/div[2]/form/div/div/img",
    "captchaInput":"/html/body/div[5]/div[2]/form/div/div/div/input",
    "captchaButton":"/html/body/div[5]/div[2]/form/div/div/div/div/button",
    "captchaCheck":"//*[@id='errorcapthcaclose']/div/div",
    "viewsButton": "/html/body/div[6]/div/div[2]/div/div/div[5]/div/button",
    "viewsInput":"/html/body/div[10]/div/form/div/input",
    "viewsEnter":"/html/body/div[10]/div/form/div/div/button",
    "viewsTimer":"//*[@id='c2VuZC9mb2xeb3dlcnNfdGlrdG9V']/span",
    "viewsExpire":"//*[@id='c2VuZC9mb2xeb3dlcnNfdGlrdG9V']/div",
    "viewsConfirm":"//*[@id='c2VuZC9mb2xeb3dlcnNfdGlrdG9V']/div[1]/div/form/button",
}

import threading
import requests
import selenium
import random
import time
import os
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class ZEFOY:
    def __init__(self):
        self.options = Options()
        self.option = None
        self.driver = None
        self.itemid = input("(?) [VIDEO-ID]  ")
        self.uagent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
        self.views = 0
        self.captcha = ""
        self.timer = 0

    def setup(self):
        global driver
        self.itemid = f"https://www.tiktok.com/@{random.randint(10000,99999)}user{random.randint(10000,99999)}/video/" + self.itemid
        self.options.add_argument("--user-agent="+self.uagent)
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(),
            options=self.options
        )
        os.system("clear")
        print("""
 ███████ ███████ ███████  ██████  ██    ██
    ███  ██      ██      ██    ██  ██  ██  
   ███   █████   █████   ██    ██   ████  
  ███    ██      ██      ██    ██    ██    
 ███████ ███████ ██       ██████     ██    """)
        self.driver.get("https://zefoy.com")
        self.solve()
       
    def ocrpm(self, image):        
        response = requests.post(
            url="https://api.api-ninjas.com/v1/imagetotext",
            files={"image": image},
            headers={
                "Origin": "https://api-ninjas.com",
                "Referer": "https://api-ninjas.com/"
            }
        )
        response = list(response.json())
        response = dict(response[0])
        return response["text"]
           
    def solve(self):
        while True:
            captcha = self.driver.find_element(By.XPATH, PATHS["captchaImage"])
            captcha.screenshot('image.png')
            with open("image.png", "rb") as image:
                image = image.read()
            captcha = self.ocrpm(bytearray(image))
            print("(!) Solved " + captcha)
            self.captcha = captcha
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, PATHS['captchaInput']))).send_keys(captcha.lower())
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, PATHS['captchaButton']))).click()
            try:
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, PATHS["captchaCheck"])))
                print("(-) Captcha Incorrect")
                self.driver.refresh()
            except:
                print("(+) Captcha Passed")
                break
               
    def start(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, PATHS['viewsButton']))).click()
            print("(+) VIEWS WORKING")
        except:
            print("(-) VIEWS BROKEN")
            exit()
        os.system('clear')
        print("""
 ███████ ███████ ███████  ██████  ██    ██
    ███  ██      ██      ██    ██  ██  ██  
   ███   █████   █████   ██    ██   ████  
  ███    ██      ██      ██    ██    ██    
 ███████ ███████ ██       ██████     ██    """)
        while True:
            self.driver.get("https://zefoy.com")
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, PATHS['viewsButton']))).click()
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, PATHS['viewsInput']))).send_keys(self.itemid)
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, PATHS['viewsEnter']))).click()
            try:
                time.sleep(3)
                timer = self.driver.find_element(By.XPATH, PATHS["viewsTimer"]).text
                print(timer)
                min = timer.split("Please wait ")[1]
                min = min.split(" minute(s)")[0]
                sec = timer.split("minute(s) ")[1]
                sec = sec.split(" seconds")[0]
                print("(-) TIMER " + min + " Minutes " + sec + " Seconds")
                self.timer = int(min)*60+int(sec)
                time.sleep(self.timer+1) # Timer calculation
            except Exception as e:
                counts = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, PATHS["viewsConfirm"]))).text
                print(f"(*) VIEW COUNT {counts}")
                WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, PATHS["viewsConfirm"]))).click()
                print("(+) VIEW SENT")
                self.views += random.randint(1000,1599)
                time.sleep(5)
                timer = self.driver.find_element(By.XPATH, PATHS["viewsTimer"]).text
                print(timer)
                min = timer.split("Please wait ")[1]
                min = min.split(" minute(s)")[0]
                sec = timer.split("minute(s) ")[1]
                sec = sec.split(" seconds")[0]
                print("(+) TIMER " + min + " Minutes " + sec + " Seconds")
                self.timer = int(min)*60+int(sec)
                time.sleep(self.timer+1) # Timer calculation

#os.system(f'title [ZEFOY] (Views): {client.views} | (Captcha): {client.captcha} | (Timer): {client.timer} Seconds | (Aurthor): louissiu1998#0503 | (Discord): discord.gg/N2p62eRWam (Github): github.com/louissiu1998')
client = ZEFOY()
client.setup()
client.start()

