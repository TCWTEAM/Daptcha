# Daptcha
## Made with love and python + nodejs (electron)

#### Disclamer
- This project was made for a program and is going to be used as a poc on the exploitability of recaptcha. This will not be constantly maintained and it is reccomended to try and purchase something like DISSOLVE if you can. I am not responsible for anything you do with this program.


#### Requirements
- NodeJS 
- Python 3.6+
- A computer and a brain

#### Installation 
##### This is fairly annoying and complicated so read carefully
- CD Into the folder containing this project
- type npm install to install the node packages
- Install the following pip packages (pip install or pip3 install ...)
    - Requests
    - Flask
    - proxybroker
    - python-anticaptcha
    - asyncio


#### Usage
##### This is even more annoying
- While CD into the folder type "electron ."
- Go to settings and fill in the info then press save. It is important to not put a "/" after the site url
- Once ready run server.py, with this running you are now able to harvest manually just by opening the manual harvester from the ui
- You may also run harvester.py to use anticaptcha 2captcha and soon death by captcha to collect tokens


#### API
- Url will always be http://daptcha.siteurl:5000
    - /fetch Method: GET [Will return the oldest captcha token]
    - /total Method: GET [Will return the amount of total tokens at the moment]

#### Sorry
Yes I know this is not easy to use and is mainly for developers but the main point of this was for me to submit to a program. I will implement this into all of my bots to make it easy for you guys to harvest captchas fast.

#### Help
- For issues please just open an issue on github
