import tkinter
window = tkinter.Tk()

window.title("Window Title")
window.geometry("300x300")
window.wm_iconbitmap()

lbl = tkinter.Label(window,text="Label")
ent = tkinter.Entry(window)
btn = tkinter.Button(window,text="Button")
lbl.pack()
ent.pack()
btn.pack()

window.mainloop()
