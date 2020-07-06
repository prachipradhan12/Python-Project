from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from cx_Oracle import *
import cx_Oracle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import socket
import requests
import bs4
import re
def f1():
	root.withdraw()
	adst.deiconify()
def f2():
	adst.withdraw()
	root.deiconify()
def f3():
	con=None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		rno=entAddRno.get()
		chrno=entAddRno.get()
		chmarks=entAddMarks.get()
		chname=entAddName.get()
		numname=entAddName.get()
		name=entAddName.get()
		marks=entAddMarks.get()
		pattern=re.match('^[A-Z a-z]+$',chname)
		patrno=re.match('^[0-9 ]+$',chrno)
		patmarks=re.match('^[0-9 ]+$',chmarks)

		if (chrno.isalpha() or not patrno or int(rno) < 1 ):
			messagebox.showerror("Invalid Rno","Invalid rno entered")
			entAddRno.delete(0,END)
			entAddRno.focus()
		elif ((len(chname)<2) or not pattern ):
	
			messagebox.showerror("Invalid name","Invaild name Entered")
			entAddName.delete(0,END)
			entAddName.focus()

		elif (chmarks.isalpha() or not patmarks or int(marks)<0) or (int(marks)>100 ):
			messagebox.showerror("Invalid Marks","Invaild marks entered")
			entAddMarks.delete(0,END)
			entAddMarks.focus()
			
		else:
			rno=int(rno)
			name=name
			marks=int(marks)
			sql="insert into student values('%d', '%s','%d')"
			args=(rno,name,marks)
			cursor.execute(sql % args)
			con.commit()
			msg=str(cursor.rowcount)+"records inserted"
			messagebox.showinfo("Sahi kiya",msg)
			entAddRno.delete(0,END)
			entAddName.delete(0,END)
			entAddMarks.delete(0,END)
			entAddRno.focus()
			entAddName.focus()
			entAddMarks.focus()
	
	except  cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showinfo("Galat kiya",e)
	finally:
		if con is not None:
			con.close()

def f4():
	vist.withdraw()
	root.deiconify()
def f5():
	stdata.delete(1.0,END)
	root.withdraw()
	vist.deiconify()
	con=None
	try:
		con=cx_Oracle.connect("system/abc123")
		print("Connected")
		sql="select * from student Order by rno"
		cursor=con.cursor()
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=""
		for d in data:
			msg=msg=msg+"Rno:" + str(d[0]) + "   Name :"+str(d[1]) + "   Marks :"+str(d[2])+"\n"
		stdata.insert(INSERT,msg)
		
	
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror("Galat kiya",e)

	finally:
		if con is not None:
			con.close()
			print("disconnected")
def f6():
	root.withdraw()
	udst.deiconify()
def f7():
	udst.withdraw()
	root.deiconify()

def f8():
	con=None
	try:
		con=cx_Oracle.connect("system/abc123")
		rno=entUpdateRno.get()
		name=entUpdateName.get()
		marks=entUpdateMarks.get()
		chrno=entUpdateRno.get()
		chmarks=entUpdateMarks.get()
		chname=entUpdateName.get()
		pattern=re.match('^[A-Z a-z]+$',chname)
		patrno=re.match('^[0-9 ]+$',chrno)
		patmarks=re.match('^[0-9 ]+$',chmarks)

		if (chrno.isalpha() or not patrno or int(rno) < 1):
			messagebox.showerror("Invalid Rno","Invalid rno entered")
			entAddRno.delete(0,END)
			entAddRno.focus()
		elif ((len(name)<2) or not pattern):	
			messagebox.showerror("Invalid name","Invaild name Entered")
			entAddName.delete(0,END)
			entAddName.focus()

		elif (chmarks.isalpha() or not patmarks or int(marks)<0) or (int(marks)>100):
			messagebox.showerror("Invalid Marks","Invaild marks entered")
			entAddMarks.delete(0,END)
			entAddMarks.focus()
		else:	
			rno=int(rno)
			name=name
			marks=int(marks)

			cursor=con.cursor()
			sql="update student set name='%s',marks='%d' where rno='%d'"
			args=(name,marks,rno)
			cursor.execute(sql % args)
			con.commit()
			msg=str(cursor.rowcount)+"records updated "
			messagebox.showinfo("Sahi kiya",msg)
			entUpdateRno.delete(0,END)
			entUpdateName.delete(0,END)
			entUpdateMarks.delete(0,END)
			entUpdateRno.focus()
			entUpdateName.focus()
			entUpdateMarks.focus()
		
	except  cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showinfo("Galat kiya",e)
	finally:
		if con is not None:
			con.close()
