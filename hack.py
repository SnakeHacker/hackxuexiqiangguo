from selenium import webdriver
import time
from random import randint
import socket
socket.setdefaulttimeout(30)

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


HACK_URL = "https://www.xuexi.cn/"
LOGIN_URL = 'https://pc.xuexi.cn/points/login.html'
PAGE_NUMS = 10
VIDEO_NUMS = 5


def start_hack():
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "none"
    chrome_options = Options()
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(20)

    # 扫码登录
    browser.get(LOGIN_URL)
    time.sleep(15)

    browser.get(HACK_URL)
    time.sleep(5)

    handle = browser.current_window_handle

    # 文本新闻
    important_news = browser.find_elements_by_class_name("_3wnLIRcEni99IWb4rSpguK")
    for news in important_news:
        global PAGE_NUMS
        if PAGE_NUMS == 0:
            break
        PAGE_NUMS -= 1

        print(news.text)
        news.click()
        time.sleep(randint(2, 7))
        scrollCount = 0
        # 随机滑动页面
        while scrollCount < 10:
            handles = browser.window_handles
            for newhandle in handles:
                if newhandle != handle:
                    browser.switch_to.window(newhandle)
            jsCode = "var q=document.documentElement.scrollTop={}".format(randint(100, 700))
            browser.execute_script(jsCode)
            time.sleep(randint(3, 20))
            scrollCount += 1
        handles = browser.window_handles
        for newhandle in handles:
            if newhandle != handle:
                browser.switch_to.window(newhandle)
                browser.close()
        browser.switch_to.window(handle)

    # 视频新闻
    dypd = browser.find_element_by_xpath("//div[text()='第一频道']")
    time.sleep(5)
    dypd.click()
    time.sleep(3)

    browser.close()
    handles = browser.window_handles
    handle = handles[0]
    browser.switch_to.window(handle)
    
    video_news = browser.find_elements_by_class_name("textWrapper")
    for news in video_news:
        global VIDEO_NUMS
        if VIDEO_NUMS == 0:
            break
        VIDEO_NUMS -= 1

        print(news.text)
        news.click()

        time.sleep(randint(2, 7))
        scrollCount = 0
        # 随机滑动页面
        while scrollCount < 10:
            handles = browser.window_handles
            for newhandle in handles:
                if newhandle != handle:
                    browser.switch_to.window(newhandle)
            jsCode = "var q=document.documentElement.scrollTop={}".format(randint(100, 300))
            browser.execute_script(jsCode)
            time.sleep(randint(3, 20))
            scrollCount += 1
        handles = browser.window_handles
        for newhandle in handles:
            if newhandle != handle:
                browser.switch_to.window(newhandle)
                browser.close()
        browser.switch_to_window(handle)

    time.sleep(5)
    print("今日份已刷完")

if __name__ == '__main__':
    start_hack()