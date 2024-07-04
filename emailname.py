import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJ1aWQiOjczNjc5ODcyLCJleHAiOjE2ODMyMTE3MDh9.5pTh5ABVeVqmVGu8pZEsrhuCBk0Z33priU2SxFE3BIUi2BxwIiHxX7-rGupqQQMog7JsbaH_vkLuWH67vWCG6A',
    'Connection': 'keep-alive',
    'Origin': 'https://pro.qunjielong.com',
    'Referer': 'https://pro.qunjielong.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'feature-tag': '',
    'ghId': 'PsHG7Z8_bsSfpBS_13418e71',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'uid': '73679872',
}

response = requests.get('https://apipc.qunjielong.com/order-export/api/pc/get_output_mail_name', headers=headers)
print(response.text)