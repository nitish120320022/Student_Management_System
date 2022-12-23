from tkinter import * 
from tkinter import ttk
import mysql.connector 
from mysql.connector import Error
from tkinter import messagebox



 
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Managment System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Managment System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="cyan",fg="black")
        title.pack(side=TOP,fill=X)

   ######### All Variable===========================
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.search_by=StringVar()
        self.search_text=StringVar()


    ##########  Manage Frame===========================================
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=580)  # 560

    

        m_title=Label(Manage_Frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10) # 20


        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")


        text_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        text_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")


        lbl_name=Label(Manage_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")


        text_name=Entry(Manage_Frame,textvariable= self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        text_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")


        lbl_Email=Label(Manage_Frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        text_email=Entry(Manage_Frame,textvariable= self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        text_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")


        lbl_Gender=Label(Manage_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        # text_Gender=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        # text_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable= self.gender_var,font=("times new roman",13,"bold"),state="readonly")
        combo_gender["values"]=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        

        lbl_Contact=Label(Manage_Frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        text_Contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        text_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")


        lbl_Dob=Label(Manage_Frame,text="D.O.B",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        text_Dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        text_Dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")


        lbl_Address=Label(Manage_Frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.text_Address=Text(Manage_Frame,width=30,height=4,font=("times new roman",10))
        self.text_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")


# ########### Button Frame============================

        btn_Frame=Frame(Manage_Frame,bd=2,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=15,y=500,width=420)

        Addbtn=Button(btn_Frame,text="Add",width=8,command=self.add_student).grid(row=0,column=0,padx=8,pady=8)
        updatebtn=Button(btn_Frame,text="Update",width=8,command=self.update_data).grid(row=0,column=1,padx=8,pady=8)
        deletebtn=Button(btn_Frame,text="Delete",width=8,command=self.delete_data).grid(row=0,column=2,padx=8,pady=8)
        clearbtn=Button(btn_Frame,text="Clear",width=8,command=self.clear).grid(row=0,column=3,padx=8,pady=8)


        


# # # ##########  Details Frame===========================================

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=800,height=580) # 560      


        lbl_Search=Label(Detail_Frame,text="Search By ",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        

        combo_Search=ttk.Combobox(Detail_Frame, textvariable=self.search_by,width=9, font=("times new roman",13,"bold"),state="readonly")
        combo_Search["values"]=("Roll_No","Name","Contact")
        combo_Search.grid(row=0,column=1,padx=20,pady=10)


        text_Search=Entry(Detail_Frame,textvariable=self.search_text,width=20, font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        text_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=8,pady=5,command=self.search_data).grid(row=0,column=3,padx=8,pady=8)
        showallbtn=Button(Detail_Frame,text="Show All",width=8,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=8,pady=8)


############ Table Frame===========================

        Tabel_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Tabel_Frame.place(x=10,y=70,width=760,height=500)


        SCROLL_x=Scrollbar(Tabel_Frame,orient=HORIZONTAL)
        SCROLL_y=Scrollbar(Tabel_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Tabel_Frame,columns=("Roll","Name","Email","Gender","Contact","Dob","Address"),xscrollcommand=SCROLL_x.set,yscrollcommand=SCROLL_y.set)
        SCROLL_x.pack(side=BOTTOM,fill=X)
        SCROLL_y.pack(side=RIGHT,fill=Y)
        SCROLL_x.config(command=self.Student_table.xview)
        SCROLL_y.config(command= self.Student_table.yview)
        self.Student_table.heading("Roll",text = "Roll No.")
        self. Student_table.heading("Name",text = "Name ")
        self.Student_table.heading("Email",text = "Email")
        self.Student_table.heading("Gender",text = "Gender")
        self.Student_table.heading("Contact",text = "Contact")
        self.Student_table.heading("Dob",text="dob")
        self.Student_table.heading("Address",text = "Address")
        self.Student_table["show"]= "headings"
        self. Student_table.column("Roll",width=100)
        self.Student_table.column("Name",width=100)
        self. Student_table.column("Email",width=100)
        self. Student_table.column("Gender",width=100)
        self.Student_table.column("Contact",width=100)
        self.Student_table.column("Dob",width=100)
        self.Student_table.column("Address",width=150)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
    def add_student(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),self.name_var.get(),
        self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.text_Address.get('1.0',END)
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def fetch_data(self):
       con=mysql.connector.connect(host="localhost",user="root",password="",database="stm")
       cur=con.cursor()
       cur.execute("select * from students") 
       rows=cur.fetchall()
       print(rows)
       if len(rows)!=0:
               self.Student_table.delete(*self.Student_table.get_children())
               for row in rows:
                       self.Student_table.insert('',END,values=row)
               con.commit()
       con.close()
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.text_Address.delete("1.0",END)

    def get_cursor(self,ev):
        curosor_row= self.Student_table.focus()
        contents=self.Student_table.item(curosor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.text_Address.delete("1.0",END)
        self.text_Address.insert(END,row[6])
   
    def update_data(self):
         con=mysql.connector.connect(host="localhost",user="root",password="",database="stm")
         cur=con.cursor()
         cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s Where roll_no=%s",(self.name_var.get(),
        self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.text_Address.get('1.0',END),self.Roll_No_var.get()
        ))
         con.commit()
         self.fetch_data()
         self.clear()
         con.close()
         
    def delete_data(self):
       con=mysql.connector.connect(host="localhost",user="root",password="",database="stm")
       cur=con.cursor()
       cur.execute(f"delete from students where roll_no={self.Roll_No_var.get()}")
       con.commit()
       con.close() 
       self.fetch_data()
       self.clear()

    def search_data(self):
       con=mysql.connector.connect(host="localhost",user="root",password="",database="stm")
       cur=con.cursor()
       cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'") 
       rows=cur.fetchall()
       if len(rows)!=0:
               self.Student_table.delete(*self.Student_table.get_children())
               for row in rows:
                       self.Student_table.insert('',END,values=row)
               con.commit()
       
root=Tk()
ob=Student(root)
root.mainloop()