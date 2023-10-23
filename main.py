from os import system
from time import sleep
from httpx import get, post
from random import randint
from pystyle import Write, Colors, Colorate
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from undetected_chromedriver import ChromeOptions, Chrome
from selenium.webdriver.support import expected_conditions as EC
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

viewsSent = 0

xpathId = {
    "webTest": "/html/body/nav/button",
    "textWrong": "/html/body/div[5]/div/div/div[2]/b", 
    "textInput": "/html/body/div[5]/div[2]/form/div/div/div/input", 
    "textButton": "/html/body/div[5]/div[2]/form/div/div/div/div/button", 
    "textCaptcha": "/html/body/div[5]/div[2]/form/div/div/img",
    "serviceInput": "/html/body/div[10]/div/form/div/input",
    "serviceTimer": "/html/body/div[10]/div/div/span",
    "serviceSearch": "/html/body/div[10]/div/form/div/div/button",
    "serviceConfirm": "/html/body/div[10]/div/div/div[1]/div/form/button",
    "serviceButton": "/html/body/div[6]/div/div[2]/div/div/div[5]/div/button",
    "serviceMessage": "/html/body/div[10]/div/div/span[2]"
}


class ZefoyAutomater:
    def __init__(self):
        self.driver = Chrome()

    def double_check(self):
        sleep(1)
        for _ in range(6):
            text = self.driver.find_element(By.XPATH, xpathId["serviceTimer"]).text
            if text.startswith("Please wait"):
                return text
            else:
                sleep(1)

    def cloudfare_bypass(self):
        solved = False
        while True:
            self.driver.execute_script('window.open("https://zefoy.com");') # Flagged: self.driver.switch_to.window(self.driver.window_handles[1]) self.driver.get("https://zefoy.com")
            sleep(5) # Takes so time bro 5-8 seconds | fastest 3 slowest 14
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            try: 
                self.driver.find_element(By.XPATH, xpathId["webTest"])
            except: 
                self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/iframe"))
                for _ in range(5):
                    try: 
                        self.driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/label/input").click()
                        break
                    except: 
                        sleep(1)
                        continue

            for _ in range(3000):
                if str(self.driver.title) != "Just a moment...":
                    solved = True
                    break
            if solved == True:
                self.captcha_solver()
                self.automating_zefoy()
            else:
                solved = False
    
    def image_recoginizer(self, image):
        resp = post(
            f"https://platipus9999.pythonanywhere.com/", 
            json = {'image': image}
        ).text
        # Plati credits to, im to lazy
        return resp
    def transfer_textime(self, text):
        print(int(text.split("Please wait ")[1].split(" minute(s)")[0])*60+int(text.split("minute(s) ")[1].split(" seconds")[0]))
        return int(text.split("Please wait ")[1].split(" minute(s)")[0])*60+int(text.split("minute(s) ")[1].split(" seconds")[0])

    def captcha_solver(self):
        while True:
            captcha = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpathId["textCaptcha"]))).screenshot('image.png')
            captcha = self.image_recoginizer(bytes(bytearray(open("image.png", "rb").read()))).lower()
            print(f"(+) Solved - the text is {captcha}")
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpathId["textInput"]))).send_keys(captcha)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpathId['textButton']))).click()
            try:
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpathId["textWrong"])))
                self.driver.refresh()
            except:
                break
    
    def automating_zefoy(self):
        self.driver.get("https://zefoy.com")
        self.captcha_solver()
        if "502" in self.driver.page_source:
            print("[!] Error - Cloudfare 502 Bad Gateway IP Flagged")

        try: WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpathId["serviceButton"])))
        except: exit()

        while True:
            self.driver.get("https://zefoy.com")
            try:
                self.driver.find_element(By.XPATH, xpathId["textCaptcha"])
                self.driver.refresh()
                self.captcha_solver()
            except:
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpathId['serviceButton']))).click()
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpathId['serviceInput']))).send_keys(videoLink)
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpathId['serviceSearch']))).click()
                try:
                    sleep(2) # wait 2-3
                    self.timer = self.transfer_textime(self.double_check())
                    print(f"[*] Timer - Countdown for {self.timer} seconds")
                    sleep(self.timer)
                except:
                    try:
                        counts = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, xpathId["serviceConfirm"]))).text
                        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, xpathId["serviceConfirm"]))).click()
                        sleep(3)
                        self.timer = self.transfer_textime(self.double_check())
                        sent = self.driver.find_element(By.XPATH, xpathId["serviceMessage"]).text
                        print(f"[*] Timer - Countdown for {self.timer} seconds")
                        sleep(self.timer) 
                    except:
                        self.driver.refresh()
                        self.captcha_solver()

videoLink = Write.Input("Video Link -> ", Colors.red_to_purple, interval=0.0025)
ZefoyAutomater().automating_zefoy()
