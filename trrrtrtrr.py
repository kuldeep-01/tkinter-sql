import customtkinter as ctk
import tkinter.messagebox as tkmb
import datetime
from tabulate import tabulate
import sqlite3

mydb = sqlite3.connect("emp_record.db")

cursor = mydb.cursor()
sql='''CREATE TABLE IF NOT EXISTS employee_record (
        name VARCHAR(50) NOT NULL,
        emp_no INT NOT NULL,phone_no DOUBLE NOT NULL,
        address VARCHAR(45) NOT NULL,
        username VARCHAR(45) NOT NULL,
        password VARCHAR(45) NOT NULL,
        type VARCHAR(45) NOT NULL,
        PRIMARY KEY (name));'''
cursor.execute(sql)

sql2='''CREATE TABLE IF NOT EXISTS complaint (
        date VARCHAR(45) NOT NULL,
        emp_no INT NOT NULL,
        name VARCHAR(50) NOT NULL,
        phone_no DOUBLE NOT NULL,
        address VARCHAR(45) NOT NULL,
        type VARCHAR(45) NOT NULL,
        description VARCHAR(500) NOT NULL,
        status VARCHAR(45) NOT NULL DEFAULT '-pending-',
        PRIMARY KEY (emp_no, address, type, description, status, phone_no));'''
cursor.execute(sql2)

ctk.set_appearance_mode("dark")

root=ctk.CTk()
root.geometry("900x600")
root.resizable(False, False)
root.state("zoomed")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.title("lolo_app")

#creation of frames

start=ctk.CTkFrame(root)  #first page 
user_login=ctk.CTkFrame(root)  #login page
user_signup=ctk.CTkFrame(root)  #sign up page
user_page=ctk.CTkFrame(root)  #user's dashboard

admin_login=ctk.CTkFrame(root)
admin_signup=ctk.CTkFrame(root)
admin_page=ctk.CTkFrame(root)

#############################################################################################################

#start -first page 
start_btn1=ctk.CTkButton(start, text="User login / Sign up", font=ctk.CTkFont(size=25, weight="bold"), width=500, height=100, command=user_login.tkraise)
start_btn1.pack(pady=100)
start_btn2=ctk.CTkButton(start, text="Admin Login", font=ctk.CTkFont(size=25, weight="bold"), width=500, height=100, command=admin_login.tkraise)
start_btn2.pack(pady=100)
start.grid(row=0, column=0, sticky="nsew")

#############################################################################################################

#admin_login -login page
admin_btn1=ctk.CTkButton(admin_login, text="Back", width=100, command=start.tkraise)
admin_btn1.place(y=5)
#------------------------------------------------------------------------------------------------------------
admin_label = ctk.CTkLabel(admin_login,text="Admin Log In", text_color="grey", font=ctk.CTkFont(size=25, weight="bold"))
admin_label.pack(pady=20)

admin_frame = ctk.CTkFrame(admin_login)  #admin_frame -fram in user_login frame
admin_frame.pack(pady=20,padx=40)

admin_entry= ctk.CTkEntry(admin_frame,placeholder_text="Username", width=150)
admin_entry.pack(pady=10,padx=10)

admin_pass= ctk.CTkEntry(admin_frame,placeholder_text="Password",show="*", width=150)
admin_pass.pack(pady=10,padx=10)

admin_checkbox = ctk.CTkCheckBox(admin_frame,text='Remember Me')
admin_checkbox.pack(pady=12,padx=10)

def login_verification():
    admin_verification = admin_entry.get()
    pass_verification = admin_pass.get()
    sql = "select * from employee_record where username = ? and password = ?"
    cursor.execute(sql,[(admin_verification),(pass_verification)])
    results = cursor.fetchall()
    if results and results[0][6]=="admin":
        for i in results:
            admin_page.tkraise()
            admin_page.grid(row=0, column=0, sticky="nsew")
            tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")
            admin_pass.delete(0, ctk.END)
            break
    else:
        tkmb.showinfo(title="Login Failed",message="Please, check your login credentials")
        admin_entry.delete(0, ctk.END)
        admin_pass.delete(0, ctk.END)

admin_button = ctk.CTkButton(admin_frame,text='Login', command=login_verification)
admin_button.pack(pady=12,padx=10)
admin_login.grid(row=0, column=0, sticky="nsew")
#------------------------------------------------------------------------------------------------------------
admin_btn2=ctk.CTkButton(admin_login, text="Sign Up", width=100, command=admin_signup.tkraise)
admin_btn2.pack(pady=10)
#------------------------------------------------------------------------------------------------------------
admin_btn3=ctk.CTkButton(admin_login, text="Cancel", width=100, command=start.tkraise)
admin_btn3.pack()

#############################################################################################################

#user_login -login page
user_btn1=ctk.CTkButton(user_login, text="Back", width=100, command=start.tkraise)
user_btn1.place(y=5)
#------------------------------------------------------------------------------------------------------------
user_label = ctk.CTkLabel(user_login,text="User Log In", text_color="grey", font=ctk.CTkFont(size=25, weight="bold"))
user_label.pack(pady=20)

user_frame = ctk.CTkFrame(user_login)  #user_frame -fram in user_login frame
user_frame.pack(pady=20,padx=40)

user_entry= ctk.CTkEntry(user_frame,placeholder_text="Username", width=150)
user_entry.pack(pady=10,padx=10)

user_pass= ctk.CTkEntry(user_frame,placeholder_text="Password",show="*", width=150)
user_pass.pack(pady=10,padx=10)

user_checkbox = ctk.CTkCheckBox(user_frame,text='Remember Me')
user_checkbox.pack(pady=12,padx=10)

