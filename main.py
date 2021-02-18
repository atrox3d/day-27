import tkinter


def button_click():
    label["text"] = entry.get()
    # button.grid(row=0, column=5)


window = tkinter.Tk()
window.title("my first GUI program")
window.minsize(width=500, height=300)

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

# button

button = tkinter.Button(text="button", command=button_click)
# button.pack(side=tkinter.TOP)
# button.place(x=0, y=50)
button.grid(row=1, column=1)


# entry

entry = tkinter.Entry(width=10)
# entry.pack(side=tkinter.RIGHT)
# entry.place(x=0, y=100)
entry.grid(column=2, row=2)



window.mainloop()
