import threading
import json
import requests
from flask import Flask, request, jsonify, render_template, redirect
from sys import platform
import socket
import time

with open("settings.json") as f:
    settings = json.load(f)


app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    token = request.form['g-recaptcha-response']
    postToken = "[={}=]".format(token)
    with open("tokens.txt", "a+") as f:
        f.write("{}\n".format(postToken))
    return redirect('/')
@app.route('/')
def home():
    counta = 0
    with open("tokens.txt", "r") as file:
        for line in file:
            counta += 1
    return render_template('captcha.html', sitekey=settings['sitekey'], site=settings['url'], count=counta)

@app.route('/fetch')
def fetch():
    tokenArr = []
    pa = []
    with open("tokens.txt", "r") as file:
        for line in file:
            cap = line.split("[=")[1].split("=]")[0].replace("\n", "")
            tokenArr.append(cap)

    if len(tokenArr) < 1:
        return "None Available"
    else:
        tok = str(tokenArr[0])
        tokenArr.remove(tok)
        for toke in tokenArr:
            tokea = "[={}=]".format(toke)
            pa.append(tokea)
        with open("tokens.txt", "w+") as f:
            for t in pa:
                f.write("{}\n".format(t))
        return tok

@app.route('/total')
def total():
    count = 0
    with open("tokens.txt", "r") as f:
        for line in f:
            count += 1

    return str(count)

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
    print("DAPTCHA SERVER")
    print("")
    if platform == "darwin":
        hostdir = "/etc/hosts"
    else:
        hostdir = "C:\Windows\System32\drivers\etc\hosts"

    baseurl = settings['url'].split("://")[1]
    baseurl = "daptcha.{}".format(baseurl)
    hostenturl = "127.0.0.1       {}".format(baseurl)
    with open(hostdir, "a+") as file:
        if hostenturl in file.read():
            dfosijgf = "dfuhfghfg"
        else:
            file.write("{}\n".format(hostenturl))
    #with open(hostdir, "r") as f:
    #    print(f.read())
    print("running harvester at {}:5000".format(hostenturl))
    ask = input("Would you like to clear existing tokens? (y/n): ")
    if ask.lower() == "y":
        with open("tokens.txt", "w+") as f:
            f.write("")
    app.run()
