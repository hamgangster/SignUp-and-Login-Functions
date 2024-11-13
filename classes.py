import os 
from tkinter import Tk

class SignUp :
    def __init__(self,NewName,Email,Pass):
        self.__name=NewName
        self.__Email=Email
        self.__password=Pass
    def file(self):
        with open('Names.txt','a') as f:
            f.write(f'{self.__name},\n')
        with open ('Mail.txt','a') as f :
            f.write(f'{self.__Email},\n')
        with open('pasword.txt','a')as f :
            f.write(f'{self.__password},\n')
        
class DataBase :
    def __init__(self):
     with open('Names.txt','r')as f :
         self.t1=f.read()
     self.newName=self.t1.split(',')
     with open('Mail.txt','r')as f :
         self.t2=f.read()
     self.newMail=self.t2.split(',')
     with open('pasword.txt','r')as f:
         self.t3=f.read() 
     self.newpass=self.t3.split(',')

    def Store(self):
        self.lis1=[]
        self.lis2=[]
        self.lis3=[]
        for self.i in self.newName:
            if not self.i.strip()=='':
             self.lis1.append(self.i.strip())
        
        for self.i in self.newMail:
            if not self.i.strip()=='':
             self.lis2.append(self.i.strip())
       
        for self.i in self.newpass:
           if not self.i.strip()=='':
              self.lis3.append(self.i.strip())
      
class Check(DataBase):
   def __init__(self):
      super().__init__()
      self.Namedic={}
      self.Maildic={}
     
   def Store_(self):
      super().Store()
      if len(self.lis1)==len(self.lis3) and len(self.lis2)==len(self.lis3) and len(self.lis1)==len(self.lis2):
         for i in range(len(self.lis1)):
          self.Namedic[self.lis1[i]]=self.lis3[i]
          self.Maildic[self.lis2[i]]=self.lis3[i]
      else:
         return False
if __name__=='__main__':       
  o=Check()
  o.Store_()
  print(o.Maildic)