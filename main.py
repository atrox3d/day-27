import tkinter


def button_click():
    label["text"] = entry.get()
    # button.grid(row=0, column=5)


window = tkinter.Tk()
window.title("my first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# label

label = tkinter.Label(text="label", font=("Arial", 24, "bold"))
# add constant
tkinter.TEXT = "text"
# use it
label[tkinter.TEXT] = "new text"
label.config(text="other text")
# label.pack(side=tkinter.LEFT)
# label.place(x=0, y=0)
label.grid(row=0, column=0)
label.config(padx=50, pady=50)

# button

button = tkinter.Button(text="button", command=button_click)
# button.pack(side=tkinter.TOP)
# button.place(x=0, y=50)
button.grid(row=1, column=1)

# newbutton

newbutton = tkinter.Button(text="button", command=button_click)
# button.pack(side=tkinter.TOP)
# button.place(x=0, y=50)
newbutton.grid(row=0, column=2)


# entry

entry = tkinter.Entry(width=10)
# entry.pack(side=tkinter.RIGHT)
# entry.place(x=0, y=100)
entry.grid(row=2, column=3)


#       0     1     2     3
#    +-----+-----+-----+-----+
# 0  |  L  |     |  B  |     |
#    +-----+-----+-----+-----+
# 1  |     |  B  |     |     |
#    +-----+-----+-----+-----+
# 2  |     |     |     |  E  |
#    +-----+-----+-----+-----+



window.mainloop()
