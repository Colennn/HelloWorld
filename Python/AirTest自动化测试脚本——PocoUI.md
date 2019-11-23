# AirTest自动化测试——PocoUI

新写的一个测试安卓的自动化脚本，用了PocoUI

```python
# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# 导入 random(随机数) 模块
import random
#键盘监听
import keyboard
#图像识别，截图
import pytesseract
from PIL import Image, ImageGrab
#导入excel模块
import xlwt
import xlrd
#引入time模块
import time

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/79UNW18B13001874",
    ])
    
poco = AndroidUiautomationPoco()

# script content
print("start...")

#创建 Workbook & worksheet （excel）
wb = xlwt.Workbook()
ws = wb.add_sheet('test_sheet')
#设置excel表头
ws.write(0, 0, '商品编号')
ws.write(0, 1, '重量')
ws.write(0, 2, 'SFA价格')
#获取excel数据源（商品条码）
data = xlrd.open_workbook('itemNo5.xlsx')
table = data.sheets()[0]
itemNo = table.col_values(0)
itemWeight = table.col_values(1)

#1.进入访销管理、点击客户、开始拜访、销售订单
#touch(Template(r"tpl1572325437398.png", record_pos=(0.0, -0.586), resolution=(1080, 2340)))
#poco = AndroidUiautomationPoco()
#poco("com.efuture.sfa:id/svd_btnStart").click()
#touch(Template(r"tpl1572325623633.png", record_pos=(-0.251, -0.421), resolution=(1080, 2340)))

i=1
while (i <= len(itemNo)) :
#while (i <= 1) :
    print("+++++ 正在处理第 "+str(i)+" 订单 +++++")
    
    #录入商品编码、重量
    print("输入第 "+ str(i) +" 个商品，商品编号为 "+ str(itemNo[i-1]))
    
    #在表格中写入商品编码、重量
    ws.write(i, 0, str(int(itemNo[i-1])))
    ws.write(i, 1, str(itemWeight[i-1]))
    

    #2.点击搜索输入框输入商品编码、重量
    poco("com.efuture.sfa:id/keySearchEditText").long_click()

    text(str(int(itemNo[i-1])))
    keyevent("KEYCODE_DEL")
    poco("com.efuture.sfa:id/mxSearchBtn").click()
    poco("android.widget.TextView").click()
    poco("com.efuture.sfa:id/numEditText").click()
    text(str(itemWeight[i-1]))
    poco("com.efuture.sfa:id/confirmTextView").click()
    poco(text="金额确认").click()
    print('—————商品应收金额—————')
    money = poco("com.efuture.sfa:id/arAmountTextView").get_text()
    print(money)
    ws.write(i, 2, money)
    #3.从订单中删除商品
    poco("com.efuture.sfa:id/deleteButton").click()
    
    #保存文件，防止脚本中途停止
    if(i%5==0):
        excelSrc = "./testData/item - "+str(time.time())+" - "+str(i)+".xls"
        wb.save(excelSrc)
        print("数据已保存，文件名为 "+excelSrc)

    i += 1    
    #一轮循环结束

#保存文件
excelSrc = "./testData/item - "+str(time.time())+" - "+str(i)+".xls"
wb.save(excelSrc)
print("数据已保存，文件名为 "+excelSrc)
print("程序退出……")
```



