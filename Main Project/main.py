from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as pk
import mysql.connector
import random
from tkinter import messagebox
from os import system
import psycopg2
import datetime
import smtplib

connectiondb =psycopg2.connect(host="127.0.0.1",user="postgres",password="admin",database="login_system", port = "5432")
cursordb = connectiondb.cursor()

import smtplib, ssl
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "otpv6777@gmail.com"
password = "wwdyzvjygbgmwalm"

    
#main frame size
root= Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(True, True)


def adddb():
    username = user1.get()
    password = pass1.get()
    email = email1.get()
    ques1 = ques11.get()
    ques2 = ques22.get()
    ques3 = ques33.get()
    cursordb.execute("INSERT INTO login1 (username, password, email_id, ans1, ans2, ans3) VALUES (%s, %s, %s, %s, %s, %s)",
                       (username, password, email, ques1, ques2, ques3))
    connectiondb.commit()
    connectiondb.close()
    messagebox.showinfo("Congratulations", "Data added successfully!") 
    lab1.destroy()
    lab2.destroy()
    lab3.destroy()
    lab4.destroy()
    lab5.destroy()
    lab6.destroy()
    user1.destroy()
    pass1.destroy()
    email1.destroy()
    ques11.destroy()
    ques22.destroy()
    ques33.destroy()
    btnentry1.destroy()
    btnsub = pk.Button(root, text="REGISTER",  font = ("times new roman",12,"bold"),fg="orange", command=register,
                    bg = "white" ,padx = 2, width = 20)
    btnsub.place(y = 550, x = 280)
    btnadd = pk.Button(root, text="LOGIN",  font = ("times new roman",12,"bold"),fg="orange", command=level1,
                        bg = "white" ,padx = 2, width = 20)

    btnadd.place(y = 500, x = 280)

def register():
    new_image = pk.PhotoImage(file="1.png")
    label.config(image=new_image)
    label.image = new_image
    btnadd.destroy()
    btnsub.destroy()
    global lab1
    global lab2
    global lab3
    global lab4
    global lab5
    global lab6
    global btnentry1
    global user1
    global pass1
    global email1
    global ques11
    global ques22
    global ques33
    lab1 = Label(root,font = ("Arial",12,"bold"), text = "Enter username: ", fg = 'orange')
    lab1.place(x=130, y=400)
    user1 = Entry(root,font=('arial', 15, 'bold'), relief = RIDGE)
    user1.place(x = 400, y =399)
    lab2 = Label(root,font = ("Arial",12,"bold"), text = "Enter password: ", fg = 'orange')
    lab2.place(x=130, y=450)
    pass1 = Entry(root,font=('arial', 15, 'bold'), relief = RIDGE)
    pass1.place(x = 400, y =449)
    lab3 = Label(root,font = ("Arial",12,"bold"), text = "Enter Email ID: ", fg = 'orange')
    lab3.place(x=130, y=500)
    email1 = Entry(root,font=('arial', 15, 'bold'), relief = RIDGE)
    email1.place(x = 400, y =499)
    lab4 = Label(root,font = ("Arial",12,"bold"), text = "Favorite animal: ", fg = 'orange')
    lab4.place(x=130, y=550)
    ques11 = Entry(root,font=('arial', 15, 'bold'), relief = RIDGE)
    ques11.place(x = 400, y =549)
    lab5 = Label(root,font = ("Arial",12,"bold"), text = "Favorite color: ", fg = 'orange')
    lab5.place(x=130, y=600)
    ques22 = Entry(root,font=('arial', 15, 'bold'), relief = RIDGE)
    ques22.place(x = 400, y =599)
    lab6 = Label(root,font = ("Arial",12,"bold"), text = "Most valuable thing to you: ", fg = 'orange')
    lab6.place(x=130, y=650)
    ques33 = Entry(root,font=('arial', 15, 'bold'), relief = RIDGE)
    ques33.place(x = 400, y =649)
    btnentry1 = Button(root,text="Enter",  font = ("times new roman",12,"bold"),fg="orange", command= adddb,
                        bg = "white" ,padx = 2, width = 20)
    btnentry1.place(y = 649, x = 700)
    


