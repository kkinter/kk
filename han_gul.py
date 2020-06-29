from tkinter import *
import re
window = Tk()

def han():
    pattern = re.compile(r'[가-힛]{1,4}')
    match = re.search(pattern , e1_value.get())
    result = match.group()
    t1.delete("1.0", END)
    t1.insert(END,result)
    


b1 = Button(window, text="변환", command=han)
b1.grid(row=0,column=0)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0, column=1)

t1= Text(window,height=2,width=20)
t1.grid(row=0,column=2)

window.mainloop()
