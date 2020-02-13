import os
from selenium import webdriver
import datetime
import time
from selenium.webdriver.chrome.options import Options

# 创建浏览器对象
chrome_options = Options()
# 关闭使用 ChromeDriver 打开浏览器时上部提示语 "Chrome正在受到自动软件的控制"
chrome_options.add_argument("disable-infobars")
# 允许浏览器重定向，Framebusting requires same-origin or a user gesture
chrome_options.add_argument("disable-web-security")
driver = webdriver.Chrome(os.path.join("./src", "chromedriver.exe"),
                          chrome_options=chrome_options)
# 窗口最大化显示
driver.maximize_window()

url = "http://kzyynew.qingdao.gov.cn:81/authPage/page"
开抢时间 = "2020-02-13 08:30:00"
姓名 = ""
电话 = ""
身份证号 = ""


while 1:
    try:
        if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') > 开抢时间:
            driver.get(url)
            time.sleep(0.5)
            if driver.find_element_by_css_selector('.layui-icon.layui-icon-ok'):
                driver.find_element_by_css_selector('.layui-form.text-center').click()
                driver.find_element_by_css_selector("*[data-name='国风大药房国风药店'] > .layui-col-xs2.action.text-right").click()
                time.sleep(0.5)
                driver.find_element_by_name("name").send_keys(姓名)
                driver.find_element_by_name("mobile").send_keys(电话)
                driver.find_element_by_name("code").send_keys(身份证号)
                break
    except Exception:
        time.sleep(0.5)