def level1():
    new_image = pk.PhotoImage(file="2.png")
    label.config(image=new_image)
    label.image = new_image
    btnadd.destroy()
    btnsub.destroy()
    global username_verification
    global password_verification
    global lbluser1
    global lblpass1
    global entrypass1
    global entryuser1
    global btnenter1
    username_verification = StringVar()
    password_verification = StringVar()
    lbluser1 = Label(root,font = ("Arial",12,"bold"), text = "Enter username: ", fg = 'orange')
    lbluser1.place(x=30, y=300)
    entryuser1 = Entry(root, textvariable=username_verification, font=('arial', 15, 'bold'), relief = RIDGE)
    entryuser1.place(x = 30, y =350)
    lblpass1 = Label(root,font = ("Arial",12,"bold"), text = "Enter password: ", fg = 'orange')
    lblpass1.place(x=30, y=400)
    entrypass1 = Entry(root, textvariable=password_verification, show="*",font=('arial', 15, 'bold'), relief = RIDGE)
    entrypass1.place(x = 30, y =450)
    btnenter1 = Button(root,text="Enter",  font = ("times new roman",12,"bold"),fg="orange", command= checkme,
                        bg = "white" ,padx = 2, width = 20)
    btnenter1.place(y = 550, x = 65)

def level2():
    new_image = pk.PhotoImage(file="3.png")
    label.config(image=new_image)
    label.image = new_image
    btnenter1.destroy()
    lbluser1.destroy()
    entryuser1.destroy()
    entrypass1.destroy()
    lblpass1.destroy()
    global lbluser2
    global entryuser2
    global btnenter2
    otp_send()
    lbluser2 = Label(root,font = ("Arial",12,"bold"), text = "Enter OTP sent to your registered mail id:", fg = 'orange')
    lbluser2.place(x=350, y=400)
    entryuser2 = Entry(root, font=('arial', 15, 'bold'), relief = RIDGE, highlightcolor="orange", highlightthickness=2)
    entryuser2.place(x = 400, y =450)
    btnenter2 = Button(root,text="Enter",  font = ("times new roman",12,"bold"),fg="White", command = checkme1,
                        bg = "orange" ,padx = 2, width = 20)
    btnenter2.place(y = 500, x = 420)

def level3():
    new_image = pk.PhotoImage(file="4.png")
    label.config(image=new_image)
    label.image = new_image
    lbluser2.destroy()
    entryuser2.destroy()
    btnenter2.destroy()
    global verify1
    global verify2
    global verify3
    global password_verification
    global ques1
    global ques2
    global ques3
    global ans1
    global ans2
    global ans3
    global btnenter3
    verify1 = StringVar()
    verify2 = StringVar()
    verify3 = StringVar()
    password_verification = StringVar()
    ques1 = Label(root,font = ("Arial",12,"bold"), text = "Favorite animal: ", fg = 'orange')
    ques1.place(x=700, y=350)
    ans1 = Entry(root, textvariable=verify1, font=('arial', 15, 'bold'), relief = RIDGE)
    ans1.place(x = 700, y =390)
    ques2 = Label(root,font = ("Arial",12,"bold"), text = "Favorite color: ", fg = 'orange')
    ques2.place(x=700, y=430)
    ans2 = Entry(root, textvariable=verify2,font=('arial', 15, 'bold'), relief = RIDGE)
    ans2.place(x = 700, y =470)
    ques3 = Label(root,font = ("Arial",12,"bold"), text = "Most valuable thing to you: ", fg = 'orange')
    ques3.place(x=700, y=510)
    ans3 = Entry(root, textvariable=verify3,font=('arial', 15, 'bold'), relief = RIDGE)
    ans3.place(x = 700, y =550)
    btnenter3 = Button(root,text="Enter",  font = ("times new roman",12,"bold"),fg="orange", command=checkme2,
                        bg = "white" ,padx = 2, width = 20)
    btnenter3.place(x = 730, y = 600 )