def login_verification():
    user_verification = user_entry.get()
    pass_verification = user_pass.get()
    sql = "select * from employee_record where username = ? and password = ?"
    cursor.execute(sql,[(user_verification),(pass_verification)])
    results = cursor.fetchall()
    if results and results[0][6]=="user":
        for i in results:
            user_page.tkraise()
            user_page.grid(row=0, column=0, sticky="nsew")
            tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")
            user_pass.delete(0, ctk.END)
            break
    else:
        tkmb.showinfo(title="Login Failed",message="Please, check your login credentials")
        user_entry.delete(0, ctk.END)
        user_pass.delete(0, ctk.END)

user_button = ctk.CTkButton(user_frame,text='Login', command=login_verification)
user_button.pack(pady=12,padx=10)
user_login.grid(row=0, column=0, sticky="nsew")
#------------------------------------------------------------------------------------------------------------
user_btn2=ctk.CTkButton(user_login, text="Sign Up", width=100, command=user_signup.tkraise)
user_btn2.pack(pady=10)
#------------------------------------------------------------------------------------------------------------
user_btn3=ctk.CTkButton(user_login, text="Cancel", width=100, command=start.tkraise)
user_btn3.pack()

#############################################################################################################

#admin_page -admin's dashboard
ctk.CTkButton(admin_page, text="Back", width=100, command=user_login.tkraise).place(y=5)
ad1=ctk.CTkFrame(admin_page, width=890, height=50)
ad1.place(x=5,y=50)
ctk.CTkLabel(ad1,text="Admin's Dashboard", text_color="grey", font=ctk.CTkFont(size=25, weight="bold")).place(x=10,y=10)

#############################################################################################################

