import selinium
from bs4 import BeautifulSoup
from a_email_alert import alert_system
from threading import Timer

URL = "https://www.amazon.in/dp/B09N3ZNHTY/ref=s9_acsd_al_bw_c2_x_0_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-6&pf_rd_r=WR012SR5N0BDES57RFEX&pf_rd_t=101&pf_rd_p=5ab7a50c-a46c-4f47-99a0-316b033635ee&pf_rd_i=976419031"

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'DNT' : '1', # Do Not Track Request Header
'Connection' : 'close'
}

set_price = 1000

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    product_title = str(title)
    product_title = product_title.strip()
    print(product_title)
    price = soup.find(id='priceblock_ourprice').get_text()
    # print(price)
    product_price = ''
    for letters in price:
        if letters.isnumeric() or letters == '.':
            product_price += letters
    print(float(product_price))
    if float(product_price) <= set_price:
        alert_system(product_title, URL)
        print('sent')
        return
    else:
        print('not sent')
    Timer(60, check_price).start()

check_price()