import requests
import json


def get_comments(url):
    name_id = url.split('=')[1]

    # proxies = {'http':"127.0.0.1:1080,'https':"127.0.0.1:1080"} # 使用代理

    userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3528.4 Safari/537.36'
    referer = 'https://music.163.com/song?id=27808044'
    params = 'rD7ZEsgmHwElITtfzTznG8pCEvGWODNrKhEzOtU05JBaY8fuEl5VfcPp0wiggmEjMK0egLauuNTPCUIv32rxJ4cJFrMNpa1PpGuOmYn3hoUH0bS9IbzsIrsGR18Z7fl1CmAQLCjgwgfV4fKoX2FgHH + J174dxWEez9cDF8zDSQuG7IKjXBQDIhuo8lhFS8hB'
    encSecKey = 'd92a459d2e5b8fdcc21e0b6ed3fd4bed90bce896dfe12bd089453cdec2be25101a40622270a11925f766d2ba8453108ab1ec02b0e891c2da22b86725869d776a23036bc7f46a9f488cdd44b89f73632fc0de05f81d583176de5c244c87513fcd2e6075fa3e36ef03df09b96b506293e0c70d1c5bd418154d04f18f53074f2627'

    data = {'params': params, 'encSecKey': encSecKey}

    headers = {'user-agent': userAgent, 'referer': referer}

    # 热门评论隐藏所在的url
    target_url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(name_id)

    # res = requests.get(url,headers=headers,proxies=proxies)
    res = requests.post(target_url, headers=headers, data=data)  # 使用post方式

    return res


def get_hot_comments(res):
    comments_json = json.loads(res.text)
    hot_comments = comments_json['hotComments']
    with open('hot_comments.txt', 'w', encoding='utf-8') as f:
        for each in hot_comments:
            f.write('用户名:' + each['user']['nickname'] + '\n')
            f.write('评论内容:' + each['content'] + '\n')
            f.write('---------------------------------------------\n\n')


def main():
    url = input('请输入链接地址:')
    # url = 'https://music.163.com/#/song?id=27808044'
    res = get_comments(url)

    # 调试
    # with open('网易云音乐热门评论.txt', 'w', encoding='utf-8') as f:
    #    f.write(res.text)

    get_hot_comments(res)


if __name__ == '__main__':
    main()
