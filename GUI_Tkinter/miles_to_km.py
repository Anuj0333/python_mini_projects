from tkinter import *

def click_button():
    new_value=float(input.get())
    KM=round(new_value*1.689,2)
    zero_lable.config(text=f"{KM}")

window=Tk()
window.title("Miles to KM converter")

window.minsize(width=500,height=400)
window.config(padx=200,pady=200)


input=Entry(width=20)
input.focus()
input.insert(END,string="cal from here")

print(input.get())
input.grid(column=1,row=0)

lable=Label(text="Miles")
lable.grid(column=3,row=0)

new_lable=Label(text="is equal to")
new_lable.grid(column=0,row=2)

zero_lable=Label(text="0")
zero_lable.grid(column=1,row=2)

new_lable=Label(text="Km")
new_lable.grid(column=2 ,row=2)

cal=Button(text="calculate",command=click_button)
cal.grid(column=1,row=3)




window.mainloop()