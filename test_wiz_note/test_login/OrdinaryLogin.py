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
browser.get(conf.url_wiz_login)
# Let the page load, will be added to the API
time.sleep(conf.sleep_time_loading)


def test_go_to_login_page():
    try:
        # find element
        login_button = browser.find_element_by_xpath('//*[@id="navbar-link"]/ul/li[8]/a')
        login_button.click()
        print my_log.i(time_utils.default(), 'click login button ok')
    except NoSuchElementException:
        assert 0, "can't find login button"


# test_go_to_login_page()


def test_error_login_info():
    try:
        assert login_error_info.text in "帐号或密码有误，重新输入。"
        print my_log.i(time_utils.default(), "ordinary login test success!")
    except AssertionError:
        print my_log.e('test_error_login_info()', "login error info error, it was not show in 帐号或密码有误，重新输入。")


def do_input_login_info():
    username = browser.find_element_by_xpath('//*[@id="login-wizID"]')
    username.send_keys("sinlov" + Keys.RETURN)
    my_log.i('do_input_login_info()', 'Input username ok')
    password = browser.find_element_by_xpath('//*[@id="login-password"]')
    password.send_keys("sinlov" + Keys.RETURN)
    my_log.i('do_input_login_info()', 'Input password ok')
    btn_login = browser.find_element_by_xpath('//*[@id="loginbtn"]')
    btn_login.click()
    my_log.i('do_input_login_info()', 'click login ok')


try:
    do_input_login_info()
    time.sleep(conf.sleep_time_middle)
    login_error_info = browser.find_element_by_xpath("//*[@id='loginarea']/div/div[1]/div/span[5]")
    test_error_login_info()
except NoSuchElementException:
    assert 1, "can't find username or password for input"

# quit test
time.sleep(conf.sleep_time_large)
browser.quit()