def f9():
	root.withdraw()
	ddst.deiconify()	
def f10():
	ddst.withdraw()
	root.deiconify()
def f11():
	con=None
	try:
		con=connect("system/abc123")
		rno=entDeleteRno.get()
		chrno=entDeleteRno.get()
		patrno=re.match('^[0-9 ]+$',chrno)
		
		if (chrno.isalpha() or not patrno or int(rno) < 1):
			messagebox.showerror("Invalid Rno","Invalid rno entered")
			entDeleteRno.delete(0,END)
			entDeleteRno.focus()
		else:
			rno=int(rno)

			cursor=con.cursor()
			sql="delete from student where rno='%d'"
			args=(rno)
			cursor.execute(sql % args)
			con.commit()
			msg=str(cursor.rowcount)+"records Deleted"
			messagebox.showinfo("Sahi kiya",msg)
			entDeleteRno.delete(0,END)
			entDeleteRno.focus()
		
	except  DatabaseError as e:
		con.rollback()
		messagebox.showinfo("Galat kiya",e)
	finally:
		if con is not None:
			con.close()

def f12():
	root.withdraw()
	gpst.deiconify()
	con=None
	lname=[]
	lmarks=[]
	name=[]
	marks=[]
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="SELECT name,marks FROM (SELECT name,marks FROM student ORDER BY marks DESC)WHERE ROWNUM<=3"
		cursor.execute(sql)
		data=list(cursor.fetchall())
		for d in data:
			lname.append(d[0])
			lmarks.append(d[1])
		rdict=dict(zip(lname, lmarks))
		ldict=sorted(rdict.items(), key=lambda x: x[1]) 		
		for key, value in ldict:
			name.append(key)
			marks.append(value)
		name=name[-5:]
		marks=marks[-5:]
		x=np.arange(len(name))
		plt.bar(x,marks,width=0.3,label='marks')
		plt.xticks(x,name)
		plt.xlabel("Name")
		plt.ylabel("Marks")
		plt.title("STUDENTS DATA")
		plt.legend()
		plt.show()
		
	except DatabaseError as e:
		messagebox.showerror("Graph invisible")
	finally:
		if con is  not None:
			con.close()



def f13():
	gpst.withdraw()
	root.deiconify()

root=Tk()
root.title("Student Management System")
root.geometry("900x800+200+70")
btnAdd=Button(root,text="Add",width=10,font=("arial",20,'bold'),command=f1)
btnView=Button(root,text="View",width=10,font=("arial",20,'bold'),command=f5)
btnUpdate=Button(root,text="Update",width=10,font=("arial",20,'bold'),command=f6)
btnDelete=Button(root,text="Delete",width=10,font=("arial",20,'bold'),command=f9)
btnGraph=Button(root,text="Graph",width=10,font=("arial",20,'bold'),command=f12)
fetchdata= scrolledtext.ScrolledText(root,width=70,height=4,font=('airal',15,'bold'))
btnAdd.pack(pady=20)
btnView.pack(pady=20)
btnUpdate.pack(pady=20)
btnDelete.pack(pady=20)
btnGraph.pack(pady=20)
fetchdata.pack(pady=5)



try:
	socket.create_connection(("www.google.com", 80))
	res = requests.get("https://ipinfo.io")
	data = res.json()
	city = data['city']
	a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2="&q="+city
	a3="&appid=c6e315d09197cec231495138183954bd"
	api_address=a1+a2+a3;
	res1=requests.get(api_address)
	data=res1.json()
	temp=data['main']['temp']

	fetchdata.insert(INSERT,"\n*Mumbai--> ")
	fetchdata.insert(INSERT,temp)
	res=requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
	soup=bs4.BeautifulSoup(res.text,'lxml')
	quote=soup.find('img',{"class":"p-qotd"})
	text=quote['alt']
	fetchdata.insert(INSERT,"\n*Quotes of today--> ")
	fetchdata.insert(INSERT,text)
	fetchdata.insert(INSERT,"\n")

	
