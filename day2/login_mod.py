# Author: Qiaoguo Zhang

import getpass

_username = 'zhangqiaoguo'
_password = '123'

user = input("请输入用户名：")
pwd = input("请输入密码:")

if user == _username and pwd == _password:
    print("welcome user %s login"% _username)
else:
    print("wrong username or password")

print(user,pwd)