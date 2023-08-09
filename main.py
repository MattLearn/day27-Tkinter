import tkinter

# Miles to Kilometer Converter

window = tkinter.Tk()
window.title("Miles to Kilometer Converter")


def conversion_m_km():
    to_km.set(float(m_to_km.get())*0.62)
    km_to_m.config(textvariable=to_km)


def conversion_km_m():
    to_m.set(float(km_to_m.get()) * 1.61)
    m_to_km.config(textvariable=to_m)


def clear_values():
    to_m.set(0)
    to_km.set(0)
    m_to_km.config(textvariable=to_m)
    km_to_m.config(textvariable=to_km)


# 1 Button fields
clear_btn = tkinter.Button(text="Clear", command=clear_values)
conv_to_km = tkinter.Button(text="Convert to Km", width=14, command=conversion_m_km)
conv_to_m = tkinter.Button(text="Convert to m", width=14, command=conversion_km_m)

# 2 Entry fields
to_m = tkinter.StringVar()
to_km = tkinter.StringVar()
m_to_km = tkinter.Entry()
km_to_m = tkinter.Entry()


# 2-3 Labels
m_label = tkinter.Label(text="Miles")
km_label = tkinter.Label(text="Km")

# load to grid 3x3
m_to_km.grid(column=1, row=0)
conv_to_km.grid(column=0, row=0)
conv_to_m.grid(column=0, row=1)
m_label.grid(column=2, row=0)
km_to_m.grid(column=1, row=1)
km_label.grid(column=2, row=1)
clear_btn.grid(column=1, row=2)

window.mainloop()
