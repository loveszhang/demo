# Author: Qiaoguo Zhang

'''
for i in range(10):
    print("loop ", i)

for i in range(0,10,3):
    print("loop ", i)
'''

'''
for i in range(0, 10):
    if i < 3:
        print("i:", i)
    else:
        continue
    print("hehe")
'''

for i in range(10):
    print('------------', i)
    for j in range(10):
        print(j)
        if j>5:
            break