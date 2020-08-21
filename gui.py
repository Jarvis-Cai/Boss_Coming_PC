# boss coming 1.0.0
# author: caijiawei

import tkinter as tk
import listener as Li

window = tk.Tk()
window.title('Boss coming')
window.geometry('500x300')


test = tk.Label(window, bg='yellow', width=20, text='wait for test...')
test.pack()


def test_fn():
    if Li.test:
        test.config(text='test finished!!!', bg='green')


# show the local ip
IP_address = Li.show_to_the_gui()
label = tk.Label(window, text="Your IP address is:%s" % IP_address)
label.pack()

label = tk.Label(window, text="choose what software you want to switch to: ☟")
label.pack()

# 第5步，定义两个Checkbutton选项并放置
var1 = tk.IntVar()  # 定义var1和var2整型变量用来存放选择行为返回值
var2 = tk.IntVar()
var3 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Adobe Acrobat Reader', variable=var1, onvalue=1, offvalue=0)  # 传值原理类似于radiobutton部件
c1.pack()
c2 = tk.Checkbutton(window, text='Chrome', variable=var2, onvalue=1, offvalue=0)
c2.pack()
c3 = tk.Checkbutton(window, text='Windows system message', variable=var3, onvalue=1, offvalue=0)
c3.pack()

b = tk.Button(window, text='start', command=lambda: Li.Work(var1.get(), var2.get(), var3.get()).start()).place(x=190, y=240)
b1 = tk.Button(window, text='test ', command=test_fn).place(x=270, y=240)


window.mainloop()
