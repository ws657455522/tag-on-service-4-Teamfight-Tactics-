import tkinter as tk

def key_action(event):
    print("pressed",repr(event.char))#按下时打印在工作台
    s=event.char
    labelText.set(s)#按下的字母记录到txt上
def callback(event):
    label.focus_set()#把键盘焦点设置到文本上

root = tk.Tk()
labelText = tk.StringVar()
labelText.set('123')
label = tk.Label(root, textvariable=labelText, font=('Times','30'), fg='black', bg='white')
label.master.overrideredirect(True)
label.master.geometry("+250+250")
label.master.lift()
label.master.wm_attributes("-topmost", True)
label.master.wm_attributes("-disabled", True)
label.master.wm_attributes("-transparentcolor", "white")
label.bind("<KeyPress>",key_action)
label.bind("<Button-1>",callback)#鼠标点下将回调回来到我点的地方

label.pack()
label.mainloop()
