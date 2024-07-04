import requests
import os
from query import get_query
import xlrd

def get_xls(xls):


    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://pro.qunjielong.com/',
        'Sec-Fetch-Dest': 'iframe',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    url='https://res0.shangshi360.com/{}'.format(xls)

    response = requests.get(
        url,
        headers=headers,
    )
    content = response.content

    save_path='D:/xls/'
    file_name = 'act_order.xls'
    xls_path=os.path.join(save_path, file_name)

    with open(xls_path, 'wb') as f:
        f.write(content)

    num_dic,cash_dic=get_goods_xls(xls_path)
    os.remove(xls_path)
    return num_dic,cash_dic





def get_goods_xls(url):
    # 打开xls文件并获取第二个工作表
    workbook = xlrd.open_workbook(url)
    sheet = workbook.sheet_by_index(1)  # 第二个工作表的索引为1
    num_dic={}
    cash_dic={}
    cash_pos=0


    for row in range(sheet.nrows):
        cell_value = sheet.cell_value(row, 0)
        if cell_value == '请勾选地址':
            cash_pos+=sheet.cell_value(row,4)

        elif cell_value!='商品名称'and cell_value!='接龙个数'and type(cell_value) is str and cell_value!='':
            num_dic[cell_value] = sheet.cell_value(row,3)
            #商品数量字典
            cash_dic[cell_value] = sheet.cell_value(row,4)
            #商品金额字典
        cash_dic['配送费'] = cash_pos
    return num_dic,cash_dic



def get_pos_xls(url,target):
    # 打开xls文件并获取第二个工作表
    workbook = xlrd.open_workbook('example.xls')
    sheet = workbook.sheet_by_index(1)  # 第二个工作表的索引为1

    # 查找目标值
    target_value = target
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            cell_value = sheet.cell_value(row, col)
            if cell_value == target_value:
                return sheet.cell_value(row+1,col)
                #print('目标值位于第%d行第%d列' % (row+1, col+1))



#xls=get_query('5036755')
#print(get_xls('up/async_excel/dingdan20230411_2235_ea1f7ddfa6fc4cbf9f0cba2a15f91f0e.xls'))