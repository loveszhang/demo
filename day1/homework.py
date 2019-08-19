# Author: Qiaoguo Zhang

import ast

username = input("username: ")
password = input("password: ")

#student = {"username":"zhangqiaoguo", "age":30}
#print(type(student), student)

isErrorInputBigThree = False #isErrorInputBigThree 标识当前用户登陆是否出错超过三次
isHavingErrorUser = False #isHavingUser 是否存在登陆出错超过三次的用户
with open("error.txt","r",encoding="utf-8") as readErrorF:
    errorLines = readErrorF.readlines()
    for line in errorLines:
        errorLine = ast.literal_eval(line)
        if username == errorLine.get("username") and errorLine.get("count")>=3:
            print("您的账号，密码输入出错多次已被锁定")
            isErrorInputBigThree = True
            isHavingErrorUser = True
            break
#print("isErrorInputBigThree: ", isErrorInputBigThree, "  isErrorInputBigThree: ", isErrorInputBigThree)

#student1 = '{"username":"zhangqiaoguo", "age":30}'
#print(type(student1), student1)

#student2 = ast.literal_eval(student1)
#print(type(student2), student2)

if isErrorInputBigThree == 0 and isHavingErrorUser == 0:
    isLoginOk = False # isLoginOk 表示是否登陆成功
    with open("customer.txt","r") as f:
        lines = f.readlines()
        print(type(lines), lines)
        for line in lines:
            line1 = ast.literal_eval(line)
            #print(type(line1), line1)
            if username == line1.get("username") and password == line1.get("password"):
                isLoginOk = True
                break

    if isLoginOk == 0:
        print("用户名密码错误")
        isAdd = True #isAdd 表示是否要写入登陆出错用户

        with open("error.txt", "r") as readErrorF:
            errorLines = readErrorF.readlines()

            with open("error.txt", "w") as wiretErrorf:
                for linee in errorLines:
                    errorLine = ast.literal_eval(linee)
                    if username == errorLine.get("username"):
                        count = errorLine.get("count") + 1
                        errorLine['count'] = count
                        isAdd = False
                        wiretErrorf.write(str(errorLine) + " \n")
                    else:
                        if len(linee) != 0:
                            wiretErrorf.write(linee)
                #print("isAdd ", isAdd)
                if isAdd:
                    errorContent = {"username":username, "count":1}
                    wiretErrorf.write(str(errorContent) + " \n")

    else:
        print("欢迎用户：{_username} 登陆！！！".format(_username=username))
        with open("error.txt", "r") as readErrorF:
            errorLines = readErrorF.readlines()
            print(len(errorLines), errorLines)

            with open("error.txt", "w") as wiretErrorf:
                for linee in errorLines:
                    errorLine = ast.literal_eval(linee)
                    if username == errorLine.get("username"):
                        continue
                    wiretErrorf.write(linee)