def final():
    new_image = pk.PhotoImage(file="5.png")
    label.config(image=new_image)
    label.image = new_image
    ques1.destroy()
    ques2.destroy()
    ques3.destroy()
    ans1.destroy()
    ans2.destroy()
    ans3.destroy()
    btnenter3.destroy()
    btnenter4 = Button(root,text="Login",  font = ("times new roman",12,"bold"),fg="orange", command= checkme3,
                        bg = "white" ,padx = 2, width = 20)
    btnenter4.place(y = 500, x = 65)

def otp_send():
    try:
        global value
        value = random.randint(100000, 999999)
        Subject="One time password"
        text = " Hi there \n This message is sent from Three level password systems"
        text+="\n"
        text+="This is to inform You that your onr time password is:"
        text+= str(value)
        text+="\n THANK YOU!"
        message = 'Subject: {}\n\n{}'.format(Subject,text)
        context = ssl.create_default_context()
        user_verification = username_verification.get()
        receiver_email = "select email_id from login1 where username = %s"
        cursordb.execute(receiver_email,[(user_verification)])
        results = cursordb.fetchall()
        print(results[0])
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, results[0],message)
    except Exception as e:
        messagebox.showerror("Failed", f"Error sending OTP: {str(e)}")

def checkme():
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    try:
        int(pass_verification)
        sql = "select * from login1 where username = %s and password = %s"
        cursordb.execute(sql,[(user_verification),(pass_verification)])
        results = cursordb.fetchall()
        if results:
            for i in results:
                logged()
                level2()
                break
        else:
            failed()
    except ValueError:
        messagebox.showinfo("Error", "Input Password correctly!")   

def checkme1():
    entry_user2 = entryuser2.get()
    entry_user2 = int(entry_user2)
    # print(entry_user2)
    if value == entry_user2:
        logged()
        level3()
    else:
        failed()

def checkme2():
    user_verification = username_verification.get()
    ans_1 = verify1.get()
    ans_2 = verify2.get()
    ans_3 = verify3.get()
    try:
        sql = "select * from login1 where username = %s and ans1 = %s and ans2 = %s and ans3 = %s"
        cursordb.execute(sql,[(user_verification),(ans_1),(ans_2),(ans_3)])
        results = cursordb.fetchall()
        if results:
            for i in results:
                logged()
                final()
                break
        else:
            failed()
    except ValueError:
        messagebox.showinfo("Error", "Input data correctly!") 

def checkme3():
    logged()
    root.destroy()

def logged():
    global logged_message
    logged_message = Toplevel(root)
    logged_message.title("Welcome")
    logged_message.geometry("500x100")
    Label(logged_message, text="Login Successfully!... Welcome {} ".format(username_verification.get()), fg="green", font="bold").pack()
    Label(logged_message, text="").pack()
    Button(logged_message, text="OK", bg="orange", fg='white', relief="ridge", font=('arial', 12, 'bold'), command=logged_destroy).pack()

def failed():
    global failed_message
    failed_message = Toplevel(root)
    failed_message.title("Invalid Message")
    failed_message.geometry("500x100")
    Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message,text="Ok", bg="orange", fg='white', relief="ridge", font=('arial', 12, 'bold'), command=failed_destroy).pack()
def logged_destroy():
    logged_message.destroy()
def failed_destroy():
    failed_message.destroy()
    level1()
#navigation buttons
def logout():
    root.destroy()

#Creating main page
img = ImageTk.PhotoImage(Image.open("1.png"))
label = Label(root , image = img)
label.pack()
btnsub = pk.Button(root, text="REGISTER",  font = ("times new roman",12,"bold"),fg="orange", command=register,
                    bg = "white" ,padx = 2, width = 20)
btnsub.place(y = 550, x = 280)
btnadd = pk.Button(root, text="LOGIN",  font = ("times new roman",12,"bold"),fg="orange", command=level1,
                    bg = "white" ,padx = 2, width = 20)

btnadd.place(y = 500, x = 280)

root.mainloop()
connectiondb.close()
