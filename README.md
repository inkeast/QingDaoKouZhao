# 青岛政务网口罩售卖辅助购买软件
## 简介
    本软件可以设定购买时间，在开始购买时自动选择购买门店，自动输入相关信息，用户只需输入验证码即可完成口罩购买。
## 测试环境&&环境需求
    Chorme V80.0.3987.100 X64  
    Python 3.7 X64
## Python包
    selenium
## 运行
    修改kouzhao.py中的
    ```
    开抢时间 = "2020-02-13 08:30:00"  
    姓名 = ""  
    电话 = ""  
    身份证号 = ""  
    ```
    修改
    ```
    driver.find_element_by_css_selector("*[data-name='国风大药房国风药店'] > .layui-col-xs2.action.text-right").click()
    ```
    中的药店名(务必准确！！)
    在命令台中运行：
    ```
    python kouzhao.py
    ```