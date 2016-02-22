WebTestSelenium
=====================

# For what

this is simple python test web use selenium framework

## before using

### words marking

|word|where|use|detail|
|---|---|---|---|
|test|prefix|Mark this is test|use in file name or method|
|pd|prefix|Mark this is preconditions|use in file name or method most use public|
|pub|prefix|Mark this is public|use in file name or method most use public|
|bt|prefix|Mark this is backtracking|use in file name or method most use public|
|utils|suffix|Mark this is tools|use in file name or method|
|conf|suffix|Config and setting|use in file name or method|
|NG|log|Use cases totally can not pass|use in log, mark `NG`|
|NT|log|Use cases never even been run|use in log, Maybe the preconditions are not run, or bt have a Bug, Mark `NT`|
|ND|log|Use cases failed to identify Bug|use in log, usually mark `Ok` instead of `Pass`|
|Block|log|Use cases can not continue what executed a part of the bug|use in log, usually mark `Block`|
|OK|log|Use cases are ok and have some bug|use in log, usually mark `Ok`|
|Pass|log|Use cases without any bug|use in log, usually mark `Pass`. Of course, this generally does not appear|
|rc|log|Mark this is runtime tracking|use in log|
|anr|log|Mark this is application not responding|use in log|

### Code structure

code name **Except utils**

must be use **Three-tier structure**

```bash
project name-------------------Module name      `prefix test`
    Module name----------------package name     `prefix test`
        Super use case---------code file name   `CamelCasing`
            Sub use case-------code method      `prefix test`

utils
    in Module name utils
utils file
    ordinary            `purpose_utils`
    system utils plus   `base_log` or `my_os`
```

# How to use

## install ChromeDriver

you must install driver just like  [ChromeDriver driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)


## create file

This is for team setting

**You must create** python file `local_properties.py` for conf web driver path

Contents

```python
# coding:utf-8
__author__ = '"sinlov"'

from selenium import webdriver

path_chrome_driver_win = "C:\Users\sin-base\AppData\Local\Google\Chrome\Application\chromedriver.exe"
path_chrome_driver_osx = "/usr/bin/chromedriver"


def init_chrome():
    return webdriver.Chrome(path_chrome_driver_osx)

def init_android_driver():
    return webdriver.Android()

def init_safari():
    return webdriver.Safari()

```

### if use windows

You **must assign** your `path_chrome_driver_win` to your runtime path and install **OS X chrome driver**

```python
path_chrome_driver_win = "your chrome driver path"
def init_chrome():
    return webdriver.Chrome(path_chrome_driver_win)
```

When you **use other driver**  you can create like this

```python
local_properties.init_android_driver()
```

### if use OS X

install **OS X chrome driver** and change **init_web_driver** like this

```python
def init_chrome():
    return webdriver.Chrome(path_chrome_driver_osx)
```


### config suggest

for team work init web driver just in `local_properties`

### Use Log out with utils `my_log`

* Auto put log at path {\[code path\]/build/out_log/}

```python
from utils import my_log

my_log.init_log_out(True)
my_log.i('test_one', 'message')
my_log.v('test_one', 'message')
my_log.d('test_one', 'message')
my_log.w('test_one', 'message')
my_log.e('test_one', 'message')
```


* You can debug like this do not write log

```python
from utils import my_log

print my_log.i('test_one', 'message')
print my_log.v('test_one', 'message')
print my_log.d('test_one', 'message')
print my_log.w('test_one', 'message')
print my_log.e('test_one', 'message')
```

### Use Type check `type_check`

```python
from utils import type_check

```

you can use `type_check.boolean()` `type_check.string` ... to type check or update check by yourself

## When Error

if Code error when import package, you can install selenium and dependencies

> Mostly try to open this is page [pypi](https://pypi.python.org/simple/).
> It can not be install python package which page is not open.


License
--------

    Apache License
	Version 2.0, January 2004
	http://www.apache.org/licenses/

	TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
