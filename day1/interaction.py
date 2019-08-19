# Author: Qiaoguo Zhang

#用户输入
#username = input("username:")
#password = input("password:")
#print(username, password)

#打印如下格式
'''
------------ info of $ ------------
Name:
Age:
Job:
Salary:
'''
name = input("name:")
age = int(input("age:")) #转换int类型
print(type(age)) #打印变量类型
job = input("job:")
salary = input("salary:")

#格式化输出 这种拼接开辟了好几块空间
info = '''
------------ info of ''' + name + ''' ------------
Name:'''+ name + '''
Age:'''+ str(age) + '''
Job:'''+ job + '''
Salary:'''+ salary + ''''''
print(info)

# %s 字符串 %d 数字 $f小数点
msg = '''
------------ info of %s ------------
Name:%s
Age:%d
Job:%s
Salary:%s ''' % (name, name, age, job, salary)
print(msg)

#这种拼接开辟一块空间
msg2 = '''
------------ info of {_name} ------------
Name: {_name}
Age: {_age}
Job: {_job}
Salary: {_salary} 
'''.format(_name=name,
           _age=str(age),
           _job=job,
           _salary=salary)
print(msg2)

#这种拼接开辟一块空间
msg3 = '''
------------ info of {0} ------------
Name: {0}
Age: {1}
Job: {2}
Salary: {3} 
'''.format(name, str(age), job, salary)
print(msg3)