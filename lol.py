import time
from PIL import ImageGrab
import cv2
from pathlib import Path
import numpy as np
from numba import jit
from pynput import keyboard
from threading import Thread
from lol2 import search_returnPoint
import tkinter as tk

scale = 1
##截图
datu = cv2.imread('./da.png')
##匹配模板
template = cv2.imread('./xiao.png')#图中的小图
template = cv2.resize(template, (0, 0), fx=scale, fy=scale)
template_size= template.shape[:2]
##屏幕
label = tk.Label(text='开始', font=('Times','30'), fg='black', bg='white')
label.master.overrideredirect(True)
label.master.geometry("+250+250")
label.master.lift()
label.master.wm_attributes("-topmost", True)
label.master.wm_attributes("-disabled", True)
label.master.wm_attributes("-transparentcolor", "white")
label.pack()
label.mainloop()
class ScreenshotVideo(Thread):
    def __init__(self,):
        """初始化参数"""
        super().__init__()

    def on_press(self, key):
        try:
            if key.char == 't':  # 录屏结束，保存视频
                print('开始1')
                img, x_, y_ = search_returnPoint(datu, template, template_size)
                if img is None:
                    print("没找到图片")
                else:
                    print("找到图片b 位置:" + str(x_) + " " + str(y_))
                    tk.Label(text="找到图片 位置:" + str(x_) + " " + str(y_), font=('Times', '30'), fg='black', bg='white')
                    print("找到图片f 位置:" + str(x_) + " " + str(y_))
        except Exception as e:
            print(e)

    def hotkey(self):
        """热键监听"""
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    @staticmethod
    def screenshot():
        """静态方法，屏幕截图，并转换为np.array数组"""
        return np.array(ImageGrab.grab())


    def run(self):
        # 运行函数
        # 设置守护线程
        Thread(target=self.hotkey, daemon=True).start()

sv = ScreenshotVideo().hotkey()

tk.Label(text="123", font=('Times', '30'), fg='black', bg='white')
