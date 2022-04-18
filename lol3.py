import tkinter
import threading

from pynput.keyboard import Listener

class myThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)

    def run(self):
        def on_press(key):
            print('{0} 被按下'.format(key))
            func(key)
            print(threading.activeCount())
        # 创建监听
        with Listener(on_press=on_press) as listener:
            listener.join()

    @staticmethod
    def static_fun():
        print("xx")

win = tkinter.Tk()

str = tkinter.StringVar()
str.set("开始")
label = tkinter.Label(win, textvariable=str, bg="red")
label.master.overrideredirect(True)
label.master.geometry("+250+250")
label.master.lift()
label.master.wm_attributes("-topmost", True)
label.master.wm_attributes("-disabled", True)
label.master.wm_attributes("-transparentcolor", "white")
label.pack()


def func(key):
    str.set(key)
myThread.static_fun()
myThread = myThread()
myThread.start()

win.mainloop()
