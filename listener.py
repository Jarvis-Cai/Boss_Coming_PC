import socket
import sys
import action_to_windows as atw
from threading import Thread

test = 0


def show_to_the_gui():
    # 获取本机电脑名
    myname = socket.gethostname()
    # 获取本机ip
    myaddr = socket.gethostbyname(myname)
    return myaddr


class Work(Thread):
    def __init__(self, pdfreader, chrome, windows):
        self.pdfreader = pdfreader
        self.chrome = chrome
        self.windows = windows
        super().__init__()

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', 22222))
        while True:
            try:
                ret = sock.recvfrom(6)[0].decode()

                if ret == 'danger':
                    if self.pdfreader or self.chrome:
                        t1 = Thread(target=atw.switch_window, args=(self.pdfreader, self.chrome))
                        t1.start()
                    if self.windows:
                        t2 = Thread(target=atw.tips)
                        t2.start()
                else:
                    global test
                    test = 1

            except KeyboardInterrupt:
                print('Now we will exit')
                sys.exit(0)
        sock.close()


if __name__ == '__main__':
    a = Work(1, 0, 1)
    a.start()
