from datetime import datetime

import aiohttp


async def get_zodiac_response(request_type, zodiac_type):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    }
    date = datetime.today().strftime("%Y-%m-%d")
    if request_type == ZODIAC_REQUEST.TODAY:
        url = f"https://astro.click108.com.tw/daily_0.php?iAstro={zodiac_type}&iAcDay={date}"
    elif request_type == ZODIAC_REQUEST.WEEK:
        url = f"https://astro.click108.com.tw/weekly_0.php?iAstro={zodiac_type}&iAcDay={date}&iType=1"
    else :
        url = f"https://astro.click108.com.tw/weekly_0.php?iAstro={zodiac_type}&iAcDay={date}&iType=2"
    res = requests.get(url, headers = headers)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        today_content = soup.find('div', {'class': 'TODAY_CONTENT'}).find_all('p')
        if request_type in (0, 1):
            for index in range(len(today_content)):
                if index %2 == 0:
                    today_content[index] = today_content[index].text[-6:-1].count('★')
                else:
                    today_content[index] = today_content[index].text
        else:
            for index in range(len(today_content)):
                if index in (0, 2, 6, 10):
                    today_content[index] = today_content[index].text[-6:-1].count('★')
                else:
                    today_content[index] = today_content[index].text
                
    today_content.insert(0, request_type)
    today_content.insert(0, zodiac_type)
    return today_content