except OSError:
	fetchdata.insert(INSERT,"**Network error check your internet connection.** ")

adst=Toplevel(root)
adst.title("Add student")
adst.geometry("500x500+300+100")
adst.withdraw()

lblAddRno=Label(adst,text="Enter rno",font=('arial',18,'bold'))
lblAddName=Label(adst,text="Enter name",font=('arial',18,'bold'))
lblAddMarks=Label(adst,text="Enter marks",font=('arial',18,'bold'))
entAddRno=Entry(adst,bd=2,font=('arial',18,'bold'))
entAddName=Entry(adst,bd=2,font=('arial',18,'bold'))
entAddMarks=Entry(adst,bd=2,font=('arial',18,'bold'))
btnAddSave=Button(adst,text="Save",font=('arial',18,'bold'),command=f3)
btnAddBack=Button(adst,text="Back",font=('arial',18,'bold'),command=f2)

lblAddRno.pack(pady=5)
entAddRno.pack(pady=5)
lblAddName.pack(pady=5)
entAddName.pack(pady=5)
lblAddMarks.pack(pady=5)
entAddMarks.pack(pady=5)
btnAddSave.pack(pady=5)
btnAddBack.pack(pady=5)

vist=Toplevel(root)
vist.title("View student")
vist.geometry("500x500+300+100")
vist.withdraw()

stdata=scrolledtext.ScrolledText(vist,width=70,height=20)
btnViewBack=Button(vist,text="Back",font=('arial',18,'bold'),command=f4)

stdata.pack(pady=5)
btnViewBack.pack(pady=5)

udst=Toplevel(root)
udst.title("Update student")
udst.geometry("500x500+300+100")
udst.withdraw()

lblUpdateRno=Label(udst,text="Enter rno",font=('arial',18,'bold'))
lblUpdateName=Label(udst,text="Enter name",font=('arial',18,'bold'))
lblUpdateMarks=Label(udst,text="Enter marks",font=('arial',18,'bold'))
entUpdateRno=Entry(udst,bd=2,font=('arial',18,'bold'))
entUpdateName=Entry(udst,bd=2,font=('arial',18,'bold'))
entUpdateMarks=Entry(udst,bd=2,font=('arial',18,'bold'))
btnUpdateSave=Button(udst,text="Save",font=('arial',18,'bold'),command=f8)
btnUpdateBack=Button(udst,text="Back",font=('arial',18,'bold'),command=f7)
lblUpdateRno.pack(pady=5)
entUpdateRno.pack(pady=5)
lblUpdateName.pack(pady=5)
entUpdateName.pack(pady=5)
lblUpdateMarks.pack(pady=5)
entUpdateMarks.pack(pady=5)
btnUpdateSave.pack(pady=5)
btnUpdateBack.pack(pady=5)

ddst=Toplevel(root)
ddst.title("Delete student")
ddst.geometry("500x500+300+100")
ddst.withdraw()

lblDeleteRno=Label(ddst,text="Enter rno",font=('arial',18,'bold'))
entDeleteRno=Entry(ddst,bd=2,font=('arial',18,'bold'))
btnDeleteDelete=Button(ddst,text="Delete",font=('arial',18,'bold'),command=f11)
btnDeleteBack=Button(ddst,text="Back",font=('arial',18,'bold'),command=f10)
lblDeleteRno.pack(pady=5)
entDeleteRno.pack(pady=5)
btnDeleteDelete.pack(pady=5)
btnDeleteBack.pack(pady=5)

gpst = Toplevel(root)
gpst.title("Graph student")
gpst.geometry("1000x1000+300+100")
gpst.withdraw()
btnGraphBack=Button(gpst,text="Back",font=('arial',18,'bold'),command=f13)
btnGraphBack.pack(pady=5)





root.mainloop()
