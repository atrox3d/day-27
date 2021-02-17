import tkinter

window = tkinter.Tk()
window.title("my first GUI program")
window.minsize(width=500, height=300)

# label

label = tkinter.Label(text="label", font=("Arial", 24, "bold"))
# center-top
label.pack()
label.pack()
label["text"] = "new text"
label.config(text="other text")


# button

def button_click():
    label["text"] = "Click"


button = tkinter.Button(text="button", command=button_click)
button.pack()

window.mainloop()
