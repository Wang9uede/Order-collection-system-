import requests
from bs4 import BeautifulSoup
import time
from actlist import find_actlist
from export import get_exp
from query import get_query
from getxsl import get_xls
from fortest import comb

ghID_T=['PsqYI0A_bsMe6rJ_c2b9c352','Psq54TN_bsMjBqD_f700a128']
ghID_N=['PsHG7Z8_bsSfpBS_13418e71','PsH6wjX_bsS1adv_d48a646e']
#档口分流

Act_name=[]
totalnum_list=[]
totalcash_list=[]
totalname_list=[]
def order_collt(ghID):
    for ghId in ghID:
        #Act_list=[]
        act_list,act_name=find_actlist(ghId)
        #Act_name.append(act_name)
        #每个ghid对应的活动列表及名字
        totalname_list.append(act_name)
        #所有id的活动列表及名字,以一个个数组区分
        numdic_list=[]
        cashdic_list=[]
        #print(act_list)
        for index,actid in enumerate(act_list):
            time.sleep(6)
            taskid=get_exp(ghId,actid)
            #taskid=str(taskid)
            #print(type(taskid))
            #taskid="'"+str(taskid)+"'"
            xls_url=get_query(taskid,ghId)
            num_dic,cash_dic=get_xls(xls_url)
            num_dic['活动']=act_name[index]
            numdic_list.append(num_dic)
            #把每一个活动输出的商品字典存入list
            cash_dic['活动'] = act_name[index]
            cashdic_list.append(cash_dic)
            #把每一个活动输出的金额字典存入list
        totalnum_list.append(numdic_list)
        totalcash_list.append(cashdic_list)


    return  totalname_list,totalnum_list,totalcash_list

totalname_list,totalnum_list,totalcash_list=order_collt(ghID_N)
#print(order_collt(ghID_N))
comb(totalname_list,totalnum_list,totalcash_list)











    #response = requests.get(url)
    #soup = BeautifulSoup(response.text, 'html.parser')
    #orders = soup.find_all('div', class_='order-item')

