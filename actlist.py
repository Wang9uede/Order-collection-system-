#GO哥1  请求活动list

import requests

def find_actlist(ghid):
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
        'ghId': 'PsqYI0A_bsMe6rJ_c2b9c352',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'uid': '73679872',
    }

    json_data = {
        'ghId': ghid,
        'activityStatus': 0,
        'ghViewType': 20,
        'likeName': '',
    }

    response = requests.post(
        'https://apipc.qunjielong.com/activity-accessory/pc/order_activity_list/order_manage',
        headers=headers,
        json=json_data,
    )
    list=response.json()
    act_list=[]
    act_name=[]
    for item in list['data']:
        if item['activityStatus'] == 10:
            act_list.append(item['actId'])
            #活动id
            act_name.append(item['activityName'])
            #活动名(用来判断相同活动)
    #print(list)
    return act_list,act_name




#ghid = PsqYI0A_bsMe6rJ_c2b9c352
#print(find_actlist('PsHG7Z8_bsSfpBS_13418e71'))
#print(len(find_actlist('PsqYI0A_bsMe6rJ_c2b9c352')))

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"ghId":"PsqYI0A_bsMe6rJ_c2b9c352","activityStatus":0,"ghViewType":20,"likeName":""}'
#response = requests.post(
#    'https://apipc.qunjielong.com/activity-accessory/pc/order_activity_list/order_manage',
#    headers=headers,
#    data=data,
#)