from tkinter import *
root = Tk()

bg = "#00bbff"
btnbg = "#00ffff"
btnfg = "#005555"
acbg = "#00eeee"
root.config(background=bg)
labels = []

def view():
	mainframe.destroy()
	viewframe.pack()
	file = open("Contact Book.txt", "r")
	for line in file:
		label = Label(viewframe, text=line, bg=bg, font=("Comic Sans MS", 17))
		label.pack()
		labels.append(label)
	file.close()
	
def create():
	mainframe.destroy()
	createframe.pack()
	
def save():
	file = open("Contact Book.txt", "a")
	name = namebox.get()
	num = numbox.get()
	contact = name + " : " + num
	file.write(contact)
	file.close()
	
def delete():
	mainframe.destroy()
	delframe.pack()
	file = open("Contact Book.txt", "r")
	for line in file:
		btn = Button(delframe, text=line, bg=btnbg, fg="red", activebackground=acbg)
		btn["command"] = lambda b=btn: delit(b)
		btn.pack()
	file.close()
	
def delit(b):
	f = open("Contact Book.txt", "r")
	lines = f.readlines()
	f.close()
	newf = open("Contact Book.txt", "w")
	for line in lines:
		if line != b['text']:
			newf.write(line)
	newf.close()
	b.destroy()
	
def edit():
	mainframe.destroy()
	editframe.pack()
	file = open("Contact Book.txt", "r")
	for line in file:
		btn = Button(editframe, text=line, bg=btnbg, activebackground=acbg)
		btn["command"] = lambda b=btn: editit(b)
		btn.pack()
	file.close()
	
def editit(b):
	edititframe.pack()
	npn = b["text"]
	npnl = npn.split(" : ")
	name = npnl[0]
	num = npnl[1]
	nameentry.set(name)
	numentry.set(num)
	savebtne['command'] = lambda: savee(name, num)
	editframe.destroy()

def savee(name, num):
	newname = nameentry.get()
	newnum = numentry.get()
	f = open("Contact Book.txt", "r")
	lines = f.readlines()
	f.close()
	file = open("Contact Book.txt", "w")
	contact = name + " : " + num
	newcontact = newname + " : " + newnum 
	for line in lines:
		if line == contact:
			file.write(newcontact)
		else:
			file.write(line) 
	file.close()

def main_page():
	mainframe.pack()

mainframe = LabelFrame(root, bg=bg, padx=70, pady=100)

viewframe = LabelFrame(root, bg=bg)

createframe = LabelFrame(root, bg=bg, padx=30, pady=400)

delframe = LabelFrame(root, bg=bg)

editframe = LabelFrame(root, bg=bg)

edititframe = LabelFrame(root, bg=bg, padx=30, pady=400)

head = Label(mainframe, text="Contact Book", font=("Comic Sans MS", 25, 'underline'),
bg=bg)

createbtn = Button(mainframe, text=" New", padx=90, pady=100, bg=btnbg, font=("Comic Sans MS", 20), fg=btnfg, activebackground=acbg,command=create)

editbtn = Button(mainframe, text=" Edit ", bg=btnbg, font=("Comic Sans MS", 20), padx=90, pady=100, fg=btnfg, activebackground=acbg, command=edit)

delbtn = Button(mainframe, text=" Del", padx=110, pady=100, bg=btnbg, font=("Comic Sans MS", 20), fg=btnfg, activebackground=acbg, command=delete)

viewbtn = Button(mainframe, text="View", padx=90, pady=100, bg=btnbg, font=("Comic Sans MS", 20), fg=btnfg, activebackground=acbg, command=view)

namelbl = Label(createframe, text="Name: ", bg=bg, font=("Comic Sans MS", 20))
namebox = Entry(createframe)

numlbl = Label(createframe, text="Number: ", bg=bg, font=("Comic Sans MS", 20))
numbox = Entry(createframe)

savebtn = Button(createframe, text="Save", bg=btnbg, font=("Comic Sans MS", 20), padx=70, pady=10, fg=btnfg, activebackground=acbg, command=save)

nameentry = StringVar()
numentry = StringVar()

namelble = Label(edititframe, text="Name: ", bg=bg, font=("Comic Sans MS", 20))
nameboxe = Entry(edititframe, text=nameentry)

numlble = Label(edititframe, text="Number: ", bg=bg, font=("Comic Sans MS", 20))
numboxe = Entry(edititframe, text=numentry)

savebtne = Button(edititframe, text="Save", bg=btnbg, font=("Comic Sans MS", 20), padx=70, pady=10, fg=btnfg, activebackground=acbg)

head.pack()
createbtn.pack()
viewbtn.pack()
editbtn.pack()
delbtn.pack()
namelbl.grid(row=0, column=0)
namebox.grid(row=0, column=1)
numlbl.grid(row=1, column=0)
numbox.grid(row=1, column=1)
savebtn.grid(row=2,column=1)
namelble.grid(row=0, column=0)
nameboxe.grid(row=0, column=1)
numlble.grid(row=1, column=0)
numboxe.grid(row=1, column=1)
savebtne.grid(row=2, column=1)

main_page()
root.mainloop()
