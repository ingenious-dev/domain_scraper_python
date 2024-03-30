from utility import creating_and_viewing_html_files

import requests
from bs4 import BeautifulSoup

token = None
cookies = None

def scrape_kenyawebexperts_for_domains(domain):

    # domain = 'test.com'
    url = 'https://www.kenyawebexperts.co.ke/index.php'
    params = {
        'rp': '/domain/check', # ! REQUIRED
    }
    payload = {
        # 'token': token,
        # 'a': 'checkDomain',
        'domain': domain, # ! REQUIRED
        # 'type': 'domain',
    }
    headers = {
        # 'authority': 'www.kenyawebexperts.co.ke',
        # 'method': 'POST',
        # 'path': '/index.php?rp=/domain/check',
        # 'scheme': 'https',
        # 'Accept': '*/*',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        # 'Accept-Language': 'en-US,en;q=0.9,la;q=0.8,sm;q=0.7',
        # 'Content-Length': '88', # ! VARIABLE - set by http library
        # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '_ga=GA1.3.672913941.1690973673; cookielawinfo-checkbox-non-necessary=yes; viewed_cookie_policy=yes; twk_idm_key=X1VITrFiu_xdebgiW120T; __stripe_mid=3694a283-e88b-460a-98ad-6523660dea73f52cdb; WHMCSlogin_auth_tk=M2VmSlJBTUcvNGxXb0NDS3NLd1pYYXdId1V5Q3llOEdjbGdxQitWTnNKbDNRaGdaZUxsRWZxSWVydlhNUXFoL0RZdXY3ODFCNTJ3Y213L2VDODBaQTdmUDdBV0Eza3BPTGU1V2d4Zk5NVkFFVCt1elovYkx2WFRyODN4K0Q4alEvT1FhaFhrWlMvc2pQQ3V3OW05VnJwc0JRNXpVY1lwc2VFT3loSll2K0RSdldQeVBZUGUyM2s3cEhSZHRvUWZwQlZDUEZYaTlmT3cyM1BRWHhCY0gzbDVHVHpyNzRMSlQvWWZmbXBvQ0ZDT0l3Wkp2STQveWZSdmRDWW1LWm8zUVRXZ1YrODdYR3pTV0F4c01WM3lCMC9LWlgvaFhzbmoxRU02cDRheDlUaUJzNkdlMmhsU0NxTjc0ZCtnQ0NFNjNORGo2amdnRW5EYXd6bEJ1U2k3UXZsTmNOYVlEZXJaS1NZODExOWh1ZURHQ28rVUtXcHhQMm9Hb0hNQzk1WnhRdzRmTCtjWUFnU0VWTWtlaXJKUDhYZnZnR1NqdmVONWdvc2EyT1pJPQ%3D%3D; _gcl_au=1.1.1916729459.1706706805; WHMCSK6VIp9JjrYa7=626fd59e8ea91d2033fd7496ee5ccd6d; cookielawinfo-checkbox-necessary=yes; PHPSESSID=5b64a6e9b2a3756fd9f933d685b1dc68; _gid=GA1.3.1420072732.1711689684; trustedsite_visit=1; __stripe_sid=c8a03625-34fa-44b9-a26e-3031d39cc00ab5c109; _ga_TFFNV4XPPQ=GS1.3.1711711159.51.1.1711711265.0.0.0; TawkConnectionTime=0; twk_uuid_5cd26e15d07d7e0c639274a5=%7B%22uuid%22%3A%221.bJp44ssXtvSVKplAdnRomu82OrrQkagcsHp5ZZ6zM8sqTE7YTvFId0IrmDx9W9xOxJNpuB7ajVYRvX9OCVbaY2gPRa1G3rf5eem7Efcj279V3EBnhW8WkL9PuU5yt%22%2C%22version%22%3A3%2C%22domain%22%3A%22kenyawebexperts.co.ke%22%2C%22ts%22%3A1711711279399%7D',
        # 'Origin': 'https://www.kenyawebexperts.co.ke',
        # 'Referer': f'https://www.kenyawebexperts.co.ke/cart.php?a=add&domain=register&query={domain}',
        # 'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        # 'Sec-Ch-Ua-Mobile': '?0',
        # 'Sec-Ch-Ua-Platform': '"Windows"',
        # 'Sec-Fetch-Dest': 'empty',
        # 'Sec-Fetch-Mode': 'cors',
        # 'Sec-Fetch-Site': 'same-origin',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        # 'X-Requested-With': 'XMLHttpRequest',
    }
    # cookies = {
    #     '': '_ga=GA1.3.672913941.1690973673; cookielawinfo-checkbox-non-necessary=yes; viewed_cookie_policy=yes; twk_idm_key=X1VITrFiu_xdebgiW120T; __stripe_mid=3694a283-e88b-460a-98ad-6523660dea73f52cdb; _gcl_au=1.1.1916729459.1706706805; cookielawinfo-checkbox-necessary=yes; PHPSESSID=5b64a6e9b2a3756fd9f933d685b1dc68; _gid=GA1.3.1420072732.1711689684; WHMCSK6VIp9JjrYa7=c1fdce32c0adda9aa1e1259d2c25d046; trustedsite_visit=1; __stripe_sid=ff871698-b6fd-421a-8c6e-85b325d63420e75531; _ga_TFFNV4XPPQ=GS1.3.1711787538.54.0.1711787538.0.0.0; TawkConnectionTime=0; twk_uuid_5cd26e15d07d7e0c639274a5=%7B%22uuid%22%3A%221.bJp44ssXtvSVKplAdnRomu82OrrQkagcsHp5ZZ6zM8sqTE7YTvFId0IrmDx9W9xOxJNpuB7ajVYRvX9OCVbaY2gPRa1G3rf5eem7Efcj279V3EBnhW8WkL9PuU5yt%22%2C%22version%22%3A3%2C%22domain%22%3A%22kenyawebexperts.co.ke%22%2C%22ts%22%3A1711789298832%7D'
    # }

    r = requests.post(url,
        params=params,
        data=payload,
        headers=headers,
        # cookies=cookies,
    )
    # print(r.text)

    creating_and_viewing_html_files(r.text, None, None)

    if r.status_code == requests.codes.ok:
        if r.headers.get('Content-Type') == 'application/json':
            data = r.json()
            if data.get('result'):                
                # print(data['result'][0]['isRegistered'])
                return data['result']
            
    return []

