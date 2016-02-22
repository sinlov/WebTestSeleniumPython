# coding=utf-8

__author__ = 'sinlov'

from selenium.webdriver.remote import webdriver


def string(check):
    if not isinstance(check, str):
        raise TypeError('bad operand type it was not str')


def boolean(check):
    if not isinstance(check, bool):
        raise TypeError('bad operand type it was not boolean')


def web_driver(driver):
    if not isinstance(driver, webdriver.WebDriver):
        raise TypeError('bad operand type, it was not WebDriver')
