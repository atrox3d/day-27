import tkinter


def button_click():
    label["text"] = entry.get()


window = tkinter.Tk()
window.title("my first GUI program")
window.minsize(width=500, height=300)

# label

label = tkinter.Label(text="label", font=("Arial", 24, "bold"))
# center-top
label["text"] = "new text"
label.config(text="other text")
label.pack(side=tkinter.LEFT)

# button

button = tkinter.Button(text="button", command=button_click)
button.pack(side=tkinter.TOP)

# entry

entry = tkinter.Entry(width=10)
entry.pack(side=tkinter.RIGHT)

window.mainloop()