if __name__ == "__main__":
    import xlwt

    book = xlwt.Workbook()
    sh = book.add_sheet('Kenya Web Experts')

    # lookup_domains = ['test.com']
    print('Checking domains.txt')
    domains_file = open('domains.txt')
    lookup_domains = [ x.replace('\n', '') for x in domains_file.readlines()]
    # print(lookup_domains)

    row_index = 0
    sh.write(row_index, 0, 'Domain')
    sh.write(row_index, 1, 'Status')
    sh.write(row_index, 2, 'Registration')
    sh.write(row_index, 3, 'Transfer')
    sh.write(row_index, 4, 'Renew')
    row_index += 1

    for domain in lookup_domains:
        results = scrape_kenyawebexperts_for_domains(domain)
        for result in results:
            sh.write(row_index, 0, result.get('domainName'))
            sh.write(row_index, 1, 'AVAILABLE' if result.get('isAvailable') else '-')
            sh.write(row_index, 2, result.get('pricing').get('1').get('register'))
            sh.write(row_index, 3, result.get('pricing').get('1').get('transfer'))
            sh.write(row_index, 4, result.get('pricing').get('1').get('renew'))
            row_index += 1

    book.save('results/domains.xls')
    print('See results/domains.xls for results')

# References
# https://realpython.com/beautiful-soup-web-scraper-python/#step-3-parse-html-code-with-beautiful-soup
# https://www.freecodecamp.org/news/how-to-read-a-file-line-by-line-in-python/
# https://stackoverflow.com/questions/13437727/how-to-write-to-an-excel-spreadsheet-using-python/13437772#13437772
