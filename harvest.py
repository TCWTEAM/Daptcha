import requests
import json
from proxybroker import Broker
import asyncio
import threading
import random
from random import *
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from time import sleep

proxyArr = []
tck = []
ack = []

with open("settings.json") as file:
    settings = json.load(file)

async def save(proxies, filename):
    """Save proxies to a file."""
    with open(filename, 'w') as f:
        while True:
            proxy = await proxies.get()
            if proxy is None:
                break
            proto = 'https' if 'HTTPS' in proxy.types else 'http'
            row = '%s://%s:%d\n' % (proto, proxy.host, proxy.port)
            f.write(row)


def grab(limit):
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    tasks = asyncio.gather(broker.find(types=['HTTP', 'HTTPS'], limit=int(limit)),
                           save(proxies, filename='proxies.txt'))
    loop = asyncio.get_event_loop()

def tc():
    while True:
        proxy = proxyArr[randint(0, len(proxyArr) - 1)]
        proxy = {'http': 'http://' + proxy, 'https': 'https://' + proxy}
        url = settings['url']
        site_key = settings['sitekey']
        API_KEY = tck[randint(0, len(tck) - 1)]
        s = requests.Session()
        try;
            captcha_id = s.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(API_KEY, site_key, url), proxies=proxy).text.split('|')[1]
            # then we parse gresponse from 2captcha response
            recaptcha_answer = s.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id), proxies=proxy).text
            print("solving ref captcha...")
            while 'CAPCHA_NOT_READY' in recaptcha_answer:
                sleep(5)
                recaptcha_answer = s.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id), proxies=proxy).text
            recaptcha_answer = recaptcha_answer.split('|')[1]
            capto = "[={}=]".format(recaptcha_answer)
            with open("tokens.txt", "a+") as f:
                f.write("{}\n".format(capto))
            print("SOLVED")
        except:
            print("error in 2captcha thread")
def anti():
    while True:

        api_key = ack[randint(0, len(ack) - 1)]
        print(api_key)
        site_key = settings['sitekey']
        url = settings['url']
        try:
            client = AnticaptchaClient(api_key)
            task = NoCaptchaTaskProxylessTask(url, site_key)
            job = client.createTask(task)
            print("solving anti captcha")
            job.join()
            capto = job.get_solution_response()
            capto = "[={}=]".format(capto)
            with open("tokens.txt", "a+") as f:
                f.write("{}\n".format(capto))
            print("solved")
        except:
            print("error in anticaptcha thread")
if __name__ == '__main__':
    print("________                 __         .__            ")
    print("\______ \ _____  _______/  |_  ____ |  |__ _____   ")
    print(" |    |  \\__  \ \____ \   __\/ ___\|  |  \\__  \  ")
    print(" |    `   \/ __ \|  |_> >  | \  \___|   Y  \/ __ \_")
    print("/_______  (____  /   __/|__|  \___  >___|  (____  /")
    print("        \/     \/|__|             \/     \/     \/ ")
    print("")
    print("+-" * 24)
    print("Daptcha BY XO FOR C3WSI")
    print("Github Repo https://github.com/TCWTEAM/Daptcha")
    print("Twitter @ehxohd")
    print("Discord XO#0001")

    print("+-" * 24)
    print("DAPTCHA HARVEST")
    limit = input("Proxy Amount?: ")
    grab(limit)
    with open("proxies.txt", "r") as file:
        for line in file:
            proxy = line.split("://")[1].replace("\n", "")
            proxyArr.append(proxy)
    threadn = input("Amount Of Threads: ")
    #replace dilameters
    if len(settings['acks']) < 3:
        print("No Anticaptcha Keys")
    elif "," not in settings['acks']:
        ack.append(settings['acks'].replace("\n", ""))
        for i in range(int(2)):
            t = threading.Thread(target=anti)
            t.start()
    else:
        for akey in settings['acks'].split(","):
            ack.append(akey.replace("\n", ""))
            for i in range(int(threadn)):
                t = threading.Thread(target=anti)
                t.start()

    if len(settings['tcks']) < 3:
        print("No 2Captcha Keys")
    elif "," not in settings['tcks']:
        tck.append(settings['tcks'].replace("\n", ""))
        for i in range(int(2)):
            t = threading.Thread(target=tc)
            t.start()
    else:
        for akey in settings['tcks'].split(","):
            tck.append(akey.replace("\n", ""))
            for i in range(int(threadn)):
                t = threading.Thread(target=tc)
                t.start()
