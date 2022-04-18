import tkinter as tk

def key_press(event):
    if event.keysym == 'space':
        print('pressed')

def key_release(event):
    if event.keysym == 'space':
        print('released')


def update_label():
    # get the time from the string
    time = float(timer_label.get()[:-1])

    # increment the time and put it back in timer_label
    timer_label.set(str(time+1) + 's')

    # calling this function again 1000ms later, which will call this again 1000ms later, ...
    main.after(1000, update_label)

main = tk.Tk()
main.title("Cube Timer Mark 4 Prototype")
main.resizable(0,0)

tk.Label(main, text="Cube Time Mk3 Prototype", font=['Consolas',16]).grid(row = 0,column=0)
textbox = tk.Text(main,font=['Consolas',20], height = 1,width = 27)
textbox.grid(row = 1,column=0)
#textbox.insert('1.0',scrambler())
timer_frame = tk.Frame(main).grid(row=2,column=0)

timer_label = tk.StringVar()
timer_label.set("0.0s")

# using textvariable, you can simply update timer_label and it will be reflected
tk.Label(timer_frame,textvariable = timer_label ,font=['Consolas',20,'bold'],pady = 25).grid(row = 2,column = 0)

# bind keypress and keyrelease to the functions
main.bind("<KeyPress>", key_press)
main.bind("<KeyRelease>", key_release)

# call update label function for the first time
update_label()
main.mainloop()