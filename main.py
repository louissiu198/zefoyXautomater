
class ZEFOY:
    def __init__(self):
        self.options = Options()
        self.driver = None
        os.system('cls')
        print(Colorate.Horizontal(Colors.yellow_to_red, """
 ███████ ███████ ███████  ██████  ██    ██
    ███  ██      ██      ██    ██  ██  ██  
   ███   █████   █████   ██    ██   ████  
  ███    ██      ██      ██    ██    ██    
 ███████ ███████ ██       ██████     ██    """, 1))
        self.itemid = Write.Input("(?) [Video-ID]  ", Colors.red_to_purple, interval=0.0025)
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
        os.system("cls")
        print(Colorate.Horizontal(Colors.purple_to_red, """
 ███████ ███████ ███████  ██████  ██    ██
    ███  ██      ██      ██    ██  ██  ██  
   ███   █████   █████   ██    ██   ████  
  ███    ██      ██      ██    ██    ██    
 ███████ ███████ ██       ██████     ██    """, 1))
        print(Colorate.Horizontal(Colors.purple_to_red, "(Aurthor) louissiu1998#0503\n(Discord) discord.gg/N2p62eRWam\n(Github) github.com/tvg6u56bu5i/ZEFOY\n", 1))
        print("  ")
        self.driver.get("https://zefoy.com")
        try:
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/h1")
            print(Colorate.Horizontal(Colors.red_to_blue, "(-) Zefoy Access Denied | Error Code 103", 1))
            print(Colorate.Horizontal(Colors.green_to_blue, "(-) Please join server https://discord.gg/N2p62eRWam and submit the error code (example: 101)", 1))
            input("(?) Enter to Exit")
            exit()
        except:
            try:
                self.driver.find_element(By.XPATH, "//*[@id='cf-error-details']/header/h1/span[1]")
                print(Colorate.Horizontal(Colors.red_to_blue, "(-) Zefoy 502 Bad Gateway | Error Code 102", 1))
                print(Colorate.Horizontal(Colors.green_to_blue, "(-) Please join server https://discord.gg/N2p62eRWam and submit the error code (example: 101)", 1))
                input("(?) Enter to Exit")
                exit()
            except:
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
            captcha = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/form/div/div/img')
            captcha.screenshot('image.png')
            with open("image.png", "rb") as image:
                image = image.read()
            captcha = self.ocrpm(bytearray(image))
            print(Colorate.Horizontal(Colors.yellow_to_red, "(!) Solved " + captcha, 1))
            self.captcha = captcha
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/form/div/div/div/input'))).send_keys(captcha.lower())
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/form/div/div/div/div/button'))).click()
            try:
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="errorcapthcaclose"]/div/div')))
                print(Colorate.Horizontal(Colors.red_to_blue, "(-) Captcha Incorrect", 1))
                self.driver.refresh()
            except:
                print(Colorate.Horizontal(Colors.yellow_to_red, "(+) Captcha passed", 1))
                break
               
    def start(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div[2]/div/div/div[5]/div/button'))).click()
            print(Colorate.Horizontal(Colors.yellow_to_red, "(+) Views Working", 1))
        except:
            print(Colorate.Horizontal(Colors.red_to_blue, "(-) Views Broken", 1))
            exit()
        os.system('cls')
        print(Colorate.Horizontal(Colors.yellow_to_red, """
 ███████ ███████ ███████  ██████  ██    ██
    ███  ██      ██      ██    ██  ██  ██  
   ███   █████   █████   ██    ██   ████  
  ███    ██      ██      ██    ██    ██    
 ███████ ███████ ██       ██████     ██    """, 1))
        print(Colorate.Horizontal(Colors.yellow_to_red, "(Aurthor) louissiu1998#0503\n(Discord) discord.gg/N2p62eRWam\n(Github) github.com/tvg6u56bu5i/ZEFOY\n", 1))
        while True:
            self.driver.get("https://zefoy.com")
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div[2]/div/div/div[5]/div/button'))).click()
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[10]/div/form/div/input'))).send_keys(self.itemid)
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[10]/div/form/div/div/button'))).click()
            try:
                time.sleep(3)
                timer = self.driver.find_element(By.XPATH, '//*[@id="gettimesv"]').text
                min = timer.split("Please wait ")[1]
                min = min.split(" minute(s)")[0]
                sec = timer.split("minute(s) ")[1]
                sec = sec.split(" seconds")[0]
                print(Colorate.Horizontal(Colors.red_to_blue, "(-) Timer " + min + " Minutes " + sec + " Seconds", 1))
                self.timer = int(min)*60+int(sec)
                time.sleep(self.timer) # Timer calculation
            except Exception as e:
                try:
                    counts = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="c2VuZC9mb2xeb3dlcnNfdGlrdG9V"]/div[1]/div/form/button'))).text
                    print(Colorate.Horizontal(Colors.yellow_to_red, f"(*) View Count {counts}", 1))
                    WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="c2VuZC9mb2xeb3dlcnNfdGlrdG9V"]/div[1]/div/form/button'))).click()
                    print(Colorate.Horizontal(Colors.yellow_to_red, "(*) View Sent", 1))
                    time.sleep(3)
                    timer = self.driver.find_element(By.XPATH, '//*[@id="gettimesv"]').text
                    min = timer.split("Please wait ")[1]
                    min = min.split(" minute(s)")[0]
                    sec = timer.split("minute(s) ")[1]
                    sec = sec.split(" seconds")[0]
                    print(Colorate.Horizontal(Colors.red_to_blue, "(-) Timer " + min + " Minutes " + sec + " Seconds", 1))
                    self.timer = int(min)*60+int(sec)
                    time.sleep(self.timer) # Timer calculation
                except:
                    print(Colorate.Horizontal(Colors.red_to_blue, "(-) Session Expired", 1))
                    self.driver.refresh()
                    self.solve()
                    self.start()
                   
import os
try:
    import pystyle
    print("(+) Module All Installed")
except:
    print("(-) Module Not Installed")
    print("(+) Installing Modules Automaticlly")
    os.system("pip install -r requirements.txt")
import requests
import selenium
import random
import time
import os        
from pystyle import Colorate, Colors, Write
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
os.system(f'title ZEFOY     (Aurthor) louissiu1998#0503 (Discord) discord.gg/N2p62eRWam (Github) github.com/tvg6u56bu5i/ZEFOY')
client = ZEFOY()
client.setup()
client.start()



