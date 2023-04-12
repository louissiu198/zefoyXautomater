import selenium, time, random, requests
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
        self.driver = None
        self.video = input("(?) VIDEOID  ")
        self.works = []
        self.false = []

    def setup(self):
        global driver
        self.options.add_argument("--headless")
        self.video = f"https://www.tiktok.com/@{random.randint(10000,99999)}user{random.randint(10000,99999)}/video/" + self.video
        self.options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(),
            options=self.options
        )
        driver.get("https://zefoy.com")
        self.solve()
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/form/div/div/div/input'))).send_keys(captcha)
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/form/div/div/div/div/button'))).click()
        """
        driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/form/div/div/div/input").send_keys(captcha)
        driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/form/div/div/div/div/button").click()
        """
    def solve(self):
        #captcha = input("(?) CAPTCHA    ")
        while True:
            captcha = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/form/div/div/img')
            captcha.screenshot('image.png')
            response = requests.post(
                url="https://api.api-ninjas.com/v1/imagetotext",
                files = {
                    'image': open("image.png", 'rb')
                },
                headers={
                    "X-Api-Key": "zvqy05NKzJMuouwKtewfPw==aEmBwzl8nD8s47QO",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
                }
            )
            captcha = response.text.split('[{"text": "')[1]
            captcha = captcha.split('", "bounding_box"')[0] # Line 48 (Could change) This part I think json response can do all of that, didn't tried whatever
            print("(!) Solved " + captcha)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/form/div/div/div/input'))).send_keys(captcha.lower())
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/form/div/div/div/div/button'))).click()
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="errorcapthcaclose"]/div/div')))
                #driver.find_element(By.XPATH, '//*[@id="errorcapthcaclose"]/div/div')
                print("(-) Captcha Incorrect")
                driver.refresh()
            except:
                print("(+) Captcha Passed")
                break
    def start(self):
        global video
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div[2]/div/div/div[5]/div/button'))).click()
            #driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div/div/div[5]/div/button").click()
            print("(+) VIEWS WORKING")
        except:
            print("(-) VIEWS BROKEN")
            exit()
        while True:
            driver.get("https://zefoy.com")
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div[2]/div/div/div[5]/div/button'))).click()
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[10]/div/form/div/input'))).send_keys(self.video)
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[10]/div/form/div/div/button'))).click()
            """
            driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div/div/div[5]/div/button").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "/html/body/div[10]/div/form/div/input").send_keys(video)
            driver.find_element(By.XPATH, "/html/body/div[10]/div/form/div/div/button").click()
            """
            try:
                time.sleep(3)
                timer = driver.find_element(By.XPATH, '//*[@id="gettimesv"]').text
                min = timer.split("Please wait ")[1]
                min = min.split(" minute(s)")[0]
                sec = timer.split("minute(s) ")[1]
                sec = sec.split(" seconds")[0]
                print("(-) TIMER " + min + " Minutes " + sec + " Seconds")
                time.sleep(int(min)*60+int(sec)) # Timer calculation
            except Exception as e:
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="c2VuZC9mb2xeb3dlcnNfdGlrdG9V"]/div[1]/div/form/button'))).click()
                #driver.find_element(By.XPATH, '//*[@id="c2VuZC9mb2xeb3dlcnNfdGlrdG9V"]/div[1]/div/form/button').click()
                print("(+) SUCCESS VIEW SENT    (Estimate 1000)")
                time.sleep(5)
                timer = driver.find_element(By.XPATH, '//*[@id="gettimesv"]').text
                #timer = driver.find_element(By.XPATH, '').text
                min = timer.split("Please wait ")[1]
                min = min.split(" minute(s)")[0]
                sec = timer.split("minute(s) ")[1]
                sec = sec.split(" seconds")[0]
                print("(+) TIMER " + min + " Minutes " + sec + " Seconds")
                time.sleep(int(min)*60+int(sec)) # Timer calculation
zefoy = ZEFOY()
zefoy.setup()
zefoy.start()

