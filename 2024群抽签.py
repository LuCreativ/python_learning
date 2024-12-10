import random
import time

from datetime import datetime
import pytz

# 获取UTC时间
utc_time = datetime.now(pytz.utc)

# 转换为北京时间 (UTC+8)
beijing_time = utc_time.astimezone(pytz.timezone('Asia/Shanghai'))

# 转换为柏林时间 (CET/CEST)
berlin_time = utc_time.astimezone(pytz.timezone('Europe/Berlin'))

print(f"北京时间: {beijing_time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"柏林时间: {berlin_time.strftime('%Y-%m-%d %H:%M:%S')}")


sender = ['马肝','刨冰','小邓','婧玥','李','蕾蕾','嫖','了嘴']
receiver = ['马肝','刨冰','小邓','婧玥','李','蕾蕾','嫖','了嘴']

for i in range(len(sender)):     #按顺序送礼
    random.shuffle(receiver)     #随机收礼人
    y = receiver[0]              #收礼人抽一个

    while y == sender[i]:         #收礼人=送礼人
        random.shuffle(receiver)  #再次随机
        y = receiver[0]           #抽一个收礼人
    receiver.remove(y)            #收礼人列表中删除 已收    
 
    print(f'{sender[i]} -> {y}')
    time.sleep(3)