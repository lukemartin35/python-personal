import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup =bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span7.a-text-right.a-span-last > span.a-size-medium a-color-price header-price')
    return elems[0].text.strip()

price = getAmazonPrice('http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/')
print("The price is" + price)
#res = requests.get('http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/')
#res.raise_for_status()
#soup: BeautifulSoup = bs4.BeautifulSoup(res.text, 'html.parser')
#elems = soup.select('#mediaNoAccordion > div.a-row > div.a-column.a_span7.a-text-right.a-span-last > span.a-size-medium a-color-price header-price')
#elems[0].text.strip()