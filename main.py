from time import sleep
from httpx import get, post
from random import randint
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

videoId = input("VideoID: ")

serviceId = {
    "followers": [2, 8],
    "hearts": "3",
    "comments_hearts": [4, 9],
    "views": [5, 10],
    "shares": [6, 11],
    "favourites": [7, 12],
    "live_stream_likes": [8,13]
}

class ZefoyAutomater:
    def __init__(self, serviceType):
        self.driver = Chrome()
        self.option = serviceId[serviceType]
        self.setup_xpath()

    def setup_xpath(self):
        self.xpathId = {
            "webTest": "/html/body/nav/button",
            "textWrong": "/html/body/div[5]/div/div/div[2]/b", # captcha incorrect 
            "textInput": "/html/body/div[5]/div[2]/form/div/div/div/input", # captcha input
            "textButton": "/html/body/div[5]/div[2]/form/div/div/div/div/button", # captcha button
            "textCaptcha": "/html/body/div[5]/div[2]/form/div/div/img",
            "serviceInput": f"/html/body/div[{self.option[1]}]/div/form/div/input",
            "serviceTimer": f"/html/body/div[{self.option[1]}]/div/div/span",
            "serviceSearch": f"/html/body/div[{self.option[1]}]/div/form/div/div/button",
            "serviceConfirm": f"/html/body/div[{self.option[1]}]/div/div/div[1]/div/form/button",
            "serviceButton": f"/html/body/div[6]/div/div[2]/div/div/div[{self.option[0]}]/div/button",
            "serviceMessage": f"/html/body/div[{self.option[1]}]/div/div/span[2]", 
        }

    def double_check(self):
        sleep(1)
        for _ in range(6):
            text = self.driver.find_element(By.XPATH, xpathId["serviceTimer"]).text
            if text.startswith("Please wait"):
                print(text, "done")
                return text
            else:
                print(text, "error")
                sleep(1)

    def cloudfare_bypass(self):
        self.driver.get("https://zefoy.com") # normally this flag but cloudfare go to eat poop
        self.captcha_solver()
        self.automating_zefoy()
        # CLOUDFARE SUDDENLY CLOSED
        # solved = False
        # while True:
        #     self.driver.execute_script('window.open("https://zefoy.com");') # Flagged: self.driver.switch_to.window(self.driver.window_handles[1]) self.driver.get("https://zefoy.com")
        #     sleep(5) # Takes so time bro 5-8 seconds | fastest 3 slowest 14
        #     self.driver.close()
        #     self.driver.switch_to.window(self.driver.window_handles[0])

        #     try: 
        #         self.driver.find_element(By.XPATH, xpathId["webTest"])
        #     except: 
        #         self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/iframe"))
        #         for _ in range(5):
        #             try: 
        #                 self.driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/label/input").click()
        #                 break
        #             except: 
        #                 sleep(1)
        #                 continue

        #     for _ in range(3000):
        #         if str(self.driver.title) != "Just a moment...":
        #             solved = True
        #             break
        #     if solved == True:
        #         self.captcha_solver()
        #         self.automating_zefoy()
        #     else:
        #         solved = False
    
    def image_recoginizer(self, image):
        response = post(
            url = "https://api.api-ninjas.com/v1/imagetotext",
            files = {
                "image":image
            },
            headers={
                "Origin":"https://api-ninjas.com",
                "Referer":"https://api-ninjas.com/"
            }
        )
        try:
            response = list(response.json())
            response = dict(response[0])
            return response["text"]
        except:
            self.image_recoginizer(image) # can improve it to while loop

    def transfer_textime(self, text):
        print(int(text.split("Please wait ")[1].split(" minute(s)")[0])*60+int(text.split("minute(s) ")[1].split(" seconds")[0]))
        return int(text.split("Please wait ")[1].split(" minute(s)")[0])*60+int(text.split("minute(s) ")[1].split(" seconds")[0])

    def captcha_solver(self):
        while True:
            captcha = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.xpathId["textCaptcha"]))).screenshot('image.png')
            captcha = self.image_recoginizer(bytes(bytearray(open("image.png", "rb").read())))
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.xpathId["textInput"]))).send_keys(captcha.lower())
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.xpathId['textButton']))).click()
            try:
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpathId["textWrong"])))
                self.driver.refresh()
            except:
                break
    
    def automating_zefoy(self):
        try: WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.xpathId["serviceButton"])))
        except: exit()

        while True:
            self.driver.get("https://zefoy.com")
            try:
                self.driver.find_element(By.XPATH, xpathId["textCaptcha"])
                self.driver.refresh()
                self.captcha_solver()
            except:
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.xpathId['serviceButton']))).click()
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.xpathId['serviceInput']))).send_keys(videoId)
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.xpathId['serviceSearch']))).click()
                try:
                    sleep(2) # wait 2-3
                    self.timer = self.transfer_textime(self.double_check())
                    sleep(self.timer)
                except:
                    try:
                        counts = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.xpathId["serviceConfirm"]))).text
                        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.xpathId["serviceConfirm"]))).click()
                        sleep(3)
                        self.timer = self.transfer_textime(self.double_check())
                        sent = self.driver.find_element(By.XPATH, self.xpathId["serviceMessage"]).text
                        sleep(self.timer) 
                    except:
                        self.driver.refresh()
                        self.captcha_solver()

ZefoyAutomater("views").cloudfare_bypass()

