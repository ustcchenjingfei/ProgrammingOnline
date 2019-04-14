import requests
import bs4
import openpyxl


def open_url(url):
    # 使用代理
    # proxies = {'http':"127.0.0.1:1080,'https':"127.0.0.1:1080"}
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3528.4 Safari/537.36'}
    # res = requests.get(url,headers=headers,proxies=proxies)
    res = requests.get(url, headers=headers)

    return res


def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # 电影名
    movies = []
    targets = soup.find_all("div", class_="hd")
    for each in targets:
        movies.append(each.a.span.text)

    # 评分
    ranks = []
    targets = soup.find_all("span", class_="rating_num")
    for each in targets:
        ranks.append(each.text)

    # 资料
    messages = []
    targets = soup.find_all("div", class_="bd")
    for each in targets:
        try:
            messages.append(each.p.text.split('\n')[1].strip() + each.p.text.split('\n')[2].strip())
        except:
            continue

    result = []
    length = len(movies)
    for i in range(length):
        result.append([movies[i], ranks[i], messages[i]])

    return result


# 找出一共有多少个页面
def find_depth(res):
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    depth = soup.find('span', class_='next').previous_sibling.previous_sibling.text

    return int(depth)


def save_to_excel(result):
    workbook = openpyxl.Workbook()  # 创建工作簿 （工作簿、工作表、单元格）
    worktable = workbook.active  # 创建工作表

    worktable['A1'] = "电影名称"
    worktable['B1'] = "评分"
    worktable['C1'] = "详情"

    for each in result:
        worktable.append(each)

    workbook.save('豆瓣TOP250电影.xlsx')


def main():
    host = 'https://movie.douban.com/top250'
    res = open_url(host)
    depth = find_depth(res)
    result = []

    for i in range(depth):
        url = host + '/?start=' + str(25 * i)  # 原url中的filter为空，可忽略
        res = open_url(url)
        result.extend(find_movies(res))

    # with open('豆瓣TOP250电影.txt', 'w', encoding='utf-8') as f:
    #     for each in result:
    #         f.write(each)
    save_to_excel(result)


if __name__ == '__main__':
    main()
