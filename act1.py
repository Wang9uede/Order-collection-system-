import requests

def find_act(actid,ghid):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJ1aWQiOjczNjc5ODcyLCJleHAiOjE2ODMyMTE3MDh9.5pTh5ABVeVqmVGu8pZEsrhuCBk0Z33priU2SxFE3BIUi2BxwIiHxX7-rGupqQQMog7JsbaH_vkLuWH67vWCG6A',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
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

    json_data = {
        'actId': actid,
        'ghId': ghid,
        'ghViewType': 20,
        #'beginDate': 1664894917662,
        #'endDate': 1680619717662,
        'merchantGhCodeList': [
            '0',
        ],
        'status': 0,
        'refundStatus': 0,
        'isAllActExport': False,
        'forward': False,
        'dlvAddrId': 0,
        'orderNoList': [],
        'logisticsNoList': [],
        'orderTags': [],
        'logisticsPushStatus': [],
        'pageParam': {
            'page': 1,
            'pageSize': 100,
        },
    }

    response = requests.post('https://apipc.qunjielong.com/order/customer/manage/find_orders', headers=headers, json=json_data)
    print(response.json())
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"actId":2303311005259035,"ghId":"PsHG7Z8_bsSfpBS_13418e71","ghViewType":20,"beginDate":1664894917662,"endDate":1680619717662,"merchantGhCodeList":["0"],"status":0,"refundStatus":0,"isAllActExport":false,"forward":false,"dlvAddrId":0,"orderNoList":[],"logisticsNoList":[],"orderTags":[],"logisticsPushStatus":[],"pageParam":{"page":1,"pageSize":100}}'
#response = requests.post('https://apipc.qunjielong.com/order/customer/manage/find_orders', headers=headers, data=data)