#-*- coding: UTF-8 -*-
from tkinter import *
import tkinter
		
#需要传入的公共服务器与私有服务器列表
pubList = []
priList = []
#得到的结果，其中前两者为选择了公有or私有 及 该列表中的下标（从0起）
resServerList = None
resServerIndex = None
resUsername = None
resPassword = None
resEncode = None
resPort = None
resNote = None

#for test
for i in range(20):
	pubList.append('(pubic)'+str(i*100)+'______________________________________!!!')
	priList.append('(private)'+str(i*100)+'______________________________________!!!')

whichList = ('Public servers', pubList)

	
	
def freshList(v):
	global whichList
	if (v == "Public Servers"):
		whichList = ('Public Servers', pubList)
		enUsername['state'] = DISABLED
		enPassword['state'] = DISABLED
		butEncode['state'] = DISABLED
	else:
		whichList = ('Private Servers', priList)
		enUsername['state'] = NORMAL
		enPassword['state'] = NORMAL
		butEncode['state'] = NORMAL
	print(v+'loaded..')
	init()
	
def submit():
	global resServerList
	global resServerIndex 
	global resUsername 
	global resPassword 
	global resEncode
	global resPort 
	global resNote 
	print('select:')
	print(whichList[0])
	print(lb.curselection())
	print('username: ')
	print(varUsername.get())
	print('password: ')
	print(varPassword.get())
	print('encode: ')
	print(varEncode.get())
	print('port: ')
	print(spinPort.get())
	print('note: ')
	print(varNote.get())
	resServerList = whichList[0]
	resServerIndex = lb.curselection()
	resUsername = varUsername.get()
	resPassword = varPassword.get()
	resEncode = varEncode.get()
	resPort = spinPort.get()
	resNote = varNote.get()
	
	
#   print(v2.get())

root = Tk()
root.title("SHZHsocks")
varChooseList = StringVar(root)
om = OptionMenu(root, varChooseList, 'Public Servers', 'Private Servers', command = freshList)

lb = Listbox(root, height = 10)
sl1 = Scrollbar(root)
sl2 = Scrollbar(root, orient = 'horizontal')

fm = []
fm.append(Frame(height = 10, width = 50, bg = 'gray'))
fm.append(Frame(height = 10, width = 50))

labUsername =Label(fm[0], text="Username:", bg = 'gray')
varUsername = StringVar()	
enUsername = Entry(fm[0], textvariable=varUsername)

labPassword = Label(fm[0], text="Password:",bg = 'gray')
varPassword = StringVar()
enPassword = Entry(fm[0], textvariable=varPassword)
enPassword['show'] = '*'

varEncode = StringVar()
varEncode.set(0)
butEncode = Checkbutton(fm[0], text = 'Encode',bg = 'gray', variable = varEncode)
enUsername['state'] = DISABLED
enPassword['state'] = DISABLED
butEncode['state'] = DISABLED

labPort =Label(fm[1], text="Port:")
varPort = StringVar() 
spinPort = Spinbox(fm[1], from_ = 0, to = 65535, increment = 1)
labNote =Label(fm[1], text="Note:")

varNote = StringVar()	
enNote = Entry(fm[1], textvariable=varNote)
butSubmit = Button(fm[1], text="Submit", command=submit, default='active')
butQuit = Button(fm[1], text="Quit", command=quit)



	
def init():
	global varChooseList
	global lb
	varChooseList.set(whichList[0])
	print(whichList[0])
	om.grid(row = 2)
#列表
	
	lb.delete(0, lb.size())
	print(whichList[1])
	for item in whichList[1]:
		lb.insert(END, item)
	print(lb.curselection())
#print(lb.get(lb.curselection()))


	lb.configure(yscrollcommand = sl1.set)
	sl1['command'] = lb.yview
	sl1.grid(row = 5, column = 9, sticky = 'nsew')



	lb['xscrollcommand'] = sl2.set
	sl2['command'] = lb.xview
	sl2.grid(row = 6, column = 0, columnspan = 8, sticky = 'new')


	lb.grid(row = 5, columnspan = 10)


	Label(fm[0],text = 'Private Servers Configuration',bg = 'gray').grid(row = 0, column = 0,columnspan = 2)

	labUsername.grid(row=2, column=0, padx=5, pady=5, sticky=W)
	#绑定对象到Entry
	
	enUsername.grid(row=2, column=1, sticky='ew', columnspan=2)
	
	labPassword.grid(row=3, column=0, padx=5, pady=5, sticky=W)
	enPassword.grid(row=3, column=1, sticky='ew', columnspan=2)

	
	butEncode.grid(row=4)

	fm[0].grid(row = 2, column = 10, rowspan = 6)

	labPort.grid(row=0, column=0, padx=4, pady=5, sticky=W)

	spinPort.grid(row=0, column=1, columnspan =2)

	labNote.grid(row=1, column=0, padx=5, pady=5, sticky=W)
#绑定对象到Entry

	enNote.grid(row=1, column=1, sticky='ew', columnspan=3)

	fm[1].grid(row = 6, column = 10, rowspan=5)

	butSubmit.grid(row=3, column=1)
	butQuit.grid(row=3, column=2, columnspan = 2)

#lb1.grid()
#lb2.grid(row = 0, column = 1)
	root.columnconfigure(0, minsize = 100)
	root.mainloop()
	
init()