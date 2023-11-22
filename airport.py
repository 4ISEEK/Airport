import sqlite3
import datetime
from tkinter import *
from tkinter import messagebox

global db
global sql
global u


# noinspection PyRedeclaration
db = sqlite3.connect('test.db')
# noinspection PyRedeclaration
sql = db.cursor()

sql.execute(f"""CREATE TABLE IF NOT EXISTS users(
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    phone TEXT 
    )""")
db.commit()

sql.execute(f"""CREATE TABLE IF NOT EXISTS tickets(
    login TEXT,
    date TEXT,
    Go TEXT
    )""")
db.commit()
#________________________________________________
root = Tk()
root.title('Airport')
root.geometry('300x300')
#root.resizable(width=False, height=False)
root['bg'] = 'white'

def next1():
    userloginsql = user_login.get()
    userphonesql = user_phone.get()
    userpasswordsql = user_password.get()

    sql.execute(f"SELECT login FROM users WHERE login = '{userloginsql}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES(?, ?, ?)", (userloginsql, userpasswordsql, userphonesql))
        db.commit()
        messagebox.showinfo(title='Airport', message='Added!')
        login_window()
    else:
        messagebox.showerror(title='Airport', message='this account already exists!')
        reg_window()

def singin1():
    global user_login2
    user_login2 = user_login1.get()
    if user_login2 == "admin":
        sql.execute(f'SELECT login FROM users WHERE login = "{user_login2}"')
        if sql.fetchone() is None:
            messagebox.showerror(title='Airport', message='this account not found!')
            login_window()

        else:
            user_password2 = user_password1.get()
            sql.execute(f'SELECT "{user_login2}" FROM users WHERE password  = "{user_password2}"')
            if sql.fetchone() is None:
                messagebox.showerror(title='Airport', message='pass error!')
                login_window()
            else:
                admin()
    else:
        if user_login2 == "":
            messagebox.showerror(title='Airport', message='empty filed login!')
        else:
            sql.execute(f'SELECT login FROM users WHERE login = "{user_login2}"')
            if sql.fetchone() is None:
                messagebox.showerror(title='Airport', message='this account not found!')
                login_window()

            else:
                user_password2 = user_password1.get()
                sql.execute(f'SELECT "{user_login2}" FROM users WHERE password  = "{user_password2}"')
                if sql.fetchone() is None:
                    messagebox.showerror(title='Airport', message='pass error!')
                    login_window()
                else:
                    menu()
def reg1():
    reg_window()
def back1():
    login_window()

def back2():
    menu()
def next2():
    global date

    yy = int(date1_entry.get())
    mm = int(date2_entry.get())
    dd = int(date3_entry.get())
    date = (datetime.date(yy, mm, dd))
    today = datetime.date.today()

    if date < today:
        messagebox.showerror(title='Airport', message='Error "date!')
        date1()

    else:
        pay()
def next3():
    end()
def back3():
    date1()

def end():
    frame = Frame(root, bg='white')
    frame.place(relwidth=1, relheight=1)
    end_label = Label(frame, text='payment was successful!', font='Arial 15 bold', bg='white', fg='black', )
    end2_label = Label(frame, text='good day!', font='Arial 11', bg='white', fg='gray')
    back4_button = Button(frame, text='Back', font='Arial 11', bg='black', fg='white', command=back1)
    #________________
    end_label.pack()
    end2_label.pack()
    back4_button.pack(padx=10, pady=8)
def login_window():
    global user_login1
    global user_password1
    frame = Frame(root, bg='white')
    frame.place(relwidth=1, relheight=1)

    main_label = Label(frame, text='SING IN', font='Arial 15 bold', bg='white', fg='black')

    username_label = Label(frame, text='login', font='Arial 11', bg='white', fg='gray')
    user_login1 = Entry(frame, font='Arial 11', bg='white', fg='black')

    userpassword_label = Label(frame, text='password', font='Arial 11', bg='white', fg='gray')
    user_password1 = Entry(frame, font='Arial 11', bg='white', fg='black')

    singin_button = Button(frame, text='SING IN', font='Arial 11', bg='black', fg='white', command=singin1)

    reg_button = Button(frame, text='REG IN', font='Arial 11', bg='black', fg='white', command=reg1)
    #___________________________________
    main_label.pack()
    username_label.pack()

    user_login1.pack()

    userpassword_label.pack()

    user_password1.pack()

    singin_button.pack(padx=10, pady=8)
    reg_button.pack(padx=10, pady=8)
    frame.mainloop()
    #_______


def reg_window():
    global user_login
    global user_phone
    global user_password

    frame = Frame(root, bg='white')
    frame.place(relwidth=1, relheight=1)

    main_label = Label(frame, text='Creating account', font='Arial 15 bold', bg='white', fg='black')

    username_label = Label(frame, text='login', font='Arial 11', bg='white', fg='gray')
    user_login = Entry(frame, font='Arial 11', bg='white', fg='black')

    usernumber_label = Label(frame, text='number', font='Arial 11', bg='white', fg='gray')
    user_phone = Entry(frame, font='Arial 11', bg='white', fg='black')

    userpassword_label = Label(frame, text='password', font='Arial 11', bg='white', fg='gray')
    user_password = Entry(frame, font='Arial 11', bg='white', fg='black')

    next_button = Button(frame, text='Next', font='Arial 11', bg='black', fg='white', command=next1)
    back_button = Button(frame, text='Back', font='Arial 11', bg='black', fg='white', command=back1)
    #___________________________________
    main_label.pack()
    username_label.pack()
    user_login.pack()
    usernumber_label.pack()
    user_phone.pack()
    userpassword_label.pack()
    user_password.pack()
    next_button.pack(padx=10, pady=8)
    back_button.pack(padx=10, pady=8)
    frame.mainloop()
