from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup,NavigableString
from collections import Counter
import json
#url_1=requests.get('https://biz.nv.ua/ukr/markets/naybagatshi-lyudi-svitu-hto-ocholyuye-reytingi-bagatijiv-u-svojih-krajinah-50193788.html')
url = urlopen('https://bank.gov.ua')
soup = BeautifulSoup(url.read(), 'html.parser')

def ex1():
    title_list = soup.find_all('title')
    print(title_list)  # 1 way
    print(soup.title)  # 2 way
    for i in title_list:  # 3 way
        print(i.get_text())

def ex_2():
    paragraph_list = soup.find_all('p')
    text = []
    for i in paragraph_list:
        text.append(i.get_text())
    print(text)

def ex3():
    paragraph_list = soup.find_all('p')
    text = []
    for i in paragraph_list:
        text.append(i.get_text())
    print(len(text))

def ex4():
    paragraph_list = soup.find_all('p')
    text = []
    for i in paragraph_list:
        text.append(i.get_text())
    print(text[0])

def ex5():
    h2_arr = []
    h2_list = soup.find_all('h2')
    for i in h2_list:
        h2_arr.append(i.get_text())
    print(len(h2_arr[0]))

def ex6_7():
    a_arr = []
    a_href = []
    a_list = soup.find_all('a')
    for i in a_list:
        a_arr.append(i.get_text())
        a_href.append(i.get('href'))
    print(a_arr[0])
    print(a_href[0])

def ex8():
    url_arr = []
    url_list = soup.find_all('li')
    for i in url_list:
        url_arr.append(i.get('http'))
    print(url_arr)

def ex9():
    h2_arr = []
    h2_list = soup.find_all('h2')
    for i in h2_list:
        h2_arr.append(i.get_text())
    print(h2_arr[0:4])

def ex10():
    a_arr = []
    a_list = soup.find_all("a")
    for i in a_list:
        a_arr.append(i.get_text())
    print(a_arr[0:10])

def ex11():
    h1_list = [element for element in soup.find_all("h1")]
    h2_list = [element for element in soup.find_all("h2")]
    h3_list = [element for element in soup.find_all("h3")]
    print(h1_list)
    print(h2_list)
    print(h3_list)

def ex12():
    txt = []
    txt_list = soup.find_all("html")
    for i in txt_list:
        txt.append(i.get_text())
    print(txt)
    #print(soup.text)


def ex13():
    print(set(i.name for i in soup.find_all()))


def ex14():
    rez=set()
    for i in soup.findAll(True):
        if i.name!='html':
            rez.add(i.name)
    print(rez)

def ex15():
    print(soup.body.contents)


def ex16():
    print(soup.head.contents)


def ex17():
    li_list=[i for i in soup.find_all("li")]
    print(li_list)


def ex18():
    inp=input("Write str")
    for i in soup.find_all():
        if inp in i.text:
            print(i)


def ex19():
    inp=input("Write id")
    print(soup.find(id=inp))


def ex20():
    inp=input("Write attribute")
    print(soup.find((inp)[0]))



# print(soup.head.contents)
# conn=requests.get(url)
# page=conn.text
# doc=soup(page)
# print(doc)
# link=[element.get("title") for element in doc.find_all("html")]
# print(link)
# links=[]
# for element in doc.find_all("html"):
#     links.append(element.get_text("title"))
#     print(links.get_text())


def ex21():
    div_cont=soup.find('div')
    # print(div_cont)
    for i in div_cont.find_all('label'):
        print(i)
        print()

def ex22():
    css_find=soup.select('label')
    print(css_find)

def ex23():
    i=input("write txt")
    tg=soup.find(text='A1')
    tg=soup.replaceWith(i)



privat_url = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5').json()
name_liist = []
buy_list = []
sale_list = []
for i in privat_url:
    name_liist.append(i['ccy'])
    buy_list.append(i['buy'])
    sale_list.append(i['sale'])
dict_of_money = dict(zip(name_liist, zip(buy_list, sale_list)))
print(type(dict_of_money['USD'][0]))
name = "USD"


class Convert():

    def Converting(self, name, value):
        self.value = int(value)
        self.name = name
        self.buy = float(dict_of_money[self.name][0])
        self.sale = float(dict_of_money[self.name][1])
        print(type(dict_of_money[self.name][0]))

    def UAH_USD_info(self):
        rez=self.value/(self.buy)
        return f"Your convert is UAH<>{self.name}. For {self.value} UAH you can buy  {rez} {self.name}"

    def USD_UAH_info(self):
        rez = self.value/self.sale
        return f"Your convert is {self.name}<>UAH. You need {rez} {self.name} to buy {self.value} UAH"


us = Convert()
us.Converting("EUR", 150000)
print(us.UAH_USD_info())
print(us.USD_UAH_info())
