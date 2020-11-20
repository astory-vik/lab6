import requests
from bs4 import BeautifulSoup

url = "https://news.liga.net/"
def main():
    html = GetHtml(url)
    soup = BeautifulSoup(html, "html.parser")
    link = []
    news = []
    link = soup.find_all("div", class_="news-nth-title")
    for i in link:
        news.append(i.find('a').text)
    for k in news:
        print("Количество слов в новосте " + str(len(set(k.split()))))
    numInt = []
    numInt = soup.find_all("a")
    print("Количество ссылок " + str(len(numInt)))
    print("Количество изображений " + str(len(soup.find_all("img"))))


def GetHtml(url):
    r = requests.get(url)
    if(r.status_code == 200):
        return r.text
    else:
        print("Fail")


if __name__ == '__main__':
    main()