def menu():
    frame = Frame(root, bg='white')
    frame.place(relwidth=1, relheight=1)
    text_label = Label(frame, text='Select where to:', font='Arial 15 bold', bg='white', fg='black', )

    one_button = Button(frame, text='Tokyo', font='Arial 12', bg='white', fg='black', command=one)

    two_button = Button(frame, text='Moscow', font='Arial 12', bg='white', fg='black', command=two)

    three_button = Button(frame, text='London', font='Arial 12', bg='white', fg='black', command=three)

    four_button = Button(frame, text='Istanbul', font='Arial 12', bg='white', fg='black', command=four)

    back_button = Button(frame, text='Back', font='Arial 11', bg='black', fg='white', command=back1)
    #________________________________________________
    text_label.pack()
    one_button.pack(padx=10, pady=5)
    two_button.pack(padx=10, pady=5)
    three_button.pack(padx=10, pady=5)
    four_button.pack(padx=10, pady=5)
    back_button.pack(padx=10, pady=10)

def one():
    global to
    to = "Tokyo"
    date1()

def two():
    global to
    to = "Moscow"
    date1()

def three():
    global to
    to = "London"
    date1()

def four():
    global to
    to = "Istanbul"
    date1()


def date1():
    global date1_entry
    global date2_entry
    global date3_entry

    frame = Frame(root, bg='white')
    frame.place(relwidth=1, relheight=1)
    text1_label = Label(frame, text='Select date:', font='Arial 15 bold', bg='white', fg='black', )

    year_label = Label(frame, text='year (Ex: "2023")', font='Arial 11', bg='white', fg='gray')
    date1_entry = Entry(frame)
    month_label = Label(frame, text='month (Ex: "11")', font='Arial 11', bg='white', fg='gray')
    date2_entry = Entry(frame)
    day_label = Label(frame, text='day (Ex: "8")', font='Arial 11', bg='white', fg='gray')
    date3_entry = Entry(frame)

    next2_button = Button(frame, text='Next', font='Arial 11', bg='black', fg='white', command=next2)
    back2_button = Button(frame, text='Back', font='Arial 11', bg='black', fg='white', command=back2)

    #________________________________
    text1_label.pack()
    year_label.pack()
    date1_entry.pack()
    month_label.pack()
    date2_entry.pack()
    day_label.pack()
    date3_entry.pack()
    next2_button.pack(padx=10, pady=8)
    back2_button.pack(padx=10, pady=8)


def pay():
    frame = Frame(root, bg='white')
    frame.place(relwidth=1, relheight=1)
    pay1_label = Label(frame, text='Payment', font='Arial 15 bold', bg='white', fg='black', )
    ncard_label = Label(frame, text='number payment card', font='Arial 11', bg='white', fg='gray')
    ncard_entry = Entry(frame)

    cvccard_label = Label(frame, text='CVC', font='Arial 11', bg='white', fg='gray')
    cvccard_entry = Entry(frame)

    next2_button = Button(frame, text='Next', font='Arial 11', bg='black', fg='white', command=next3)
    back2_button = Button(frame, text='Back', font='Arial 11', bg='black', fg='white', command=back3)
    #_____________________________
    pay1_label.pack()
    ncard_label.pack()
    ncard_entry.pack()
    cvccard_label.pack()
    cvccard_entry.pack()
    next2_button.pack(padx=10, pady=8)
    back2_button.pack(padx=10, pady=8)
    sql.execute(f"INSERT INTO tickets VALUES(?, ?, ?)", (user_login2, date, to))
    db.commit()
    mainloop()

def admin():
    frame = Frame(root, bg='white')
    frame.place(relwidth=1, relheight=1)
    admin_label = Label(frame, text='ADMIN', font='Arial 15 bold', bg='white', fg='orange', )
    tickets_btn = Button(frame, text='Tickets', font='Arial 11', bg='black', fg='white', command=tickets)
    users_btn = Button(frame, text='Users', font='Arial 11', bg='black', fg='white', command=users)
    #_______________________
    admin_label.pack()
    tickets_btn.pack(padx=10, pady=8)
    users_btn.pack(padx=10, pady=8)

#def back10():
#   admin()

def tickets():
    frame = Frame(root, bg='white')
    frame.place(relwidth=1, relheight=1)
    for value in sql.execute("SELECT * FROM tickets"):
        label4 = Label(frame, text="Login, date, where to", font='Arial 11', bg='white', fg='gray')
        label5 = Label(frame, text=value, font='Arial 13', bg='white', fg='black')

        #__________
        label4.pack()
        label5.pack()


def users():
    frame = Frame(root, bg='white')
    frame.place(relwidth=1, relheight=1)
    for value in sql.execute("SELECT * FROM users"):
        label2 = Label(frame, text="Login, password, phone number", font='Arial 11', bg='white', fg='gray')
        label3 = Label(frame, text=value, font='Arial 13', bg='white', fg='black')

        # __________
        label2.pack()
        label3.pack()


login_window()
