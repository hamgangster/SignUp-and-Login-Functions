from tkinter import *
from tkinter import messagebox
import time
import os 
import classes as cs
logger=False
def clear():
   for widget in root.winfo_children():
      widget.destroy()

def LogIN():
   def p():
      NameEmail=NameEmailEntry.get()
      Pass=PassEntery.get()
      if NameEmail=="" or Pass=="":
         messagebox.showerror("ERROR","Please Enter Name or Email and Passsword")
      check=cs.DataBase()
      check.Store()
      
      check2=cs.Check()
      check2.Store_()
      if '@gmail.com' in NameEmail:
         
         if NameEmail in check.lis2:
            
            if check2.Maildic[NameEmail]==Pass:
               clear()
               Label(root,text="LogedIn").pack()
            else:
               messagebox.showerror("Error","Wrong Email or Password")
      else:
         if NameEmail in check.lis1:
            if check2.Namedic[NameEmail]==Pass:
               clear()
               Label(root,text='LogedIn').pack()
            else:
               messagebox.showerror('Error',"Wrong Name or Password")
         

   clear()
   Label(root,text='Enter Name or Email').pack()
   NameEmailEntry=StringVar()
   Entry(root,textvariable=NameEmailEntry).pack()
   Label(root,text='Enter Password').pack()
   PassEntery=StringVar()
   Entry(root,textvariable=PassEntery).pack()
   Button(root,text="Login",command=p).pack()
   Button(root,text='Back',command=main).pack()
def main():
    clear()
    def Sginin():
      
         Name=NameEntry.get()
         print(Name)
         Email=EmailEntry.get()
         Password=PassEntry.get()
         if Name == "" or Email == "" or Password == "":
             messagebox.showerror('Error', 'Please Enter Name, Email, and Password')
             return
         Insiate=cs.SignUp('','','')
         Insiate.file()   
         CheckIn=cs.DataBase()
         CheckIn.Store()
         if Name in CheckIn.lis1:
            messagebox.showinfo('Name Already Exists')
         elif Email in CheckIn.lis2:
            messagebox.showinfo('Email Already in Use')
         else:
           
             if '@gmail.com' in Email: 
                if len(Password)>6:
                 
                 Sined=cs.SignUp(Name,Email,Password)
                 Sined.file()
                 logger=True
                 if logger ==True:
                    with open('Log.txt','a') as f:
                       f.write(f'{Name} signed up With Email {Email} on {time.strftime("%Y-%m-%d %H:%M:%S")}')
                 messagebox.showinfo("Succesfuly Signed In")
                else:
                 messagebox.showinfo("Password Length Must Be Greater Than 6 Letter")
             else:
                messagebox.showerror('Email Error','Entered Email Format is Wrong') 
             
         NameEntry.set('') 
         EmailEntry.set('')
         PassEntry.set('')
            
    Label(root,text='Name',borderwidth=5).pack()
    NameEntry=StringVar()
    Entry(root,textvariable=NameEntry).pack()
    Label(root,text="Email",borderwidth=5).pack()
    EmailEntry=StringVar()
    Entry(root,textvariable=EmailEntry).pack()
    Label(root,text='Password').pack()
    PassEntry=StringVar()
    Entry(root,textvariable=PassEntry).pack()
    Button(root,text='SignUp',command=Sginin).pack()
    Button(root,text='LogIn',command=LogIN).pack()

root=Tk()
root.geometry('400x400')
root.maxsize(400,400)
root.minsize(400,400)
main()
root.mainloop()
