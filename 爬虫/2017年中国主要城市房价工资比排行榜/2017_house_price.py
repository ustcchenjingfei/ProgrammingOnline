import requests
import bs4
import re
import openpyxl


def open_url(url):
    # 使用代理
    # proxies = {'http':"127.0.0.1:1080,'https':"127.0.0.1:1080"}
    userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3528.4 Safari/537.36'
    headers = {'user-agent': userAgent}
    # res = requests.get(url,headers=headers,proxies=proxies)
    res = requests.get(url, headers=headers)

    return res


def find_data(res):
    data = []
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    content = soup.find(id="Cnt-Main-Article-QQ")  # 该id是唯一的
    targets = content.find_all("p", style="TEXT-INDENT: 2em")
    targets = iter(targets)  # 转换为迭代器

    for each in targets:
        if each.text.isnumeric():
            data.append([
                re.search(r'\[(.+)\]', next(targets).text).group(1),
                re.search(r'\d.*', next(targets).text).group(),
                re.search(r'\d.*', next(targets).text).group(),
                re.search(r'\d.*', next(targets).text).group()])
    return data


def to_excel(data):
    wb = openpyxl.Workbook()
    wb.guess_types = True
    ws = wb.active
    ws.append(['城市', '平均房价', '平均工资', '房价工资比'])

    for each in data:
        ws.append(each)

    wb.save('2017年中国主要城市房价工资比排行榜.xlsx')


def main():
    url = 'https://news.house.qq.com/a/20170702/003985.htm'
    res = open_url(url)
    data = find_data(res)
    to_excel(data)


if __name__ == '__main__':
    main()
