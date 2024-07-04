import requests
import time
from tenacity import retry

@retry(stop_max_attempt_number=1, stop_max_delay=2000, wait_fixed=500)
def get_query(taskId,ghId):
    headers = {
        'Accept': 'application+/json, text/plain, */*',
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
        'ghId': ghId,
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'uid': '73679872',
    }

    params = {
        'taskId': taskId,
    }
    response1 = requests.get('https://apipc.qunjielong.com/order-export/api/pc/query_export_result', params=params,
                            headers=headers)
    time.sleep(1)

    response = requests.get('https://apipc.qunjielong.com/order-export/api/pc/query_export_result', params=params, headers=headers)

    list=response.json()
    out=list['data']['filePathList'][0]

    return out

#taskid=5036877
#taskid="'"+str(taskid)+"'"
#print(type(taskid))
#print(get_query(str(taskid),'PsH6wjX_bsS1adv_d48a646e'))