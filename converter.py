from Tkinter import *

from convert import *


def calculate_celsius(event):
    temp = int(entry1.get())
    temp = conv_C(temp)
    output_label.configure(text='Converted into Celsius: {:.2f}'.format(temp))
    entry1.delete(0, END)


def calculate_fahrenheit(event):
    temp = int(entry2.get())
    temp = conv_F(temp)
    output_label.configure(text='Converted into Fahrenheit: {:.2f}'.format(temp))
    entry2.delete(0, END)


root = Tk()

root.wm_title('Temperature Converter')

message_label1 = Label(text='Enter a Fahrenheit temperature', font=('Verdana', 16))
message_label2 = Label(text='Enter a Celsius temperature', font=('Verdana', 16))

output_label = Label(font=('Verdana', 16))

entry1 = Entry(font=('Verdana', 16), width=4)
entry1.bind('<Return>', calculate_celsius)
entry2 = Entry(font=('Verdana', 16), width=4)
entry2.bind('<Return>', calculate_fahrenheit)

message_label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
message_label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
output_label.grid(row=2, column=0, columnspan=3)

root.mainloop()
