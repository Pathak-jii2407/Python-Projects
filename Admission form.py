import tkinter as tk
import pandas as pd
from tkinter import messagebox
import datetime
import random
import os
from tkinter import PhotoImage, Entry, Button, Label
from PIL import Image, ImageTk
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


folder_path = "C:\\student_profile"
try:
    os.makedirs(folder_path)
except OSError as e:
     print(e)
    
def check_again():

    result_window = tk.Tk()
    result_window.title("Result")
    result_window.geometry('400x400')

    progress_label = tk.Label(root, text="")
    progress_label.pack()
    result_label = tk.Label(result_window, text=f"Name: {name.get()}",font=("Helvetica", 15))
    result_label.pack()
    result_label = tk.Label(result_window, text=f"Fund : {age.get()}",font=("Helvetica", 15))
    result_label.pack()   
    result_label = tk.Label(result_window, text=f"Branch : {cource.get()}",font=("Helvetica", 15))
    result_label.pack()
    result_label = tk.Label(result_window, text=f"DOB : {DoB.get()}",font=("Helvetica", 15))
    result_label.pack()
    result_label = tk.Label(result_window, text=f"Address : {address.get()}",font=("Helvetica", 15))
    result_label.pack()
    result_label = tk.Label(result_window, text=f"Contact Number: {phone.get()}",font=("Helvetica", 15))
    result_label.pack() 
    result_label = tk.Label(result_window, text=f"E-Mail ID : {email.get()}",font=("Helvetica", 15))    
    result_label.pack()
    result_label = tk.Label(result_window, text=f"password : {password}",font=("Helvetica",20))
    result_label.pack()

    _button= tk.Button(result_window, text="Process",command=get_input)
    _button.pack()

    result_label = tk.Label(result_window)    
    result_label.pack()
    cancel_button= tk.Button(result_window, text="Cancel",command=main)
    cancel_button.pack()
    result_window.mainloop()

def CSV():
    try:

        display_window = tk.Toplevel(root)
        display_window.title("Student Data")
        df=pd.read_csv(f"C:\\student_profile\\{entry_otp.get()}.csv")
        text_widget = tk.Text(display_window, wrap=tk.WORD)
        text_widget.pack()
        text_widget.insert(tk.END, df.to_string(index=False))
        display_window.mainloop()

    except FileNotFoundError:
        messagebox.showerror("Error","File Not Found in C drive\nCreate a folder name:`student_profile`")
        


def get_input():
    try:
        tk.Label(root,text=f'name:{name}')
        tk.Label(root,text=f'gender:{gender}')
        tk.Label(root,text=f'Fund:{age}')
        tk.Label(root,text=f'cource:{cource}')
        tk.Label(root,text=f'DoB:{DoB}')
        tk.Label(root,text=f'address:{address}')
        tk.Label(root,text=f'phone:{phone}')
        tk.Label(root,text=f'email:{email}')

    except Exception as e:
        messagebox.showerror('Error', f'Error: {e}')
    try:
        dff=pd.DataFrame()
        df = pd.DataFrame({'date':[datetime.date.today()],'name':[name.get()],'gender':[gender.get()],'Fund':[age.get()],'cource':[cource.get()],
                        'address':[address.get()],'phone':[phone.get()],'email':[email.get()]})
        
        dff=pd.concat([dff,df])
        file_name = f'{password}.csv'
        df.to_csv(f'C:\\student_profile\\{file_name}', index=False)
        messagebox.showinfo('Success', "you have successfully submitted\nThanks for submitting")
        gmail_user = "Your_email"   #Enter your email & password.
        gmail_password = 'Your_pass' 

        to_email = f'{email.get()}'  

        msg = MIMEMultipart()
        msg["From"] = gmail_user
        msg["To"] = to_email
        msg["Subject"] = "An OTP Message for FEST Investment"  

        body = f"{password} is your OTP password.\nKeep it safe and Private.\n you Fund of {age.get()} rupees.Thank you '{name.get()}'\n\n\nDiscription:-\nHello students, Wishing you a Happy Engineer Day with laughter , love , and unfforgotable momenyts.\nInvestment:-\nInvesting is an effective way to put your money to work and potentiallybuild wealth\n\n\nLove from Jawaharlal Nehru College of Technology"
        msg.attach(MIMEText(body, "plain"))


        smtp_server = "smtp.gmail.com"
        smtp_port = 587  

        try:
            msg.as_string()
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user, to_email, msg.as_string())
            server.quit()
            messagebox.showinfo("Success", f"OTP has been sent to {to_email} email")
        except Exception as e:
            print(f"Error: {str(e)}")
            messagebox.showerror("Error",f"Error: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error","File Not Found in C drive\nCreate a folder name:`student_profile`")


root = tk.Tk()
root.title("Admission Counter")
root.geometry('900x900')
label_options = {
    "text": "Enter, OTP!",
    "font": ("Arial", 8),
    "bg": "lightblue",
    "fg": "black",
}

button_options = {
    "text": "Click Me",
    "font": ("Arial", 8),
    "bg": "lightblue",
    "fg": "black",
}

def main():
    label_n=tk.Label(root,text="Name:")
    label_n.pack()
    global name
    name = tk.Entry(root,width=40,highlightthickness=1,highlightbackground='white',highlightcolor='blue',)
    name.pack()

    label_g=tk.Label(root,text="Gender:")
    label_g.pack()
    global gender
    gender = tk.Entry(root,width=40,highlightthickness=1,highlightbackground='blue',highlightcolor='white')
    gender.pack()

    global age
    label_n=tk.Label(root,text="Fund:")
    label_n.pack()
    age = tk.Entry(root,width=40,highlightthickness=1,highlightbackground='blue',highlightcolor='white')
    age.pack()
    label_n=tk.Label(root,text="Cource:")
    label_n.pack()
    global cource
    cource = tk.Entry(root,width=40,highlightthickness=1,highlightbackground='blue',highlightcolor='white')
    cource.pack()

    label_n=tk.Label(root,text="Date of Birth :")
    label_n.pack()
    global DoB
    DoB = tk.Entry(root,width=40,highlightthickness=1,highlightbackground='blue',highlightcolor='white')
    DoB.pack()

    label_n=tk.Label(root,text="Address :")
    label_n.pack()
    global address
    address = tk.Entry(root,width=40,highlightthickness=1,highlightbackground='blue',highlightcolor='white')
    address.pack()

    label_n=tk.Label(root,text="Contact Number :")
    label_n.pack()
    global phone
    phone = tk.Entry(root,width=40,highlightthickness=1,highlightbackground='blue',highlightcolor='white')
    phone.pack()

    label_n=tk.Label(root,text="E-Mail :")
    label_n.pack()
    global email
    email = tk.Entry(root,width=40,highlightthickness=1,highlightbackground='blue',highlightcolor='white')
    email.pack()

    pass_start=2023
    pass_end=200
    pass_end_2=900
    global password_rand
    password_rand = random.randint(pass_end, pass_end_2)
    global pass_rand
    pass_rand=random.randint(pass_start,3023)
    global password
    password = f'{pass_rand}{cource.get()}{password_rand}'
    button = tk.Button(root, text="Submit", command=check_again)
    button.pack()

    label_n=tk.Label(root,text="Enter OTP :",cnf=label_options)
    label_n.pack(side='left')
    global entry_otp
    entry_otp=tk.Entry(root)
    entry_otp.pack(side='left')
    button=tk.Button(root,text='Submit',cnf=button_options,command=CSV)
    button.pack(side='left')

    result_label = tk.Label(root, text=" ")
    result_label.pack()
    result_label.destroy()




main()
root.mainloop()