#user_page -user's dashboard
def home():
    sf3=ctk.CTkScrollableFrame(user_page, width=620, height=475)
    sf3.place(x=250,y=105)

    def add_complaint():
        if var.get()!='-select-':
            sql=("INSERT INTO complaint(`date`, `emp_no`, `name`, `phone_no`, `address`, `type`, `description`,`status`)""VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
            tab="select * from employee_record where username=?"
            data=[datetime.date.today()]
            cursor.execute(tab,[(user_entry.get())])
            results= cursor.fetchall()
            for row in results:
                print(row)
                a=row[1] #emp_no
                b=row[0] #name
                c=row[2] #phone_no
                d=row[3] #address
                print(a)
                data.append(a)
                data.append(b)
                data.append(c)
                data.append(d)
                data.append(var.get())
                data.append(tb.get(1.0, ctk.END))
                data.append("-pending-")
                print(data)
            data=tuple(data)
            print(data)
            try:
                cursor.execute(sql, data)
                mydb.commit()
                tkmb.showinfo(title="Successful",message="Your complaint is registered")          
            except:
                mydb.rollback()
                tkmb.showinfo(title="Successful",message="You are now registered")
        else:
            tkmb.showinfo(title="Message", message="Please select the complaint type")
            
    ctk.CTkLabel(sf3, text="Complaint Type").pack(pady=10) 
    option=['-select-','Crpainter work involving repair','Carpenter work involving Replacement','Sewer/Drainage choke','Indoor pipe leakage','Indoor roof leakage','No/Dirty water supply','Removal of Garbage','Whitewash/Colour wash/Painting','Masonary work','Water supply','Cleaning and sweeping','Horticultural work','Bridge and sheds','Blacksmith related work','Dead animal','Fallen tree','Water logging in quarter','Termite treatment','Any other']
    var=ctk.StringVar()
    var.set('-select-')
    drop = ctk.CTkOptionMenu(sf3, width=300, variable=var , values=option )
    drop.pack()
    ctk.CTkLabel(sf3, text="Describe your complaint").pack(pady=10)
    tb=ctk.CTkTextbox(sf3 , width=300, height=100)
    tb.pack(pady=10,padx=10)
    ctk.CTkButton(sf3, text="Add Complaint", width=350, height=50, command=add_complaint).pack(pady=10)

def profile():
    sf4=ctk.CTkScrollableFrame(user_page, width=620, height=475)
    sf4.place(x=250,y=105) 
    sql="select * from employee_record where emp_no=?"
    cursor.execute(sql,[(user_entry.get())])
    results= cursor.fetchall()

    ctk.CTkLabel(sf4, text="Profile of User : \t\t\t\t\t\t", font=ctk.CTkFont(size=16, weight="bold")).pack()

    #name
    ctk.CTkLabel(sf4, text="NAME :", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=10)
    ctk.CTkLabel(sf4, text=results[0][0], width=250, text_color="black", fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")).pack()
    
    #emp_no
    ctk.CTkLabel(sf4, text="EMPLOYEE NO :", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=10)
    ctk.CTkLabel(sf4, text=results[0][1], width=250, text_color="black", fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")).pack()
    
    #phone_no
    ctk.CTkLabel(sf4, text="PHONE NO :", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=10)
    ctk.CTkLabel(sf4, text=results[0][2], width=250, text_color="black", fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")).pack()

    #address
    ctk.CTkLabel(sf4, text="ADDRESS :", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=10)
    ctk.CTkLabel(sf4, text=results[0][3], width=250, text_color="black", fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")).pack()

    def edit():
        frm=ctk.CTkToplevel(sf4)
        frm.geometry("750x450")
        ctk.CTkLabel(frm, text="Edit your profile :",text_color="grey", font=ctk.CTkFont(size=16, weight="bold")).place(x=10, y=10)
        ctk.CTkLabel(frm, text="*edit the section you want to edit, leave the rest as it is").place(x=30,y=40)

        ctk.CTkLabel(frm, text="NAME :", font=ctk.CTkFont(size=14, weight="bold")).place(x=30, y=90)
        e1=ctk.CTkEntry(frm, width=250, placeholder_text=results[0][0])
        e1.place(x=150, y=90)

        ctk.CTkLabel(frm, text="EMPLOYEE NO :", font=ctk.CTkFont(size=14, weight="bold")).place(x=30, y=120)
        e2=ctk.CTkLabel(frm, width=250, text=results[0][1])
        e2.place(x=50, y=120)

        ctk.CTkLabel(frm, text="PHONE NO :",font=ctk.CTkFont(size=14, weight="bold")).place(x=30, y=150)
        e3=ctk.CTkEntry(frm, width=250, placeholder_text=results[0][2])
        e3.place(x=150, y=150)
        
        ctk.CTkLabel(frm, text="ADDRESS :", font=ctk.CTkFont(size=14, weight="bold")).place(x=30, y=180)
        e4=ctk.CTkEntry(frm, width=250, placeholder_text=results[0][3])
        e4.place(x=150, y=180)

        def apply():
            if e1.get() and e3.get() and e4.get():
                cursor.execute("UPDATE employee_record SET `name` = ?, `phone_no` = ?, `address` = ? WHERE `emp_no` = ?",(e1.get(),e3.get(),e4.get(),results[0][1]))
                cursor.execute("UPDATE complaint SET `name` = ?, `phone_no` = ?, `address` = ? WHERE `emp_no` = ?",(e1.get(),e3.get(),e4.get(),results[0][1]))
                mydb.commit()
            elif e1.get() and e3.get():
                cursor.execute("UPDATE employee_record SET `name` = ?, `phone_no` = ? WHERE `emp_no` = ?",(e1.get(),e3.get(),results[0][1]))
                cursor.execute("UPDATE complaint SET `name` = ?, `phone_no` = ? WHERE `emp_no` = ?",(e1.get(),e3.get(),results[0][1]))
                mydb.commit()
            elif e1.get() and e4.get():
                cursor.execute("UPDATE employee_record SET `name` = ?, `address` = ? WHERE `emp_no` = ?",(e1.get(),e4.get(),results[0][1]))
                cursor.execute("UPDATE complaint SET `name` = ?,`address` = ? WHERE `emp_no` = ?",(e1.get(),e4.get(),results[0][1]))
                mydb.commit()
            elif e3.get() and e4.get():
                cursor.execute("UPDATE employee_record SET  `phone_no` = ?, `address` = ? WHERE `emp_no` = ?",(e3.get(),e4.get(),results[0][1]))
                cursor.execute("UPDATE complaint SET `phone_no` = ?, `address` = ? WHERE `emp_no` = ?",(e3.get(),e4.get(),results[0][1]))
                mydb.commit()
            elif e1.get():
                cursor.execute("UPDATE employee_record SET `name` = ? WHERE `emp_no` = ?",(e1.get(),results[0][1]))
                cursor.execute("UPDATE complaint SET `name` = ? WHERE `emp_no` = ?",(e1.get(),results[0][1]))
                mydb.commit()
            elif e3.get():
                cursor.execute("UPDATE employee_record SET  `phone_no` = ? WHERE `emp_no` = ?",(e3.get(),results[0][1]))
                cursor.execute("UPDATE complaint SET `phone_no` = ? WHERE `emp_no` = ?",(e3.get(),results[0][1]))
                mydb.commit()    
            elif e4.get():
                cursor.execute("UPDATE employee_record SET `address` = ? WHERE `emp_no` = ?",(e4.get(),results[0][1]))
                cursor.execute("UPDATE complaint SET `address` = ? WHERE `emp_no` = ?",(e4.get(),results[0][1]))
                mydb.commit()        
 
            else:
                pass
            frm.destroy()
            sf.tkraise()

        ctk.CTkButton(frm, text="Apply", width=100, height=50, command=apply).place(x=200, y=300)

        frm.mainloop()
    
    ctk.CTkButton(sf4, text="Edit your profile", width=150, height=50, command=edit).pack(pady=20)




    sf4.mainloop()

def contact():
    sf5=ctk.CTkScrollableFrame(user_page, width=620, height=475)
    sf5.place(x=250,y=105)
    ctk.CTkLabel(sf5,text="BLW Maintainance Department \n BLW Colony, Varanasi (U.P)\n Pin code-221004 \n Phone no- 0542-5868589", font=ctk.CTkFont(size=20, weight="bold")).pack()

def history():
    sf6=ctk.CTkScrollableFrame(user_page, width=620, height=475)
    sf6.place(x=250, y=105)
    ctk.CTkLabel(sf6, text="Recent Complaints and their status:- \t\t\t\t\t", font=ctk.CTkFont(size=14, weight="bold"), text_color="grey").pack(pady=10)
    sql="select * from complaint where emp_no=?"
    cursor.execute(sql,[(user_entry.get())])
    results= cursor.fetchall()
    data=list(results)
    pn=tabulate(data, headers=["Date", "Emp_no", "Name", "Phone_no", "Address", "Type of complaint", "Description", "Status"])
    ctk.CTkLabel(sf6, text=pn).pack(pady=10)

    def tb_his():
        frm=ctk.CTkToplevel(sf6)
        frm.geometry("1100x750")

        txt=ctk.StringVar()
        txt.set("DATE")
        e = ctk.CTkEntry(frm, textvariable=txt, width=100, text_color="black", fg_color='grey',state="disabled", font=ctk.CTkFont(size=14, weight="bold")) 
        e.grid(row=0, column=0) 

            #emp_no
        txt1=ctk.StringVar()    
        txt1.set("EMP_NO")
        e = ctk.CTkEntry(frm, textvariable=txt1, width=100, text_color="black", fg_color='grey',state="disabled", font=ctk.CTkFont(size=14, weight="bold")) 
        e.grid(row=0, column=1) 
        
            #name
        txt2=ctk.StringVar()    
        txt2.set("NAME")
        e = ctk.CTkEntry(frm, textvariable=txt2, width=100, text_color="black", fg_color='grey',state="disabled", font=ctk.CTkFont(size=14, weight="bold")) 
        e.grid(row=0, column=2) 

            #phone_no

        txt3=ctk.StringVar()    
        txt3.set("PHONE_no")
        e = ctk.CTkEntry(frm, textvariable=txt3, width=100, text_color="black", fg_color='grey',state="disabled", font=ctk.CTkFont(size=14, weight="bold")) 
        e.grid(row=0, column=3) 
            #address

        txt4=ctk.StringVar()    
        txt4.set("ADDRESS")
        e = ctk.CTkEntry(frm, textvariable=txt4, width=100, text_color="black", fg_color='grey',state="disabled", font=ctk.CTkFont(size=14, weight="bold")) 
        e.grid(row=0, column=4) 
            #complaint_type

        txt5=ctk.StringVar()    
        txt5.set("COMPLAINT_TYPE")
        e = ctk.CTkEntry(frm, textvariable=txt5, width=200, text_color="black", fg_color='grey',state="disabled", font=ctk.CTkFont(size=14, weight="bold")) 
        e.grid(row=0, column=5) 
            #description

        txt6=ctk.StringVar()    
        txt6.set("DESCRIPTION")
        e = ctk.CTkEntry(frm, textvariable=txt6, width=300, text_color="black", fg_color='grey',state="disabled", font=ctk.CTkFont(size=14, weight="bold")) 
        e.grid(row=0, column=6) 
            #status

        txt7=ctk.StringVar()    
        txt7.set("STATUS")
        e = ctk.CTkEntry(frm, textvariable=txt7, width=100, text_color="black", fg_color='grey',state="disabled", font=ctk.CTkFont(size=14, weight="bold")) 
        e.grid(row=0, column=7) 

      

        i=1
        for student in results: 
            for j in range(len(student)):
                #date
                e = ctk.CTkEntry(frm, width=100, fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")) 
                e.grid(row=i, column=0) 
                e.insert(ctk.END, student[0])
                #emp_no
                e = ctk.CTkEntry(frm, width=100, fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")) 
                e.grid(row=i, column=1) 
                e.insert(ctk.END, student[1])
                #name
                e = ctk.CTkEntry(frm, width=100, fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")) 
                e.grid(row=i, column=2) 
                e.insert(ctk.END, student[2])
                #phone_no
                e = ctk.CTkEntry(frm, width=100, fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")) 
                e.grid(row=i, column=3) 
                e.insert(ctk.END, student[3])
                #address
                e = ctk.CTkEntry(frm, width=100, fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")) 
                e.grid(row=i, column=4) 
                e.insert(ctk.END, student[4])
                #complaint_type
                e = ctk.CTkEntry(frm, width=200, fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")) 
                e.grid(row=i, column=5) 
                e.insert(ctk.END, student[5])
                #description
                e = ctk.CTkEntry(frm, width=300, fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")) 
                e.grid(row=i, column=6) 
                e.insert(ctk.END, student[6])
                #status
                e = ctk.CTkEntry(frm, width=100, fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")) 
                e.grid(row=i, column=7) 
                e.insert(ctk.END, student[7])
            i=i+1
        frm.mainloop()

    ctk.CTkButton(sf6, text="Click for Tabular view", width=150, height=50, command=tb_his).pack(pady=200)

def logout():
    user_login.tkraise()
    user_login.selection_clear()

ctk.CTkButton(user_page, text="Back", width=100, command=user_login.tkraise).place(y=5)
sf1=ctk.CTkFrame(user_page, width=890, height=50)
sf1.place(x=5,y=50)
ctk.CTkLabel(sf1,text="User Dashboard", text_color="grey", font=ctk.CTkFont(size=25, weight="bold")).place(x=10,y=10)
sf2=ctk.CTkFrame(user_page, width=240, height=490)
sf2.place(x=5,y=105)

ctk.CTkButton(sf2, text="Profile", width=200, height=50, font=ctk.CTkFont(size=20, weight="bold"),command=profile).place(x=20,y=20)
ctk.CTkButton(sf2, text="Home", width=200, height=50, font=ctk.CTkFont(size=20, weight="bold"), command=home).place(x=20,y=90)
ctk.CTkButton(sf2, text="History", width=200, height=50, font=ctk.CTkFont(size=20, weight="bold"), command=history).place(x=20,y=160)
ctk.CTkButton(sf2, text="Contact Us", width=200, height=50, font=ctk.CTkFont(size=20, weight="bold"), command=contact).place(x=20,y=230)
ctk.CTkButton(sf2, text="Log Out", width=200, height=50, font=ctk.CTkFont(size=20, weight="bold"), command=logout).place(x=20,y=300)

sf=ctk.CTkScrollableFrame(user_page, width=620, height=475)
sf.place(x=250,y=105)
#---------------------------------
ctk.CTkLabel(sf, text="Complaint Type").pack(pady=10) 
option=['-select-','Crpainter work involving repair','Carpenter work involving Replacement','Sewer/Drainage choke','Indoor pipe leakage','Indoor roof leakage','No/Dirty water supply','Removal of Garbage','Whitewash/Colour wash/Painting','Masonary work','Water supply','Cleaning and sweeping','Horticultural work','Bridge and sheds','Blacksmith related work','Dead animal','Fallen tree','Water logging in quarter','Termite treatment','Any other']
var=ctk.StringVar()
var.set('-select-')
drop = ctk.CTkOptionMenu(sf, width=300, variable=var , values=option )
drop.pack()
ctk.CTkLabel(sf, text="Describe your complaint").pack(pady=10)
tb=ctk.CTkTextbox(sf , width=300, height=100)
tb.pack(pady=10,padx=10)
ctk.CTkButton(sf, text="Add Complaint", width=350, height=50, command=home).pack(pady=10)

#############################################################################################################

#admin_page -admin's dashboard
def admin_complaints():
    sql="select * from complaint"
    cursor.execute(sql)
    results= cursor.fetchall()

    def daily_complaint():
        frame=ctk.CTkToplevel(sf5)
        frame.geometry('900x600')
        frame.resizable(False,False)
        option=[]
        for i in range(1,len(results)+1):
            option.append(str(i))

        var=ctk.StringVar()
        var.set('1')
        drop = ctk.CTkOptionMenu(frame, width=100, variable=var , values=option )
        drop.place(x=400, y=5)

        fm=ctk.CTkScrollableFrame(frame, width=750, height=500)
        fm.place(x=70, y=50)
        def change():
                cursor.execute(("update complaint set status=? where type=? and description=?"),['completed', results[int(var.get())-1][5], results[int(var.get())-1][6]])
                mydb.commit()
                fm.tkraise()
        
        def nxt():
            sql="select * from complaint"
            cursor.execute(sql)
            results= cursor.fetchall()

            fm=ctk.CTkScrollableFrame(frame, width=750, height=500)
            fm.place(x=70, y=50)

            ctk.CTkLabel(fm, text="Page no:", font=ctk.CTkFont(size=12, weight="bold")).pack()
            ctk.CTkLabel(fm, text=int(var.get())).pack()

            ctk.CTkLabel(fm, text="Date",  font=ctk.CTkFont(size=12, weight="bold")).pack()
            ctk.CTkEntry(fm, width=250, placeholder_text=results[int(var.get())-1][0]).pack()

            ctk.CTkLabel(fm, text="Emp_no", font=ctk.CTkFont(size=12, weight="bold")).pack()
            ctk.CTkEntry(fm, width=250, placeholder_text=results[int(var.get())-1][1]).pack()

            ctk.CTkLabel(fm, text="Name", font=ctk.CTkFont(size=12, weight="bold")).pack()
            ctk.CTkEntry(fm, width=250, placeholder_text=results[int(var.get())-1][2]).pack()

            ctk.CTkLabel(fm, text="Phone_no", font=ctk.CTkFont(size=12, weight="bold")).pack()
            ctk.CTkEntry(fm, width=250, placeholder_text=results[int(var.get())-1][3]).pack()

            ctk.CTkLabel(fm, text="Address", font=ctk.CTkFont(size=12, weight="bold")).pack()
            ctk.CTkEntry(fm, width=250, placeholder_text=results[int(var.get())-1][4]).pack()

            ctk.CTkLabel(fm, text="Type of complaint", font=ctk.CTkFont(size=12, weight="bold")).pack()
            ctk.CTkEntry(fm, width=250, placeholder_text=results[int(var.get())-1][5]).pack()

            ctk.CTkLabel(fm, text="Description of complaint", font=ctk.CTkFont(size=12, weight="bold")).pack()
            ctk.CTkEntry(fm, width=250, placeholder_text=results[int(var.get())-1][6]).pack()

            ctk.CTkLabel(fm, text="Status", font=ctk.CTkFont(size=12, weight="bold")).pack()
            ctk.CTkEntry(fm, width=250, placeholder_text=results[int(var.get())-1][7]).pack()

        i=0
        ctk.CTkButton(frame, text="Refresh", width=100, command=nxt).place(x=800, y=5)
        ctk.CTkButton(frame, text="Change to completed",command=change).place(x=5, y=5)

        frame.tkraise()

    def table_complaint():
                
        frm=ctk.CTkToplevel(sf5)
        frm.geometry("1200x750")

        txt=ctk.StringVar()
        txt.set("DATE")
        e = ctk.CTkEntry(frm, textvariable=txt, width=100, text_color="black", fg_color='grey',state="disabled", font=ctk.CTkFont(size=14, weight="bold")) 
        e.grid(row=0, column=0) 
        
        #emp_no
        txt1=ctk.StringVar()    
        txt1.set("EMP_NO")
        e = ctk.CTkEntry(frm, textvariable=txt1, width=100, text_color="black", fg_color='grey',state="disabled", font=ctk.CTkFont(size=14, weight="bold")) 
        e.grid(row=0, column=1) 
        
        #name
        txt2=ctk.StringVar()    
        txt2.set("NAME")
        e = ctk.CTkEntry(frm, textvariable=txt2, width=100, text_color="black", fg_color='grey',state="disabled", font=ctk.CTkFont(size=14, weight="bold")) 
        e.grid(row=0, column=2) 

        #phone_no
        txt3=ctk.StringVar()    
        txt3.set("PHONE_no")
        e = ctk.CTkEntry(frm, textvariable=txt3, width=100, text_color="black", fg_color='grey',state="disabled", font=ctk.CTkFont(size=14, weight="bold")) 
        e.grid(row=0, column=3) 
           
        #address
        txt4=ctk.StringVar()    
        txt4.set("ADDRESS")
        e = ctk.CTkEntry(frm, textvariable=txt4, width=100, text_color="black", fg_color='grey',state="disabled", font=ctk.CTkFont(size=14, weight="bold")) 
        e.grid(row=0, column=4) 
        
        #complaint_type
        txt5=ctk.StringVar()    
        txt5.set("COMPLAINT_TYPE")
        e = ctk.CTkEntry(frm, textvariable=txt5, width=200, text_color="black", fg_color='grey',state="disabled", font=ctk.CTkFont(size=14, weight="bold")) 
        e.grid(row=0, column=5) 
        
        #description
        txt6=ctk.StringVar()    
        txt6.set("DESCRIPTION")
        e = ctk.CTkEntry(frm, textvariable=txt6, width=300, text_color="black", fg_color='grey',state="disabled", font=ctk.CTkFont(size=14, weight="bold")) 
        e.grid(row=0, column=6) 
        
        #status
        txt7=ctk.StringVar()    
        txt7.set("STATUS")
        e = ctk.CTkEntry(frm, textvariable=txt7, width=100, text_color="black", fg_color='grey',state="disabled", font=ctk.CTkFont(size=14, weight="bold")) 
        e.grid(row=0, column=7)

        i=1
        for student in results: 
            for j in range(len(student)):
                #date
                e = ctk.CTkEntry(frm, width=100, fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")) 
                e.grid(row=i, column=0) 
                e.insert(ctk.END, student[0])
                #emp_no
                e = ctk.CTkEntry(frm, width=100, fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")) 
                e.grid(row=i, column=1) 
                e.insert(ctk.END, student[1])
                #name
                e = ctk.CTkEntry(frm, width=100, fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")) 
                e.grid(row=i, column=2) 
                e.insert(ctk.END, student[2])
                #phone_no
                e = ctk.CTkEntry(frm, width=100, fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")) 
                e.grid(row=i, column=3) 
                e.insert(ctk.END, student[3])
                #address
                e = ctk.CTkEntry(frm, width=100, fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")) 
                e.grid(row=i, column=4) 
                e.insert(ctk.END, student[4])
                #complaint_type
                e = ctk.CTkEntry(frm, width=200, fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")) 
                e.grid(row=i, column=5) 
                e.insert(ctk.END, student[5])
                #description
                e = ctk.CTkEntry(frm, width=300, fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")) 
                e.grid(row=i, column=6) 
                e.insert(ctk.END, student[6])
                #status
                e = ctk.CTkEntry(frm, width=100, fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")) 
                e.grid(row=i, column=7) 
                e.insert(ctk.END, student[7])
            i=i+1
          
        frm.mainloop()
    
    sf5=ctk.CTkScrollableFrame(admin_page, width=620, height=475)
    sf5.place(x=250,y=105)
    ctk.CTkButton(sf5, text="View Complaints", width=250, height=50, command=daily_complaint).pack(pady=30)
    ctk.CTkButton(sf5, text="Tabular view of Complaints", width=250, height=50, command=table_complaint).pack(pady=50)

def admin_profile():
    sf4=ctk.CTkScrollableFrame(admin_page, width=620, height=475)
    sf4.place(x=250,y=105) 
    sql="select * from employee_record where emp_no=?"
    cursor.execute(sql,[(admin_entry.get())])
    results= cursor.fetchall()

    ctk.CTkLabel(sf4, text="Profile of Admin : \t\t\t\t\t\t", font=ctk.CTkFont(size=16, weight="bold")).pack()

    #name
    ctk.CTkLabel(sf4, text="NAME :", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=10)
    ctk.CTkLabel(sf4, text=results[0][0], width=250, text_color="black", fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")).pack()
    
    #emp_no
    ctk.CTkLabel(sf4, text="EMPLOYEE NO :", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=10)
    ctk.CTkLabel(sf4, text=results[0][1], width=250, text_color="black", fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")).pack()
    
    #phone_no
    ctk.CTkLabel(sf4, text="PHONE NO :", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=10)
    ctk.CTkLabel(sf4, text=results[0][2], width=250, text_color="black", fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")).pack()

    #address
    ctk.CTkLabel(sf4, text="ADDRESS :", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=10)
    ctk.CTkLabel(sf4, text=results[0][3], width=250, text_color="black", fg_color='grey', font=ctk.CTkFont(size=12, weight="bold")).pack()

    def edit():
        frm=ctk.CTkToplevel(sf4)
        frm.geometry("750x450")
        ctk.CTkLabel(frm, text="Edit your profile :",text_color="grey", font=ctk.CTkFont(size=16, weight="bold")).place(x=10, y=10)
        ctk.CTkLabel(frm, text="*edit the section you want to edit, leave the rest as it is").place(x=30,y=40)

        ctk.CTkLabel(frm, text="NAME :", font=ctk.CTkFont(size=14, weight="bold")).place(x=30, y=90)
        e1=ctk.CTkEntry(frm, width=250, placeholder_text=results[0][0])
        e1.place(x=150, y=90)

        ctk.CTkLabel(frm, text="EMPLOYEE NO :", font=ctk.CTkFont(size=14, weight="bold")).place(x=30, y=120)
        e2=ctk.CTkLabel(frm, width=250, text=results[0][1])
        e2.place(x=50, y=120)

        ctk.CTkLabel(frm, text="PHONE NO :",font=ctk.CTkFont(size=14, weight="bold")).place(x=30, y=150)
        e3=ctk.CTkEntry(frm, width=250, placeholder_text=results[0][2])
        e3.place(x=150, y=150)
        
        ctk.CTkLabel(frm, text="ADDRESS :", font=ctk.CTkFont(size=14, weight="bold")).place(x=30, y=180)
        e4=ctk.CTkEntry(frm, width=250, placeholder_text=results[0][3])
        e4.place(x=150, y=180)

        def apply():
            if e1.get() and e3.get() and e4.get():
                cursor.execute("UPDATE employee_record SET `name` = ?, `phone_no` = ?, `address` = ? WHERE `emp_no` = ?",(e1.get(),e3.get(),e4.get(),results[0][1]))
                cursor.execute("UPDATE complaint SET `name` = ?, `phone_no` = ?, `address` = ? WHERE `emp_no` = ?",(e1.get(),e3.get(),e4.get(),results[0][1]))
                mydb.commit()
            elif e1.get() and e3.get():
                cursor.execute("UPDATE employee_record SET `name` = ?, `phone_no` = ? WHERE `emp_no` = ?",(e1.get(),e3.get(),results[0][1]))
                cursor.execute("UPDATE complaint SET `name` = ?, `phone_no` = ? WHERE `emp_no` = ?",(e1.get(),e3.get(),results[0][1]))
                mydb.commit()
            elif e1.get() and e4.get():
                cursor.execute("UPDATE employee_record SET `name` = ?, `address` = ? WHERE `emp_no` = ?",(e1.get(),e4.get(),results[0][1]))
                cursor.execute("UPDATE complaint SET `name` = ?,`address` = ? WHERE `emp_no` = ?",(e1.get(),e4.get(),results[0][1]))
                mydb.commit()
            elif e3.get() and e4.get():
                cursor.execute("UPDATE employee_record SET  `phone_no` = ?, `address` = ? WHERE `emp_no` = ?",(e3.get(),e4.get(),results[0][1]))
                cursor.execute("UPDATE complaint SET `phone_no` = ?, `address` = ? WHERE `emp_no` = ?",(e3.get(),e4.get(),results[0][1]))
                mydb.commit()
            elif e1.get():
                cursor.execute("UPDATE employee_record SET `name` = ? WHERE `emp_no` = ?",(e1.get(),results[0][1]))
                cursor.execute("UPDATE complaint SET `name` = ? WHERE `emp_no` = ?",(e1.get(),results[0][1]))
                mydb.commit()
            elif e3.get():
                cursor.execute("UPDATE employee_record SET  `phone_no` = ? WHERE `emp_no` = ?",(e3.get(),results[0][1]))
                cursor.execute("UPDATE complaint SET `phone_no` = ? WHERE `emp_no` = ?",(e3.get(),results[0][1]))
                mydb.commit()    
            elif e4.get():
                cursor.execute("UPDATE employee_record SET `address` = ? WHERE `emp_no` = ?",(e4.get(),results[0][1]))
                cursor.execute("UPDATE complaint SET `address` = ? WHERE `emp_no` = ?",(e4.get(),results[0][1]))
                mydb.commit()        
 
            else:
                pass
            frm.destroy()
            sf.tkraise()

        ctk.CTkButton(frm, text="Apply", width=100, height=50, command=apply).place(x=200, y=300)
        frm.mainloop()
    ctk.CTkButton(sf4, text="Edit your profile", width=150, height=50, command=edit).pack(pady=20)
    sf4.mainloop()

def admin_logout():
    admin_login.tkraise()
    admin_login.selection_clear()

ctk.CTkButton(admin_page, text="Back", width=100, command=admin_login.tkraise).place(y=5)
sf1=ctk.CTkFrame(admin_page, width=890, height=50)
sf1.place(x=5,y=50)
ctk.CTkLabel(sf1,text="Admin's Dashboard", text_color="grey", font=ctk.CTkFont(size=25, weight="bold")).place(x=10,y=10)
sf2=ctk.CTkFrame(admin_page, width=240, height=490)
sf2.place(x=5,y=105)

ctk.CTkButton(sf2, text="Complaints", width=200, height=50, font=ctk.CTkFont(size=20, weight="bold"),command=admin_complaints).place(x=20,y=20)
ctk.CTkButton(sf2, text="Profile", width=200, height=50, font=ctk.CTkFont(size=20, weight="bold"), command=admin_profile).place(x=20,y=90)
ctk.CTkButton(sf2, text="Logout", width=200, height=50, font=ctk.CTkFont(size=20, weight="bold"), command=admin_logout).place(x=20,y=160)

sf=ctk.CTkScrollableFrame(admin_page, width=620, height=475)
sf.place(x=250,y=105)
ctk.CTkLabel(sf, text="\n\nWelcome to the Complaint Management system", font=ctk.CTkFont(size=20, weight="bold")).pack()

#############################################################################################################

#admin_signup -signup page for new user
admin_btn1=ctk.CTkButton(admin_signup, text="Back", width=100, command=admin_login.tkraise)
admin_btn1.place(y=5)
#------------------------------------------------------------------------------------------------------------
admin_label = ctk.CTkLabel(admin_signup,text="Admin Sign Up", text_color="grey", font=ctk.CTkFont(size=25, weight="bold"))
admin_label.pack(pady=20)

lb1= ctk.CTkLabel(admin_signup, text="Name", width=10)  
lb1.place(x=50,y=120)  
admin_signup_1= ctk.CTkEntry(admin_signup, placeholder_text="Enter your name", width=500)  
admin_signup_1.place(x=250, y=120)  
  
lb2= ctk.CTkLabel(admin_signup, text="Employee Number", width=10)  
lb2.place(x=50, y=160)  
admin_signup_2= ctk.CTkEntry(admin_signup, placeholder_text="Enter your employee number", width=500)  
admin_signup_2.place(x=250, y=160)  
  
lb3= ctk.CTkLabel(admin_signup, text="Contact Number", width=13)  
lb3.place(x=50, y=200)  
admin_signup_3= ctk.CTkEntry(admin_signup, placeholder_text="Enter your number", width=500)  
admin_signup_3.place(x=250, y=200)  
  
lb4= ctk.CTkLabel(admin_signup, text="Select Gender", width=15, font=("arial",12))  
lb4.place(x=50, y=240)  
vars=ctk.IntVar()  
a=ctk.CTkRadioButton(admin_signup, text="Male",variable=vars, value=1)
a.place(x=250, y=240)
b=ctk.CTkRadioButton(admin_signup, text="Female", variable=vars, value=2) 
b.place(x=350, y=240) 
c=ctk.CTkRadioButton(admin_signup, text="others", variable=vars, value=3)  
c.place(x=450, y=240)

lb5= ctk.CTkLabel(admin_signup, text="Address", width=13)  
lb5.place(x=50,y=280) 
admin_signup_5= ctk.CTkEntry(admin_signup, placeholder_text="Enter your Q.No", width=500)  
admin_signup_5.place(x=250, y=280) 

lb6= ctk.CTkLabel(admin_signup, text="Enter Password", width=13)  
lb6.place(x=50, y=320)  
admin_signup_6= ctk.CTkEntry(admin_signup, placeholder_text="Enter password", width=500, show='*')  
admin_signup_6.place(x=250, y=320)  
  
lb7= ctk.CTkLabel(admin_signup, text="Re-Enter Password", width=15)  
lb7.place(x=50, y=360)  
admin_signup_7 =ctk.CTkEntry(admin_signup, placeholder_text="Re-enter password", width=500, show='*')  
admin_signup_7.place(x=250, y=360) 

lb8= ctk.CTkLabel(admin_signup,text="*your employee number will be your username")
lb8.place(x=250, y=400)

admin_signup.grid(row=0, column=0, sticky="nsew")

def admin_submission():
    if (admin_signup_1.get() and admin_signup_2.get() and admin_signup_3.get() and admin_signup_5.get() and  admin_signup_6.get() and admin_signup_7.get()) and (admin_signup_6.get()==admin_signup_7.get()):
        sql=("INSERT INTO employee_record(`name`, `emp_no`, `phone_no`, `address`, `username`, `password`, `type`)""VALUES (?, ?, ?, ?, ?, ?, ?)")
        data = (admin_signup_1.get(), admin_signup_2.get(), admin_signup_3.get(), admin_signup_5.get(), admin_signup_6.get(), admin_signup_7.get(), "admin")
        print(data)
#        sql = "INSERT INTO `emp_record`.`employee_record` (`name`, `emp_no`, `phone_no`, `address`, `username`, `password`) VALUES (en1.get(), en2.get(), en3.get(), en5.get(), en2.get(), en6.get())"
        try:
            # Executing the SQL command
            cursor.execute(sql, data)
            # Commit your changes in the database
            mydb.commit()
            tkmb.showinfo(title="Sign Up Successful",message="You are now registered, you can now login")
            admin_signup_1.delete(0, ctk.END)
            admin_signup_2.delete(0, ctk.END)
            admin_signup_3.delete(0, ctk.END)
            admin_signup_5.delete(0, ctk.END)
            admin_signup_6.delete(0, ctk.END)
            admin_signup_7.delete(0, ctk.END)           
            admin_login.tkraise()

        except:
            # Rolling back in case of error
            mydb.rollback()
            tkmb.showinfo(title="Sign Up Successful",message="You are now registered, you can now login")
            admin_login.tkraise()
    else:
        tkmb.showinfo(title="Message",message="Please, enter your details correctly")

#------------------------------------------------------------------------------------------------------------
admin_btn2=ctk.CTkButton(admin_signup, text="Submit", width=100, command=admin_submission)
admin_btn2.place(x=250,y=450)
#------------------------------------------------------------------------------------------------------------
admin_btn3=ctk.CTkButton(admin_signup, text="Cancel", width=100, command=admin_login.tkraise)
admin_btn3.place(x=550,y=450)

#############################################################################################################

#user_signup -signup page for new user
user_btn1=ctk.CTkButton(user_signup, text="Back", width=100, command=user_login.tkraise)
user_btn1.place(y=5)
#------------------------------------------------------------------------------------------------------------
user_label = ctk.CTkLabel(user_signup,text="User Sign Up", text_color="grey", font=ctk.CTkFont(size=25, weight="bold"))
user_label.pack(pady=20)

lb1= ctk.CTkLabel(user_signup, text="Name", width=10)  
lb1.place(x=50,y=120)  
en1= ctk.CTkEntry(user_signup, placeholder_text="Enter your name", width=500)  
en1.place(x=250, y=120)  
  
lb2= ctk.CTkLabel(user_signup, text="Employee Number", width=10)  
lb2.place(x=50, y=160)  
en2= ctk.CTkEntry(user_signup, placeholder_text="Enter your employee number", width=500)  
en2.place(x=250, y=160)  
  
lb3= ctk.CTkLabel(user_signup, text="Contact Number", width=13)  
lb3.place(x=50, y=200)  
en3= ctk.CTkEntry(user_signup, placeholder_text="Enter your number", width=500)  
en3.place(x=250, y=200)  
  
lb4= ctk.CTkLabel(user_signup, text="Select Gender", width=15, font=("arial",12))  
lb4.place(x=50, y=240)  
vars=ctk.IntVar()  
a=ctk.CTkRadioButton(user_signup, text="Male",variable=vars, value=1)
a.place(x=250, y=240)
b=ctk.CTkRadioButton(user_signup, text="Female", variable=vars, value=2) 
b.place(x=350, y=240) 
c=ctk.CTkRadioButton(user_signup, text="others", variable=vars, value=3)  
c.place(x=450, y=240)

lb5= ctk.CTkLabel(user_signup, text="Address", width=13)  
lb5.place(x=50,y=280) 
en5= ctk.CTkEntry(user_signup, placeholder_text="Enter your Q.No", width=500)  
en5.place(x=250, y=280) 

lb6= ctk.CTkLabel(user_signup, text="Enter Password", width=13)  
lb6.place(x=50, y=320)  
en6= ctk.CTkEntry(user_signup, placeholder_text="Enter password", width=500, show='*')  
en6.place(x=250, y=320)  
  
lb7= ctk.CTkLabel(user_signup, text="Re-Enter Password", width=15)  
lb7.place(x=50, y=360)  
en7 =ctk.CTkEntry(user_signup, placeholder_text="Re-enter password", width=500, show='*')  
en7.place(x=250, y=360) 

lb8= ctk.CTkLabel(user_signup,text="*your employee number will be your username")
lb8.place(x=250, y=400)

user_signup.grid(row=0, column=0, sticky="nsew")

def submission():
    if (en1.get() and en2.get() and en3.get() and en5.get() and  en6.get() and en7.get()) and (en6.get()==en7.get()):
        sql=("INSERT INTO employee_record(`name`, `emp_no`, `phone_no`, `address`, `username`, `password`, `type`)""VALUES (?, ?, ?, ?, ?, ?, ?)")
        data = (en1.get(), en2.get(), en3.get(), en5.get(), en2.get(), en6.get(), "user")
        try:
            cursor.execute(sql, data)
            mydb.commit()
            tkmb.showinfo(title="Sign Up Successful",message="You are now registered, you can now login")
            en1.delete(0, ctk.END)
            en2.delete(0, ctk.END)
            en3.delete(0, ctk.END)
            en5.delete(0, ctk.END)
            en6.delete(0, ctk.END)
            en7.delete(0, ctk.END)           
            user_login.tkraise()

        except:
            mydb.rollback()
            tkmb.showinfo(title="Sign Up Successful",message="You are now registered, you can now login")
            user_login.tkraise()
    else:
        tkmb.showinfo(title="Message",message="Please, enter your details correctly")

#------------------------------------------------------------------------------------------------------------
user_btn2=ctk.CTkButton(user_signup, text="Submit", width=100, command=submission)
user_btn2.place(x=250,y=450)
#------------------------------------------------------------------------------------------------------------
user_btn3=ctk.CTkButton(user_signup, text="Cancel", width=100, command=user_login.tkraise)
user_btn3.place(x=550,y=450)

#############################################################################################################

start.tkraise()
root.mainloop()