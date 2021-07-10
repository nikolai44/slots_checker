import requests
from time import sleep
from playsound import playsound
from datetime import datetime

i = 0


def checker():
    global i
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cookie': 'user.id=NTkyMzU%3D--ce0b06474b7fc6420b73550460215a351cb49e0f; _intra_42_session_production=5a7e5d9d7ec949a3fce6708f17f73586',
        'Host': 'projects.intra.42.fr',
        'If-None-Match': "4f53cda18c2baa0c0354bb5f9a3ecbe5",
        'Referer': 'https://projects.intra.42.fr/projects/piscine-python-data-science-day-08/slots?team_id=3611783',
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
        'X-CSRF-Token': '8y3kWFVkrk+CDxgfNwJLdgFuImYB/N43UPq1VAh9CMHsWi1qKNDbLcHwNG/xgij589Za63m5ItH0dHFpuceGAg=='
    }

    r = requests.get('https://projects.intra.42.fr/projects/piscine-python-data-science-day-08/slots.json?team_id=3606732&start=2021-07-05&end=2021-07-12',
                     headers=headers)
    print(datetime.now(), r, r.text)
    i += 1
    if r.text != '[]':
        playsound("music.mp3")
        sleep(100)


if __name__ == '__main__':
    while True:
        checker()
        sleep(3)


