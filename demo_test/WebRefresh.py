# coding=utf-8

__author__ = 'sinlov'

from utils import chrome_webdriver
from utils import my_log

my_log.init_log_out(True)

test_time = 100
wait_beat = 3000

web_driver = chrome_webdriver.maximize()

web_driver.get('http://test.g.kuaifazs.com/web/cr/Web.php')

for i in range(0, test_time):
    web_driver.implicitly_wait(wait_beat)
    if i > test_time:
        break
    else:
        web_driver.refresh()
        image = web_driver.find_element_by_xpath('//*[@id="v_img"]')
        src = image.get_attribute('src')
        if len(str(src)) < 21:
            my_log.w('WebRefresh check', 'image show error ' + src)
        else:
            my_log.i('WebRefresh check', 'image show success ' + src)

web_driver.close()
