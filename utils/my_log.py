# coding=utf-8
import os

from utils import time_utils

__author__ = '"sinlov"'

V = " V "
I = " I "
D = " D "
W = " W "
E = " E "

isprint = False

log_path = ''

log_file_full_path = ''


def check_type_str(check):
    if not isinstance(check, str):
        raise TypeError('bad operand type it was str')


def init_log_out(is_out_put=True):
    if not isinstance(is_out_put, bool):
        raise TypeError('bad operand type it was bool')
    global isprint, log_path, log_file_full_path
    isprint = is_out_put
    if isprint:
        log_path = time_utils.log_path()
        log_file_full_path = log_path + time_utils.log_name()


def v(where, message):  # real signature unknown; restored from __doc__
    """
     S.v(where, message) -> string
    """
    check_type_str(where)
    check_type_str(message)
    res = [time_utils.default(), V, "[", where, "] ", message]
    out = "".join(res)
    global isprint
    if isprint:
        out_log(out)
    return out


def i(where, message):
    """
     S.i(where, message) -> string
    """
    check_type_str(where)
    check_type_str(message)
    res = [time_utils.default(), I, "[", where, "] ", message]
    out = "".join(res)
    global isprint
    if isprint:
        out_log(out)
    return out


def d(where, message):
    """
     S.e(where, message) -> string
    """
    check_type_str(where)
    check_type_str(message)
    res = [time_utils.default(), D, "[", where, "] ", message]
    out = "".join(res)
    global isprint
    if isprint:
        out_log(out)
    return out


def w(where, message):
    """
     S.w(where, message) -> string
    """
    check_type_str(where)
    check_type_str(message)
    res = [time_utils.default(), W, "[", where, "] ", message]
    out = "".join(res)
    global isprint
    if isprint:
        out_log(out)
    return out


def e(where, message):
    """
     S.e(where, message) -> string
    """
    check_type_str(where)
    check_type_str(message)
    res = [time_utils.default(), E, "[", where, "] ", message]
    out = "".join(res)
    global isprint
    if isprint:
        out_log(out)
    return out


def out_log(buf=str):
    global isprint, log_path, log_file_full_path
    is_log_path = log_path != ''
    if not is_log_path:
        raise IOError('you must use method init_log_out() before this')
    if isprint:
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        file_obj = open(log_file_full_path, 'a')
        try:
            file_obj.writelines(buf + '\n')
        finally:
            file_obj.close()
    else:
        raise RuntimeError('you must set init_log_out(True) before this')
