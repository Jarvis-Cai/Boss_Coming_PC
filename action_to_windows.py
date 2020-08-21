from win10toast import ToastNotifier
import time
import win32api, win32gui, win32con


def tips(loop_times=1):
    toaster = ToastNotifier()

    for i in range(loop_times):
        toaster.show_toast("YOU HAVE A MESSAGE",
                           "Maybe you should pay attention to this☜!",
                           icon_path="warning.ico",  # you can choose the show pic
                           duration=7,
                           threaded=True)
        while toaster.notification_active():
            time.sleep(0.1)


def open_window():
    win32api.ShellExecute(1, 'open',
                          r'"C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"',
                          '', '', 1)


def switch_window(A, C):
    """
    this function is just switch windows
    current two choices : which = AcrobatSDIWindow, Chrome_WidgetWin_1
    :return:
    """
    if A:
        which = 'AcrobatSDIWindow'
    elif C:
        which = 'Chrome_WidgetWin_1'

    ctjb = win32gui.FindWindow(which, None)
    win32gui.SetForegroundWindow(ctjb)
    win32gui.ShowWindow(ctjb, win32con.SW_MAXIMIZE)


if __name__ == '__main__':
    tips()
    switch_window(1, 0)
