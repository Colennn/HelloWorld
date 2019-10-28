# AirTest自动化测试脚本

[AirTest自动化测试工具文档](http://airtest.netease.com/docs/docs_AirtestIDE-zh_CN/index.html)

最近使用AirTest写了一个自动化测试脚本，用来测试并收集商品促销价格。使用了pytesseract、xl、keyboard模块，模拟手工下单并OCR识别价格记录在excel表格中。

```python
# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

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
            "Windows:///2163954",
    ])


# script content
print("start...")
#图像识别组件，此处要安装Tesseract-OCR软件
pytesseract.pytesseract.tesseract_cmd = 'E://Program Files (x86)/Tesseract-OCR/tesseract.exe'
#会员账号
user = "{VK_NUMPAD1}{VK_NUMPAD5}{VK_NUMPAD6}{VK_NUMPAD2}{VK_NUMPAD2}{VK_NUMPAD1}{VK_NUMPAD6}{VK_NUMPAD1}{VK_NUMPAD5}{VK_NUMPAD5}{VK_NUMPAD5}"

#创建 Workbook & worksheet （excel）
wb = xlwt.Workbook()
ws = wb.add_sheet('test_sheet')

#设置excel表头
ws.write(0, 0, '条码')
ws.write(0, 1, 'POS价格')

#获取excel数据源（商品条码）
data = xlrd.open_workbook('itemNo4.xlsx')
table = data.sheets()[0]
itemNo = table.col_values(0)

i=1
while (i <= len(itemNo)) :
    
    print("+++++ 正在处理第 "+str(i)+" 订单 +++++")
    
    '''
    #录入会员账号
    sleep(1.0)
    print("输入会员账号……")
    keyevent("{F7}")
    keyevent("{ENTER}")
    sleep(1.0)
    keyevent(user)
    keyevent("{ENTER}")
    sleep(1.0)
    '''
    
    #录入商品条码
    print("输入第 "+ str(i) +" 个商品编码，商品条码为 "+ str(itemNo[i-1]))
    #sleep(0.7)
    #从表格中读取商品条码
    ws.write(i, 0, str(itemNo[i-1]))
    text(itemNo[i-1])
    keyevent("{ENTER}")
    
    '''
    #付款流程
    keyevent("{w}")
    sleep(2.0)
    keyevent("{UP}{UP}{UP}")
    '''
    
    #输入价格
    print("识别金额……")
    sleep(1.5)
    #金额截图
    #bbox = (880,250, 1191, 290)
    bbox = (1047,115, 1164, 162)
    img = ImageGrab.grab(bbox)  
    #图像识别
    money = pytesseract.image_to_string(img)
    money = "".join(money.split())
    print("付款金额为："+money)
    ws.write(i, 1, money)
    
    #删除行
    keyevent("{DEL}")
    sleep(1.0)
    
    '''
    print("录入金额……")
    try:
        text(money)
    except :
        print("金额未识别……停止录入商品……")
        break
    
    #确认金额
    keyevent("{ENTER}")
    sleep(1.0)
    keyevent("{y}")
    sleep(5.0)
    '''
    
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

