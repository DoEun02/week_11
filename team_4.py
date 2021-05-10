import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

source = requests.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun='). text
soup = BeautifulSoup(source, 'html.parser')
data = soup.find_all('table')

data_tbody = data[0].find_all('tbody')

data_tbody_tr = data_tbody[0].find_all('tr')
maindata = []
count=0
print('지역'+' : '+'확진환자수')
for x in data_tbody_tr:
    count+=1
    if count==1:
        continue
    elif count == 19:
        break
    subdata = []
    td = x.find_all("td")
    th = x.find('th').get_text()
    subdata.append(th)
    name = 0
    num = 0
    for content in td:
        num+=1
        name+=1
        if name==1:
            print(th, end=' : ')
        elif num == 4:
            print(content.get_text().strip())
        elif num == 7:
            num = 0
        subdata.append(content.get_text())
    maindata.append(subdata)
up = []
area = []
for x in maindata:
    up.append(x[1])
    area.append(x[0])

x = range(len(area))

plt.rc('font', family='Malgun Gothic')
plt.bar(x, up)
plt.ylabel('전일대비 확진자수 증가')
plt.title('COVID-19')
plt.xticks(x, area)
plt.show()