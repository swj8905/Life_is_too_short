from easy_crawling.bs4 import *

price = get_elements_list("https://finance.naver.com/marketindex/", "ul#exchangeList span.value")
for i in price:
    print(i.text)
