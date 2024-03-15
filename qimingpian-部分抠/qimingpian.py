import requests
import execjs
import json

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.qimingpian.com',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

data = {
    'time_interval': '',
    'tag': '',
    'tag_type': '',
    'province': '',
    'lunci': '',
    'page': '1',
    'num': '20',
    'unionid': '',
}

response = requests.post('https://vipapi.qimingpian.cn/DataList/productListVip', headers=headers, data=data)

encrypt_data = response.json()['encrypt_data']

ctx = execjs.compile(open('JS_reverse/11-3-qimingpian-部分抠/qimingpian.js', 'r', encoding='utf-8').read())

# print(response.json())

# print(ctx.call('s', encrypt_data))

decrypt_data = ctx.call('s', encrypt_data)

formated_data = json.dumps(decrypt_data, indent=4, ensure_ascii=False)
print(formated_data)