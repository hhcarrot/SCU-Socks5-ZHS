#-*- coding: UTF-8 -*-
from tkinter import *
import tkinter

def hello():
	print('hello menu')
	
def isEncode():
	#v.set('check Tkinter')	
	print(varEncode.get())
	
def submit():
   print(v1.get())
   print(v2.get())
	
root = Tk()
varChooseList = StringVar(root)
varChooseList.set('公用服务器')
om = OptionMenu(root, varChooseList, '公用服务器', '私有服务器')
om.grid(row = 2)


#列表
lb = Listbox(root, height = 10)
for i in range(20):
	lb.insert(END, str(i*100)+'______________________________________!!!')
print(lb.curselection())
#print(lb.get(lb.curselection()))


sl1 = Scrollbar(root)
lb.configure(yscrollcommand = sl1.set)
sl1['command'] = lb.yview
sl1.grid(row = 5, column = 9, sticky = 'nsew')



sl2 = Scrollbar(root, orient = 'horizontal')
lb['xscrollcommand'] = sl2.set
sl2['command'] = lb.xview
sl2.grid(row = 6, column = 0, columnspan = 8, sticky = 'new')


lb.grid(row = 5, columnspan = 10)

#menubar = Menu(root)
#filemenu = Menu(menubar, tearoff = 0)
#for item in ['a', 'b', 'c']:
#	filemenu.add_command(label = item, command = hello)
#	filemenu.add_separator()
#menubar.add_cascade(label = 'Language', menu = filemenu)
#root['menu'] = menubar


fm = []
fm.append(Frame(height = 10, width = 50, bg = 'gray'))
fm.append(Frame(height = 10, width = 50))
Label(fm[0],text = '私有服务器配置',bg = 'gray').grid(row = 0, column = 0,columnspan = 2)

labUsername =Label(fm[0], text="用户名:", bg = 'gray')
labUsername.grid(row=2, column=0, padx=5, pady=5, sticky=W)
#绑定对象到Entry
varUsername = StringVar()	
enUsername = Entry(fm[0], textvariable=varUsername)
enUsername.grid(row=2, column=1, sticky='ew', columnspan=2)
	
labPassword = Label(fm[0], text="密码:",bg = 'gray')
labPassword.grid(row=3, column=0, padx=5, pady=5, sticky=W)
varPassword = StringVar()
enPassword = Entry(fm[0], textvariable=varPassword)
enPassword['show'] = '*'
enPassword.grid(row=3, column=1, sticky='ew', columnspan=2)

varEncode = StringVar()
varEncode.set('check Tkinter')
Checkbutton(fm[0], text = '加密',bg = 'gray', variable = varEncode, command = isEncode).grid(row=4)




fm[0].grid(row = 2, column = 10, rowspan = 6)

labPort =Label(fm[1], text="代理端口:")
labPort.grid(row=0, column=0, padx=4, pady=5, sticky=W)

varPort = StringVar() 
spinPort = Spinbox(fm[1], from_ = 0, to = 65535, increment = 1)
spinPort.grid(row=0, column=1, columnspan =2)

labNote =Label(fm[1], text="备注:")
labNote.grid(row=1, column=0, padx=5, pady=5, sticky=W)
#绑定对象到Entry
varNote = StringVar()	
enNote = Entry(fm[1], textvariable=varNote)
enNote.grid(row=1, column=1, sticky='ew', columnspan=3)

fm[1].grid(row = 6, column = 10, rowspan=5)

butSubmit = Button(fm[1], text="应用", command=submit, default='active')
butSubmit.grid(row=3, column=1)
butQuit = Button(fm[1], text="退出", command=quit)
butQuit.grid(row=3, column=2, columnspan = 2)

#lb1.grid()
#lb2.grid(row = 0, column = 1)
root.columnconfigure(0, minsize = 100)
root.mainloop()