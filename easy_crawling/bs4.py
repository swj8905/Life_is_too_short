from bs4 import BeautifulSoup
import urllib.request as req

def get_elements_list(url, *args):
    result = []
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    for css in args:
        result.append(soup.select(css))
    if len(result) == 1:
        return result[0]
    else:
        return result