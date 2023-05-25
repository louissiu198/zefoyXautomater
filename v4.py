import urllib.parse
import requests
import base64
import random
import time 

PHPSESSID = ""
cf_id = ""
ab00830585c603720b68ddd6a5ef99fda3caa18b = ""

baseHeaders = {
    "upgrade-insecure-requests:": "1",
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36" 
}

def getSpilited(decrypted_string):
    server_settime = decrypted_string.split("var ltm=")[1].split(";")[0]
    server_message = decrypted_string.split("$('.views-countdown').html('")[1].split("');")[0]
    try:
        server_sent = decrypted_string.split("<span style='font-size:110%;font-weight:bold;font-family:Arial, Helvetica, sans-serif;text-align:center;color:green;'>")[1].split("</span>")[0]
        print(server_sent)
        if server_message == "Please wait '+me+' minute(s) '+se+' seconds for your next submit!":
            time.sleep(int(server_settime))
    except:
        if server_message == "Please wait '+me+' minute(s) '+se+' seconds for your next submit!":
            time.sleep(int(server_settime))

def getCookies():
    response = requests.get(
        url = "https://zefoy.com",
        headers = baseHeaders
    )
    
    if response.status_code == 200:
        PHPSESSID = response.cookies["PHPSESSID"]
        cf_id = response.cookies["cf_id"]
        ab00830585c603720b68ddd6a5ef99fda3caa18b = response.cookies["ab00830585c603720b68ddd6a5ef99fda3caa18b"]
    else:
        print("(!) Error")
        exit()

    response = response.text
    response = response.replace("&amp", "&")
    captcha_image = response.split('img src="')[0].split('"')[0]
    return captcha_image, response

def getCaptcha(captcha_image):
    del baseHeaders["upgrade-insecure-requests"]
    baseHeaders["cookie"] = f"PHPSESSID={PHPSESSID}; cf_id={cf_id}; ab00830585c603720b68ddd6a5ef99fda3caa18b={ab00830585c603720b68ddd6a5ef99fda3caa18b}"

    response = requests.get(
        url = "https://zefoy.com" + captcha_image,
        headers = baseHeaders
    )

def getVerified(website):
    firstA = website.split('<input type="hidden" name="')[1]
    firstA1 = firstA.split('" value="')[0]
    firstA2 = firstA.split('" value="')[1].split('">')[0]

    secondA = website.split('<input type="hidden" name="')[2]
    secondA1 = secondA.split('" value="')[0]
    secondA2 = secondA.split('" value="')[1].split('">')[0]   

    thirdA = website.split('<input type="hidden" name="')[3]
    thirdA1 = thirdA.split('" value="')[0]
    thirdA2 = thirdA.split('" value="')[1].split('">')[0]    

    response = requests.post(
        url = "https://zefoy.com",
        headers = baseHeaders,
        data = {
            f"{firstA1}": f"{firstA2}",
            f"{secondA1}": f"{secondA2}",
            f"{thirdA1}": f"{thirdA2}",
            "token": "",
        }
    )

    response = response.text
    checking = checking.split('<p class="card-text"><small class="badge badge-round badge-warning d-sm-inline-block">')[1]
    checking = checking.split("</small></p>")[0]
    multitok = response.split('<input type="search" class="form-control text-center font-weight-bold rounded-0 remove-spaces" name="')[1].split('" placeholder')[0]
    print(checking)

def getService(videoId):
    reqtoken = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=16)) # Thanks for tekky idk how to do with this honestly
    response = requests.post(
        url = "https://zefoy.com" + "/c2VuZC9mb2xeb3dlcnNfdGlrdG9V",
        headers = baseHeaders,
        data = f'------WebKitFormBoundary{reqtoken}\r\nContent-Disposition: form-data; name="{token}"\r\n\r\n{videoId}\r\n------WebKitFormBoundary{reqtoken}--\r\n'
    ) 
    decrypted = getDecryption(response.text)
    getSpilited(decrypted)
    



def getDecryption(data):
    response = urllib.parse.unquote(data[::-1])
    return base64.b64decode(response).decode()

