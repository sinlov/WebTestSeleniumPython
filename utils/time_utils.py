# coding:utf-8
__author__ = 'sinlov'

import os
import time
import datetime


def default():
    return time.strftime("%Y-%m-%d %H:%M:%S")


def microsecond():
    return int(datetime.datetime.now().microsecond)


def str_format():
    res = [str(time.strftime("%Y-%m-%d %H:%M:%S")), " .", str(microsecond())]
    return ''.join(res)


def file_format():
    res = [str(time.strftime("%Y_%m_%d %H_%M_%S")), '.', str(microsecond())]
    return ''.join(res)


def log_path():
    global middle_path
    os_type = os.name
    middle_path = '/build/out_log/'
    if os_type == 'nt':
        middle_path = '\\build\\out_log\\'
    res = [os.getcwd(), middle_path]
    return ''.join(res)


def log_name():
    res = [file_format(), '.log']
    return ''.join(res)
