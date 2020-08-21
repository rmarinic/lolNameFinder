from lxml import html
import requests
import re

URL = "https://lolnames.gg/en/"
PATH = "/html/body/div/div[2]/div/div/h4"
REGIONS = 'eune/', 'euw/', 'na/'

i = -1
searching = True
while searching:
    i += 1
    URL = "https://lolnames.gg/en/"
    URL += REGIONS[i]
    print("REGION: " + REGIONS[i])
    with open('words.txt') as fp:
        word = fp.readline()
        cnt = 1
        while word:
            fullUrl = URL + word.strip()
            page = requests.get(fullUrl)
            tree = html.fromstring(page.content)
            result = tree.xpath('/html/body/div/div[2]/div/div/h4/text()')
            daysLeft = re.findall("\d+", result[0])
            if daysLeft:
                if int(daysLeft[0]) < 20:
                    print(result)
            else:
                print(result)
            word = fp.readline()
            cnt += 1
        if(i >= 2):
            searching = False

