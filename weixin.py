import PyOfficeRobot
from PyOfficeRobot.lib.CONST import NEW_LINE
def wx(my_dict):
    # 使用列表推导式将字典中的每个键值对转换为字符串，并将它们添加到列表中
    str_list = [f"{key}: {value}" for key, value in my_dict.items()]
    result_str=''
    # 使用join()方法将列表中的字符串连接起来
    for item in str_list:
        result_str=result_str+item+NEW_LINE
    PyOfficeRobot.chat.send_message(who='文件传输助手', message=result_str)