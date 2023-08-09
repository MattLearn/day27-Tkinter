import tkinter

# basic setup
window = tkinter.Tk()
window.title("Basic Window Program")
window.minsize(width=750, height=550)

# labels
label = tkinter.Label(text="Label")
label.grid(column=0, row=0)

# button event
def button_clicked():
    label.config(text=input.get())


# buttons
button = tkinter.Button(text="click here", command=button_clicked)
button.grid(column=1, row=1)
button2 = tkinter.Button(text="Another one", command=button_clicked)
button2.grid(column=2, row=0)

# entry component
input = tkinter.Entry()
input.grid(column=3, row=3)

# code to make window not automatically close
window.mainloop()

# *args to have a function take unlimited variables which is read as a tuple
# def add(*args):
#     sum = 0
#     for num in args:
#         sum += num
#     print(f"{args} numbers adding up to {sum}")
#
# add(5,4,3,2,8,9)

# **kwargs is like *args however tha values passed through are keyword arguments aka dicts.
# def calculate(**kwargs):
#     n = 0
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     n -= kwargs["subtract"]
#     n /= kwargs["divide"]
#     print(n)
#
# calculate(add=3, multiply=5, subtract=2, divide=1)
