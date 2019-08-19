# Author: Qiaoguo Zhang

with open("codingWord.txt","r",encoding="utf-8") as readErrorF:
    errorLines = readErrorF.readlines()

    with open('codingWord.txt','w') as f:
        for line in errorLines:
            f.write(line)

        for i in range(1,10):
            student = {"username":"zhangqiaoguo", "age":30}
            f.write(str(student) + "\n")

        print(type(student))
        f.write(str(student) + "\n")
