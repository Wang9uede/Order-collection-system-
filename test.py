a=[]
b=[1,2]
for i in range(3):
    a.append(b)
print(a)



list1 = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
list2 = [{'a': 10, 'c': 20}, {'b': 30, 'd': 40}]
list3 = [{'e': 50, 'f': 60}, {'g': 70, 'h': 80}]

# 定义一个空字典用于存储结果
result_dict = {}

# 遍历每个列表
for my_list in [list1, list2, list3]:
    # 对于列表中的每个字典，遍历它的每个键值对
    for my_dict in my_list:
        for key, value in my_dict.items():
            # 如果当前键已经在 result_dict 中存在，将它的值加上当前字典对应键的值
            if key in result_dict:
                result_dict[key] += value
            # 否则，在 result_dict 中添加一个新键值对
            else:
                result_dict[key] = value

# 将 result_dict 中的键值对转换为字典，并添加到一个新的列表 result_list 中
result_list = [{key: value} for key, value in result_dict.items()]

print(result_list)  # 输出 [{'a': 11, 'b': 32, 'c': 23, 'd': 44, 'e': 50, 'f': 60, 'g': 70, 'h': 80}]





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
    'ghId': 'PsH6wjX_bsS1adv_d48a646e',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'uid': '73679872',
}

params = {
    'taskId': '5036823',
}
response = requests.get('https://apipc.qunjielong.com/order-export/api/pc/query_export_result', params=params, headers=headers)



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
    'ghId': 'PsH6wjX_bsS1adv_d48a646e',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'uid': '73679872',
}

params = {
    'taskId': '5036823',
}
response = requests.get('https://apipc.qunjielong.com/order-export/api/pc/query_export_result', params=params, headers=headers)








result_name = []
    result_dic = {}
    for my_list,index1 in enumerate(totalname_list):
        # 对于列表中的每个list，遍历它的每个键值对
        for item,index2 in enumerate(my_list):
                # 如果当前键已经在 result_dict 中存在，将它的值加上当前字典对应键的值
            if item in result_name:
                for key,value in totalnum_list:
                    if key in result_dic:
                        result_dict[key] += value

                    else:
                        result_dict[key] = value





                result_dict[key] += value
                # 否则，在 result_dict 中添加一个新键值对
            else:
                result_dict[key] = value

    # 将 result_dict 中的键值对转换为字典，并添加到一个新的列表 result_list 中
    result_list = [{key: value} for key, value in result_dict.items()]

    print(result_list)  # 输出 [{'a': 11, 'b': 32, 'c': 23, 'd': 44, 'e': 50, 'f': 60, 'g': 70, 'h': 80}]







