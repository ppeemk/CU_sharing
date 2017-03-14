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


def read_file(file):
    info = []

    with open(file, encoding='utf8') as f:
        for line in f:
            s = line.strip()
            # print(s)
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
    menu = read_file('สารบัญ.txt')
    for i, e in enumerate(menu):
        print('{} {}'.format(i + 1, e))
    menu_c = int(input('โปรดเลือกหัวข้อที่ท่านต้องการจะเรียน :')) - 1
    info = read_file(menu[menu_c] + '.txt')  # return list
    ia = 0
    answer = read_file(menu[menu_c] + '[a].txt')
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


system()
# answer = ["type('name')",2]
# print(eval(answer[0]))
# x = play()
# print(type(x))

# x = ['type("x")', 2]
# print(eval(x[0]))
