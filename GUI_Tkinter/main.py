import tkinter

def button_clicked(): 
    print("it will clicked")
    new_text=input.get()
    (my_label.config(text=new_text))



window=tkinter.Tk()
window.title("my first GUI program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)



# Labels
my_label=tkinter.Label(text="this is label",font=("Arial",24,"bold "))
my_label.pack( )

# my_label["text"]="new text"
my_label.config(text="new text")
my_label.config(text="new text")
my_label.grid(column=0,row=0)

#Button

button=tkinter.Button(text="click here",command=button_clicked)
# button.pack( )
button.grid(column=1,row=1)

new_button=tkinter.Button(text="click_here")
new_button.grid(row=0,column=2)

#Enitry
input=tkinter.Entry()
input.grid(column=3 ,row=3)
print(input.get())

window.mainloop()
