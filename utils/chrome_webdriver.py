# coding:utf-8
__author__ = '"sinlov"'

import local_properties


def maximize():
    browser = local_properties.init_web_driver()
    # let browser max size
    browser.maximize_window()
    return browser
