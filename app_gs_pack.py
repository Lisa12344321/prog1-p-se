import tkinter

inventory = []

main = tkinter.Tk()
main.geometry("600x500")
main.title("Påsen")

label = tkinter.Label(main, text= "Välkommen till påsen!")
label.pack(pady = 20)

text_box = tkinter.Text(main, height = 10)
text_box.pack(pady = 20)


#add
input_text_add = tkinter.Entry(main)
input_text_add.pack(pady = 5)

def add_to_bag(event=None):
    inventory.append(input_text_add.get())
    input_text_add.delete(0, tkinter.END)
    log()

def log():
    text_box.delete(1.0, tkinter.END)
    text_box.insert(tkinter.END,"\n".join(inventory) + "\n")


add_button = tkinter.Button(main,text="Spara i påsen", command=add_to_bag)
add_button.pack()


#remove
input_text_remove = tkinter.Entry(main)
input_text_remove.pack(pady = 5)

def remove_from_bag(event=None):
    inventory.remove(input_text_remove.get())
    log()


remove_button = tkinter.Button(main,text="Ta bort", command=remove_from_bag)
remove_button.pack()



exit_button = tkinter.Button(main, text="Avsluta", command=quit)
exit_button.pack(pady = 20)


main.mainloop()