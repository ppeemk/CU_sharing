import os
import io
from setuptools import setup, find_packages

# print(os.path.abspath(__file__))
# print(os.path.join(os.path.abspath(__file__), 'README.TXT'))
here = os.path.abspath(os.path.abspath(__file__))
# print(here)

dic = {'ข้อ1': 'คำตอบ1', 'ข้อ2': 'คำตอบ2'}


# print(dic.keys())

# README = io.open(os.path.join(here,'README.MD'), encoding="utf8").read()
# print(README)


def read_file(file,split = False):
    info = []

    with open(file, encoding='utf8') as f:
        for line in f:
            if split != True:
                s = line.strip()
                info.append(s)
            else:
                s = line.split('/')
                for i, e in enumerate(s):
                    s[i] = e.strip()
                info.append(s)

    # print(info)
    return info


def play():
    return input('>>> ')


def wait():
    input('... ')


def system():
    print('ยินดีต้อนรับเข้าสู่ระบบการเรียนรู้ภาษาไพธอนภาษาไทย\n')
    user_name = input(
        'ให้ผมเรียกคุณว่าอย่างไรดีครับ :')  # ต้องนำไปเขียนฟังก์ชั่นรับชื่อ แบบกรองอักษรพิเศษ และเว้นวรรค
    menu = read_file('C:/Users/Acer/Documents/GitHub/CU_sharing/teach_file/สารบัญ.txt')
    for i, e in enumerate(menu):
        print('{} {}'.format(i + 1, e))
    # menu_c = int(input('โปรดเลือกหัวข้อที่ท่านต้องการจะเรียน :')) - 1
    info = read_file('C:/Users/Acer/Documents/GitHub/CU_sharing/teach_file/ชนิดของตัวแปร.txt') # return list
    ia = 0
    answer = read_file('C:/Users/Acer/Documents/GitHub/CU_sharing/teach_file/ชนิดของตัวแปร[a].txt')
    # print(answer[ia])
    # print(info)
    for i, e in enumerate(info):
        if '%n%' in e:  # name
            info[i] = e.replace('%n%', user_name)

    for i in info:
        if '%w%' in i:  # wait
            i = i.replace('%w%', '')
            print(i)
            wait()
        elif '%p%' in i:  # play
            i = i.replace('%p%', '')
            print(i)
            x = play()
        elif '%uo%' in i:  # user output
            i = i.replace('%uo%', x)
            print(i)
        elif '%ca%' in i:  # compare answer
            # if x == str(answer[ia]):
            #     print(eval(answer[ia]))
            #     ia += 1
            # else:
            #     print('Error')
            while x != answer[ia]:
                print('โปรดพิมพ์', answer[ia])
                x = play()
            else:
                # exec('print 1\n print2')
                print(eval(answer[ia]))
                print('นั่นแหละครับ คำตอบที่เราต้องการ')
                ia += 1
                wait()
        else:
            print(i)


z = read_file(os.path.join(os.getcwd(),'teach_file','การเช็คเงื่อนไข[a].txt'),split=True)
# print(z)
# print(z[1])
# print(z[1][0])
# print(z[1][1])
# exec(z[1][1])
# for i,e in enumerate(z):
    # print(i,e)
    # for index,info in enumerate(e):
        # print(index,info)
        # print(ex)
        # if '%nl%' in info:
        #     e[index] = e[index].replace('%nl%','\n')
            # print(ex)

# print(z)
# exec(z[1][0])

# print(type(x[0][0]))
# print(eval(str(x[0])))
# print(x[0][1])
# print(exec(x[0][0]))
# print(eval(x[0][0]))
# print(eval('type(20)'))
# print(exec('a=20'))
#
# print(a)

# system()
# answer = ["type('name')",2]
# print(eval(answer[0]))
# x = play()
# print(type(x))
# print(print('hello world'))
# try:
#     eval('print('+'print("ฉัน","รัก","ไพธอน",sep= "<3")'+')')
# except None:
#     pass
# x = ['type("x")', 2]
# print(eval(x[0]))
# exec('a = input("a:")')
# print(eval('"a คือ",a'))
# eval("print('hello world')")
# eval('type(20)')
# print(type(20))
# b = 'type(2)'
# eval('print('+b+')')
# s ="print('a คือ',a)/ a = input('โปรดใส่ค่า a:')"
# a = s.split('/')
# for i,e in enumerate(a):
#     a[i] = e.strip()
#
# print(a)
a =  range(5)
print(a)