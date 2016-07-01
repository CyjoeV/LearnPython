# import tkinter module
import tkinter

# create new window
window = tkinter.Tk()

# set window title
window.title("Window Title")

# set window size
window.geometry("300x300")

# set window icon(icon.ico)
window.wm_iconbitmap()

# create label 
lbl = tkinter.Label(window,text="Label")

# create text entry
ent = tkinter.Entry(window)

# create button
btn = tkinter.Button(window,text="Button")

# pack(add) the widgets into the window
lbl.pack()
ent.pack()
btn.pack()

# start application
window.mainloop()
