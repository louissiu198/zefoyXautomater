

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

ICONS = """
 ███████ ███████ ███████  ██████  ██    ██
    ███  ██      ██      ██    ██  ██  ██  
   ███   █████   █████   ██    ██   ████  
  ███    ██      ██      ██    ██    ██    
 ███████ ███████ ██       ██████     ██    
"""

class ZEFOY:
    def __init__(self):
        self.itemid = input("(?) [ZEFOY]  Video-Id  | ")
        self.uagent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"

    def setup(self):
        self.options = Options()
        self.options.add_argument("--user-agent="+self.uagent)
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=self.options)
        os.system("clear")
        self.prank("9")
        self.driver.get("https://zefoy.com")
        self.solve()

    def sleep(self, timer):
        min = timer.split("Please wait ")[1]
        min = min.split(" minute(s)")[0]
        sec = timer.split("minute(s) ")[1]
        sec = sec.split(" seconds")[0]
        return min, sec
    
    def prank(self, choice, bar1=None, bar2=None):
        if choice == "1":
            print(Colorate.Horizontal(Colors.yellow_to_red,f"[ZEFOY] (-) Captcha Incorrect"))
        elif choice == "2":
            print(Colorate.Horizontal(Colors.yellow_to_red,f"[ZEFOY] (+) Captcha Correct"))
        elif choice == "3":
            print(Colorate.Horizontal(Colors.yellow_to_red,f"[ZEFOY] (!) Captcha Solved | {bar1}"))
        elif choice == "4":
            print(Colorate.Horizontal(Colors.yellow_to_red,"[ZEFOY] (+) Views Working"))
        elif choice == "5":
            print(Colorate.Horizontal(Colors.yellow_to_red,"[ZEFOY] (+) Views Broken"))
        elif choice == "6":
            print(Colorate.Horizontal(Colors.yellow_to_red,f"[ZEFOY] (-) Timeout | {bar1} Minutes {bar2} Seconds"))
        elif choice == "9":
            print(Colorate.Horizontal(Colors.yellow_to_red,ICONS))
    def ocrpm(self, image):        
        response = requests.post(
            url="https://api.api-ninjas.com/v1/imagetotext",
            files={"image": image},
            headers={
                "Origin": "https://api-ninjas.com",
                "Referer": "https://api-ninjas.com/"
            }
        )
        try:
            response = list(response.json())
            response = dict(response[0])
            return response["text"]
        except:
            self.ocrpm(image)
    # Try Except Prevent Exceptions as json to list to dict
           
    def solve(self):
        while True:
            captcha = self.driver.find_element(By.XPATH, PATHS["captchaImage"])
            captcha.screenshot('image.png')
            with open("image.png", "rb") as image:
                image = image.read()
            captcha = self.ocrpm(bytearray(image))
            self.prank("3", captcha)
            self.captcha = captcha
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, PATHS['captchaInput']))).send_keys(captcha.lower())
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, PATHS['captchaButton']))).click()
            try:
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, PATHS["captchaCheck"])))
                self.prank("1")
                self.driver.refresh()
            except:
                self.prank("2")
                break
               
    def start(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, PATHS['viewsButton']))).click()
            self.prank("4")
        except:
            self.prank("5")
            exit()
        os.system('clear')
        self.prank("9")
        while True:
            self.driver.get("https://zefoy.com")
            try:
                self.driver.find_element(By.XPATH, PATHS["captchaImage"])
                self.driver.refresh()
                self.solve()
            except:
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, PATHS['viewsButton']))).click()
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, PATHS['viewsInput']))).send_keys(self.itemid)
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, PATHS['viewsEnter']))).click()
                try:
                    time.sleep(3)
                    min, sec = self.sleep(self.driver.find_element(By.XPATH, PATHS["viewsTimer"]).text)
                    self.prank("6", min, sec)
                    self.timer = int(min)*60+int(sec)
                    time.sleep(self.timer+1)
                except Exception as e:
                    try:
                        counts = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, PATHS["viewsConfirm"]))).text
                        print(Colorate.Horizontal(Colors.yellow_to_red,f"(*) [ZEFOY] Count {counts}"))
                        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, PATHS["viewsConfirm"]))).click()
                        print(Colorate.Horizontal(Colors.yellow_to_red,"(+) [ZEFOY] Sent"))
                        time.sleep(5)
                        min, sec = self.sleep(self.driver.find_element(By.XPATH, PATHS["viewsTimer"]).text)
                        self.prank("6", min, sec)
                        self.timer = int(min)*60+int(sec)
                        time.sleep(self.timer+1) 
                    except:
                        self.driver.refresh()
                        self.solve()
        # First Loop, then try except to prevent captcha appear after 5-6 refresh, then next try except about the first timer and session expired

client = ZEFOY()
client.setup()
client.start()

import threading
import requests
import selenium
import random
import time
import os
from PIL import Image
from io import BytesIO
from selenium import webdriver
from pystyle import Colorate, Colors, Write
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


