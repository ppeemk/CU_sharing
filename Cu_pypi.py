# github proj
import os


class Cu_pypi():
    def __init__(self):
        # self.read_file('saraban.txt')
        self.start()

    def wait(self):
        return input('...')

    def play(self):
        return input('>>> ')

    def read_file(self, filename, split=False):
        info = []
        with open(filename, encoding='utf8')as f:
            for line in f:
                if split != True:
                    s = line.strip()
                    info.append(s)
                else:
                    s = line.split('/')
                    for i, e in enumerate(s):
                        s[i] = e.strip()
                    info.append(s)
        return info

    def install_package(self, package_name):  # เขียนฟังก์ชั่นดาว์นโหลดข้อมูล textfile สอน
        pass

    def take_user_name(self):  # เขียนโค้ดเพิ่มเติมดักตัวอักษรพิเศษ
        return input('โปรดระบุชื่อของคุณ : ')

    def start(self):
        # เมื่อเริ่มจะสั่งโปรแกรมให้ทำการหาไฟล์ในการสอน ถ้ามีจะเริ่มทำงานต่อถ้าไม่มีจะเข้า except บอกต้องดาว์นโหลดและวิธีการใช้งานโปรแกรมเบื้องต้น
        try:
            saraban = self.read_file(
                os.path.join(os.path.abspath(os.getcwd()), 'teach_file', 'สารบัญ.txt'))
        except:
            # self.install_package()
            pass
        user_name = self.take_user_name()
        # ทำฟังก์ชั่นวน loop ให้ถามไฟล์ที่ต้องการเรียนหลังจากเรียนจบ
        print('โปรดเลือกหัวข้อที่ต้องการเรียน\n')
        for i, e in enumerate(saraban):
            print('{} {}'.format(i + 1, e))
        saraban_c = int(input('โปรดเลือก : ')) - 1
        teach_file = self.read_file(
            os.path.join(os.path.abspath(os.getcwd()), 'teach_file',
                         (saraban[saraban_c] + '.txt')))
        try:
            answer_file = self.read_file(
                os.path.join(os.path.abspath(os.getcwd()), 'teach_file',
                             (saraban[saraban_c] + '[a].txt')), split=True)
        except:
            pass
        ia = 0

        # ทำการเปลี่ยนอักขระพิเศษให้เป็นชื่อผู้เข้าใช้งาน
        for i, e in enumerate(teach_file):
            if '%n%' in e:
                teach_file[i] = e.replace('%n%', user_name)
        for i, e in enumerate(answer_file):
            try:
                for  index,info in enumerate(e):
                    if '%n%' in info:
                        e[index] = e[index].replace('%n%', user_name)
                    if '%nl%' in info:
                        e[index] = e[index].replace('%nl%', '\n')
            except:
                if '%n%' in e:
                    answer_file[i] = e.replace('%n%', user_name)
                if '%nl%' in e:
                    answer_file[i] = e.replace('%nl%', '\n')

        for i in teach_file:
            if '%w%' in i:  # wait
                i = i.replace('%w%', '')
                print(i)
                self.wait()
            elif '%p%' in i:  # play
                i = i.replace('%p%', '')
                print(i)
                x = self.play()
            elif '%cp%' in i:  # compare print
                while x != answer_file[ia][0]:
                    print('โปรดพิมพ์', answer_file[ia][0])
                    x = self.play()
                else:
                    try:
                        # print(answer_file[ia][1])
                        exec(answer_file[ia][1])
                    except:
                        pass
                    # print(answer_file[ia][0])
                    exec(answer_file[ia][0])
                    print('นั่นแหละครับ คำตอบที่เราต้องการ')
                    ia += 1
                    self.wait()
            elif '%ca%' in i:  # compare answer
                while x != answer_file[ia][0]:
                    print('โปรดพิมพ์', answer_file[ia][0])
                    x = self.play()
                else:
                    try:
                        exec(answer_file[ia][1])
                    except:
                        pass
                    exec('print(' + (answer_file[ia][0]) + ')')
                    print('นั่นแหละครับ คำตอบที่เราต้องการ')
                    ia += 1
                    self.wait()
            else:
                print(i)


x = Cu_pypi()

# print(os.path.join(os.path.abspath(__file__)))
# print(os.getcwd())
# print(os.path.join(os.path.abspath(os.getcwd()), 'teach_file', ('สารบัญ' + '.txt')))
