#-*- coding: UTF-8 -*-
from tkinter import *
import tkinter




class guiObject(object):
	def __init__(self, root, publ, pril):
		self.varChooseList = StringVar(root)
		self.om = OptionMenu(root, self.varChooseList, 'Public Servers', 'Private Servers', command = self.freshList)

		self.lb = Listbox(root, height = 10)
		self.sl1 = Scrollbar(root)
		self.sl2 = Scrollbar(root, orient = 'horizontal')

		self.fm = []
		self.fm.append(Frame(height = 10, width = 50, bg = 'gray'))
		self.fm.append(Frame(height = 10, width = 50))

		self.labUsername =Label(self.fm[0], text="Username:", bg = 'gray')
		self.varUsername = StringVar()	
		self.enUsername = Entry(self.fm[0], textvariable=self.varUsername)

		self.labPassword = Label(self.fm[0], text="Password:",bg = 'gray')
		self.varPassword = StringVar()
		self.enPassword = Entry(self.fm[0], textvariable=self.varPassword)
		self.enPassword['show'] = '*'

		self.varEncode = StringVar()
		self.varEncode.set(0)
		self.butEncode = Checkbutton(self.fm[0], text = 'Encode',bg = 'gray', variable = self.varEncode)
		self.enUsername['state'] = DISABLED
		self.enPassword['state'] = DISABLED
		self.butEncode['state'] = DISABLED

		self.labPort =Label(self.fm[1], text="Port:")
		self.varPort = StringVar() 
		self.spinPort = Spinbox(self.fm[1], from_ = 0, to = 65535, increment = 1)
		self.labNote =Label(self.fm[1], text="Note:")

		self.varNote = StringVar()	
		self.enNote = Entry(self.fm[1], textvariable=self.varNote)
		self.butSubmit = Button(self.fm[1], text="Submit", command=self.submit, default='active')
		self.butQuit = Button(self.fm[1], text="Quit", command=quit)
		self.pubList = publ
		self.priList = pril
		self.whichList = ('Public servers', self.pubList)
		self.resServerList = None
		self.resServerIndex = None
		self.resUsername = None
		self.resPassword = None
		self.resEncode = None
		self.resPort = None
		self.resNote = None
		self.init()
		
		
	def freshList(self, v):
		if (v == "Public Servers"):
			self.whichList = ('Public Servers', self.pubList)
			self.enUsername['state'] = DISABLED
			self.enPassword['state'] = DISABLED
			self.butEncode['state'] = DISABLED
		else:
			self.whichList = ('Private Servers', self.priList)
			self.enUsername['state'] = NORMAL
			self.enPassword['state'] = NORMAL
			self.butEncode['state'] = NORMAL
		print(v+'loaded..')
		self.init()
		
	def submit(self):
		print('select:')
		print(self.whichList[0])
		print(self.lb.curselection())
		print('username: ')
		print(self.varUsername.get())
		print('password: ')
		print(self.varPassword.get())
		print('encode: ')
		print(self.varEncode.get())
		print('port: ')
		print(self.spinPort.get())
		print('note: ')
		print(self.varNote.get())
		self.resServerList = self.whichList[0]
		self.resServerIndex = self.lb.curselection()
		self.resUsername = self.varUsername.get()
		self.resPassword = self.varPassword.get()
		self.resEncode = self.varEncode.get()
		self.resPort = self.spinPort.get()
		self.resNote = self.varNote.get()
		
	def init(self):

		self.varChooseList.set(self.whichList[0])
		print(self.whichList[0])
		self.om.grid(row = 2)
#列表
	
		self.lb.delete(0, self.lb.size())
		print(self.whichList[1])
		for item in self.whichList[1]:
			self.lb.insert(END, item)
		print(self.lb.curselection())
#print(lb.get(lb.curselection()))


		self.lb.configure(yscrollcommand = self.sl1.set)
		self.sl1['command'] = self.lb.yview
		self.sl1.grid(row = 5, column = 9, sticky = 'nsew')



		self.lb['xscrollcommand'] = self.sl2.set
		self.sl2['command'] = self.lb.xview
		self.sl2.grid(row = 6, column = 0, columnspan = 8, sticky = 'new')


		self.lb.grid(row = 5, columnspan = 10)


		Label(self.fm[0],text = 'Private Servers Configuration',bg = 'gray').grid(row = 0, column = 0,columnspan = 2)

		self.labUsername.grid(row=2, column=0, padx=5, pady=5, sticky=W)
	#绑定对象到Entry
	
		self.enUsername.grid(row=2, column=1, sticky='ew', columnspan=2)
	
		self.labPassword.grid(row=3, column=0, padx=5, pady=5, sticky=W)
		self.enPassword.grid(row=3, column=1, sticky='ew', columnspan=2)

	
		self.butEncode.grid(row=4)

		self.fm[0].grid(row = 2, column = 10, rowspan = 6)

		self.labPort.grid(row=0, column=0, padx=4, pady=5, sticky=W)

		self.spinPort.grid(row=0, column=1, columnspan =2)

		self.labNote.grid(row=1, column=0, padx=5, pady=5, sticky=W)
#绑定对象到Entry

		self.enNote.grid(row=1, column=1, sticky='ew', columnspan=3)

		self.fm[1].grid(row = 6, column = 10, rowspan=5)

		self.butSubmit.grid(row=3, column=1)
		self.butQuit.grid(row=3, column=2, columnspan = 2)

#lb1.grid()
#lb2.grid(row = 0, column = 1)
		root.columnconfigure(0, minsize = 100)
		
		
		
	def getWhichList(self):
		return self.resServerList
	
	def getServerIndex(self):
		return self.resServerIndex
		
	def getUsername(self):
		return self.resUsername
		
	def getPassword(self):
		return self.resPassword
	
	def getIsEncode(self):
		return self.resEncode
		
	def getPort(self):
		return self.resPort
		
	def getNote(self):
		return self.resNote 


pubList = []
priList = []
#for test
for i in range(20):
	pubList.append('(pubic)'+str(i*100)+'______________________________________!!!')
	priList.append('(private)'+str(i*100)+'______________________________________!!!')

root = Tk()
root.title("SHZHsocks")

test = guiObject(root, pubList, priList)	
print(test.getWhichList())
print(test.getServerIndex())
print(test.getUsername())
print(test.getPassword())
print(test.getIsEncode())
print(test.getPort)
print(test.getNote())

root.mainloop()
