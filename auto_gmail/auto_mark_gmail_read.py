# coding=utf-8

__author__ = '"sinlov"'

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import conf
import time
from utils import chrome_webdriver
from utils import time_utils
from utils import my_log
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

my_log.init_log_out(True)

browser = chrome_webdriver.maximize()
# load page
browser.get(conf.url_gmail)
# Let the page load, will be added to the API
time.sleep(conf.sleep_time_waiting_lang)


def do_refresh_inbox():
    btn_inbox = browser.find_element_by_xpath('//*[@id=":iq"]/div/div[1]/span/a')
    btn_inbox.click()
    time.sleep(conf.sleep_time_loading)
    btn_refresh = browser.find_element_by_xpath('//*[@id=":5"]/div[2]/div[1]/div[1]/div/div/div[4]/div')
    btn_refresh.click()
    time.sleep(conf.sleep_time_waiting)
    btn_more_more_actions = browser.find_element_by_xpath('//*[@id=":30"]')
    btn_more_more_actions.click()
    time.sleep(conf.sleep_time_middle)
    # my_log.i('do_input_login_info()', 'click login ok')


try:
    do_refresh_inbox()
    time.sleep(conf.sleep_time_middle)
except NoSuchElementException:
    assert 1, "can't read gmail info"

# quit test
time.sleep(conf.sleep_time_large)
# browser.quit()
