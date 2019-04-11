import requests
import bs4
import pandas as pd
import tabulate

tabulate.PRESERVE_WHITESPACE = True  # 保留空格

pd.set_option('display.max_rows', None)  # 打印完整信息
pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', 100)

pd.set_option('display.unicode.ambiguous_as_wide', True)  # 对齐
pd.set_option('display.unicode.east_asian_width', True)

url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
headers = {'user-agent': userAgent}  # 伪装成Chrome浏览器，解决反爬虫

res = requests.get(url, headers=headers)
res.encoding = 'utf8'
soup = bs4.BeautifulSoup(res.text, "html.parser")

# university rank
rank = []
targets = soup.find_all("tr", class_="alt")
for each in targets:
    rank.append(each.td.text)

# university name
name = []
targets = soup.find_all("div", align="left")
for each in targets:
    name.append(each.text)

# university city
city = []
targets = soup.find_all("div", align="left")
for each in targets:
    city.append(each.parent.next_sibling.text)

# university score
score = []
targets = soup.find_all("div", align="left")
for each in targets:
    score.append(each.parent.next_sibling.next_sibling.text)

result = []
result.append(rank)
result.append(name)
result.append(city)
result.append(score)
columns = ['排名', '学校名称', '省市', '总分']

result_dict = dict(zip(columns, result))
df = pd.DataFrame(result_dict)

# md = tabulate.tabulate(df, tablefmt="grid", headers="keys", showindex=False)
# print(md)

df.to_csv(r"ChineseUniversityRank.csv", header=True, index=False, encoding='gbk')  # 输出csv文件
