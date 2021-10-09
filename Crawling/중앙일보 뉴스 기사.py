from easy_crawling.bs4 import *

keyword = input("키워드 입력 >> ")
encoded = par.quote(keyword) # 한글 -> 특수한 문자

page_num = 1
while True:
    url = f"https://www.joongang.co.kr/_CP/496?keyword={encoded}&sort%20=&pageItemId=439&page={page_num}"
    title = get_elements_list(url, "h2.headline a")
    if len(title) == 0:
        break
    for i in title:
        print("제목 :", i.text.strip())
        print("링크 :", i.attrs["href"])
        content = get_elements_list(i.attrs["href"], "div#article_body")
        result = content[0].text.strip()
        print(result)
        print()
    page_num += 1