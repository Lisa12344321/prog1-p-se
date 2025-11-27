import tkinter

inventory = []

main = tkinter.Tk()
main.geometry("600x500")
main.title("Påsen")




label = tkinter.Label(main, text= "Välkommen till påsen!")
label.grid(row=0, columnspan=2)

text_box = tkinter.Text(main, height=10)
text_box.grid(row=1, columnspan=2)


#add
input_text_add = tkinter.Entry(main)
input_text_add.grid(row=2, column=0, sticky=tkinter.W)

def add_to_bag(event=None):
    inventory.append(input_text_add.get())
    input_text_add.delete(0, tkinter.END)
    log()

def log():
    text_box.delete(1.0, tkinter.END)
    text_box.insert(tkinter.END,"\n".join(inventory) + "\n")


add_button = tkinter.Button(main,text="Spara i påsen", command=add_to_bag)
add_button.grid(row=2, column=0,)


#remove
input_text_remove = tkinter.Entry(main)
input_text_remove.grid(row=2,  column=1, sticky=tkinter.W)

def remove_from_bag(event=None):
    inventory.remove(input_text_remove.get())
    log()


remove_button = tkinter.Button(main,text="Ta bort", command=remove_from_bag)
remove_button.grid(row=2,  column=1)



exit_button = tkinter.Button(main, text="Avsluta", command=quit)
exit_button.grid(row=2,  column=1, sticky=tkinter.E)


main.mainloop()