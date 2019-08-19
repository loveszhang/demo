# Author: Qiaoguo Zhang

import getpass

_username = "zhangqiaoguo"
_password = "123456"

username = input("username:")
#password = getpass.getpass("password:")
password = input("password:")

print(username, password)

#为什么要强制缩进 目的是为了省掉结束符，结构清晰
if _username == username and _password == password:
    print("welcode user {name} login... ".format(name=username))
else:
    print("Invalid username or password")