print(getDecryption("D3%D3%gPuFGcz9CPuQnblNHIzdXZpZHIwADMxASesxWdmN3clN2Y1NlPnsjblVmcnpjcvx2bjtjclRnblNmOudWasFWL0hXZ0tjZpJXZz1ycuF2cgwSYjlGdlZHblhEIswWYpJXQ6kHbp1WYm1Cdu9mZ7QGbvJmO0h2ZpV2dtQnbvZ2OlATMxoTZ6l2ctQnbvZ2J9UGb5R3cg4WYwNHPK4jbhB3cvwjLu4icl1WaUByZul2ajVGaD5zJ7USNxEjOlpXaz1Cdu9mZ7QGbvJmO0h2ZpV2dtQnbvZ2O3IWY3MzMjojcvx2bjtjclRnblNmOudWasFWL0hXZ0dSPlxWe0NHIn42dvRGduV3bj1yc3VWa2BCepZmchVGbjdSPzNXYsNGIuFGczxjCB2%QHcpJ3Yz9CPKsTKwATNs0nC9pwOpcSIu4iLukFRBVkUgoDdp1mY1NFI0hXZOdCKs1Gdo5SKn42dvRGduV3bj1yc3VWa25yJoQiC7kSb0R2YowWY2JXZ05WSyFWZsNmC7lCM9wTZzBiJmACM9wTZthiZppwOpcSI0lWbiV3cgQHel5GIyV3b5BicvZGIzRmbvNWZzByJrU2crcCIpMHKlRXdulWbgcyKl12KnACdpF2dgU2chVGbQdCKs1Gdo5SKn42dvRGduV3bj1yc3VWa25yJoQiC7kCM2UyayFmZoQnbJV2cyFGcg0DIlNHIyFmdKsTKwYzLrJXYmhCdulUZzJXYwBSPgUWbgIXY2pwOp0GdstSKtRnbt0GdzhCK9smchZGIyFmdKsTKwADMx8SKoc3bu5SZ0FGRoI3bvxmZugGdh1UPtRnbgIXY2pwepgibvlGdj5WdmhCbhZnclRnbJRXZz1Tb0R2YgIXY2pwO0ITM90GdsBichZnC7kCMwATMvkCK39mbuUGdhREKy92bsZmLoRXYN1Tb0NHIyFmdK4zJ0BXayN2chZXYq9Cd4VGdn0TZwlHdgQHcpJ3YzxjC"))















































# # import json
# # devices = open("devices.txt").read().splitlines()
# # print(len(devices))

# import requests
# import random
# import json

# def generateAccounts():
#     letters = "qwertyuiopasdfghjklzxcvbnm"
#     passwrd = "1234567890qwertyuiopasdfghjklzxcvbnm"
#     response = requests.post(
#         url = "https://proxy.webshare.io/api/v2/register/",
#         headers = {
#             "content-type":"application/json",
#             "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
#         },
#         json = {
#             "email": f"{''.join(random.choice(letters) for i in range(10))}@gmail.com",
#             "password": ''.join(random.choice(passwrd) for i in range(10)),
#             "tos_accepted": "true",
#             "recaptcha": "03AL8dmw8qohPrSWNOjwpTIStlYtj0P1G1fVg397S_7ZecZXZiUhKaAgWmQuX6Zng_I-aCxgv8vqB_XeKm8x6oS6IbNKSvJywI0u4lhxqjtrDnmliFTYBxf4VQ-B1fxaA6jY5bSuRaIup51LqG8EQnt5nM0ukuYwYrVUQp3RdjhRx5riSTMio64lsiguIeLBfkkKRdiTDHrXVpjbOOK1VhDXn9Z36j-aVUyCs1ak_owIc9oeWrymJ1-QxIMaN257lvnV1gMLBsx_ulXkbTtDQv2cDNl6csOypOIcbc3BQhuUl7wRactpBCSrmD4kYl059oh2dXbzcrfddXne4Ks0iOMgV2puZt3kpc95-_n5kGYXKZUfPecT-0oHzd4LyAeLfFho9j6MClD7cVmURzzz4V0Bpmb3vSNORhod347mLRiqXSQFSCCZlaxEBTjv1LzeF2JcG-bZOF5ANWfX4pXc2fkHIL483qSRapR8MI4Ukgus1LTVRP3DlSlFgG0U_cU9_f5M_GV_9-WMiY_VxVu_fgjOcmcjdiDc3BZUOx845xe58Ck4tPtBLAICuu2NX0HRzAEhClNDa3Lt8F"
#         }
#     )
#     token = response.json()["token"]
#     sessionid = response.cookies["sessionid"]
#     csrftoken = response.cookies["csrftoken"]
#     newDesignLoginToken = response.cookies["newDesignLoginToken"]
#     response = requests.post(
#         url = "https://proxy.webshare.io/api/v2/proxy/config/",
#         headers = {
#             "authorization":"Token " + token,
#             "cookie":f"sessionid={sessionid}; csrftoken={csrftoken}; newDesignLoginToken={newDesignLoginToken}",
#             "content-type":"application/json",
#             "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
#         }
#     )
#     response = response.json()
#     username = response["username"]
#     password = response["password"]
#     proxy_list_download_token = ["proxy_list_download_token"]
#     print(username, password, proxy_list_download_token)

# for i in range(len(devices)):
#     with open("domains.txt", "a") as f:
#         devices[i] = json.loads(devices[i])
#         device = str(devices[i]["data"])
#         f.write(device+"\n")
# lock = threading.Lock()

# def e():
#     lock.acquire()
#     print("e")
#     time.sleep(10)
#     lock.release()
# for i in range(10):

#     #{'message': 'You have exceeded the rate limit per minute for your plan, PRO, by the API provider'}
#     threading.Thread(target=e).start()
