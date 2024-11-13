from tkinter import *
root=Tk()
root.geometry("350x500")

label=Label(root, text="hello",font="50")
label.pack()

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

mylist= Listbox(root , yscrollcommand=scrollbar.set)

for line in range(1,26):
    mylist.insert(END , " Hi " + str(line))

    mylist.pack(side=LEFT , fill=BOTH)

root.mainloop()