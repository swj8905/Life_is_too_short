from easy_crawling.bs4 import *


page_num = 1
while True:
    url = "https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Used&KeyWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&KeyLastWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&ViewRowCount=25&page={}".format(page_num)
    title, price = get_elements_list(url, "a.bo3 > b", "a.bo_used > b")
    if len(title) == 0: # 끝 페이지까지 크롤링 모두 완료했다면?
        break
    for i in range(len(title)):
        print(title[i].string, price[i].string)
    page_num += 1