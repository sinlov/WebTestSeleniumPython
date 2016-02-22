# coding:utf-8
__author__ = 'sinlov'

import local_properties


def maximize():
    browser = local_properties.init_chrome()
    # let browser max size
    browser.maximize_window()
    return browser

def mobile_iphone_5():
    browser = local_properties.init_chrome()
    browser.set_window_size(320, 568)
    return browser
