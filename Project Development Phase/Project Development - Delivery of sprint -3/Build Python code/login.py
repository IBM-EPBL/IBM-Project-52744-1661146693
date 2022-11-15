from tkinter import *
from tkinter import messagebox
import ast

root=Tk()
root.title('Login Page')
root.geometry('1540x1080')
root.configure(bg='#fff')
root.resizable(True,True)

def signin():
    username=user.get()
    password=code.get()

    file=open('datasheet.txt', 'r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    #print(r.keys())
    #print(r.values())

    if username in r.keys() and password==r[username]:
        screen=Toplevel(root)
        screen.title("Nutrition Assistant")
        screen.geometry('1540x1080')
        screen.config(bg="white")

        Label(screen,text='Welcome to the Nutrition Assistant!',bg='white',font=('Cascadia Mono SemiBold',50,'bold')).pack(expand=True)
        screen.mainloop()

    elif username!='admin' and password!='1234':
         messagebox.showerror("Invalid", "Invalid Credentials")   

    elif username!='admin':
        messagebox.showerror("Invalid", "Invalid UserName") 
    elif password!='1234':
        messagebox.showerror("Invalid", "Invalid PassWord")
    else:
        messagebox.showerror("Invalid", "Invalid Credentials")

#####---------------------------------------------------call sign up page-----------------------------------------------
def signup():
    window=Toplevel(root)

#------------------------------------------------------code of signup.py-------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
    window.title("Registration Page")
    window.geometry('1540x1080')
    window.configure(bg='#fff')
    window.resizable(True,True)

    def signup():
        username=user.get()
        password=code.get()
        confirmpassword=c_code.get()

        if password==confirmpassword:
            try:
                file=open('datasheet.txt', 'r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open('datasheet.txt','w')
                w=file.write(str(r))

                messagebox.showinfo('Sign Up','Successfully Signed up')
                window.destroy()

            except:
                file=open('datasheet.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid','Both Password should match')

    def Login():
        window.destroy()


    img=PhotoImage(file='restaurant.png')
    Label(window,image=img,border=0,bg='white').place(x=50,y=60)

    frame=Frame(window,width=450,height=680,bg='white')
    frame.place(x=970,y=50)

    heading = Label(frame,text="Sign Up", fg="#57a1f8", bg='white', font=('Cascadia Mono SemiBold',30,'bold'))
    heading.place(x=155,y=5)

#------------------------------------------Username------------------------------------------------------------------------

    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'User Name')

    user = Entry(frame,width=28,fg='black',border=0,bg='white',font=('Times New Roman',15))
    user.place (x=88,y=80)
    user.insert(0, 'User Name')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=1,bg='black').place(x=85,y=105)

#-------------------------------------------------------password-----------------------------------------------------------

    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        if code.get()=='':
            code.insert(0,'Password')

    code = Entry(frame,width=28,fg='black',border=0,bg='white',font=('Times New Roman',15))
    code.place (x=88,y=160)
    code.insert(0, 'Password')
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=1,bg='black').place(x=85,y=185)

#-------------------------------------Confirm password----------------------------------------------------------------

    def on_enter(e):
        c_code.delete(0,'end')
    def on_leave(e):
        if c_code.get()=='':
            c_code.insert(0,'Confirm Password')

    c_code = Entry(frame,width=28,fg='black',border=0,bg='white',font=('Times New Roman',15))
    c_code.place (x=88,y=240)
    c_code.insert(0, 'Confirm Password')
    c_code.bind("<FocusIn>", on_enter)
    c_code.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=1,bg='black').place(x=85,y=265)

#-------------------------------------------signin Button-----------------------------------------------------------------------

    Button(frame,width=50,pady=10,text='Sign Up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=60,y=300)
    label=Label(frame,text='I already have an account ?',fg='black',bg='white',font=('Times New Roman',13))
    label.place(x=100,y=360)

    signin=Button(frame,width=5,text='Login',border=0,bg='white',cursor='hand2',fg='#47a1f8',command=Login)
    signin.place(x=290,y=360)



    window.mainloop()
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
img=PhotoImage(file='restaurant.png')
Label(root,image=img,border=0,bg='white').place(x=50,y=60)

frame=Frame(root,width=450,height=680,bg='white')
frame.place(x=970,y=50)

heading = Label(frame,text="Login", fg="#57a1f8", bg='white', font=('Cascadia Mono SemiBold',30,'bold'))
heading.place(x=155,y=5)

#------------------------------------------Username------------------------------------------------------------------------

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    if user.get()=='':
        user.insert(0,'User Name')

user = Entry(frame,width=28,fg='black',border=0,bg='white',font=('Times New Roman',15))
user.place (x=88,y=80)
user.insert(0, 'User Name')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=1,bg='black').place(x=85,y=105)

#-------------------------------------------------------password-----------------------------------------------------------

def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    if code.get()=='':
        code.insert(0,'Password')

code = Entry(frame,width=28,fg='black',border=0,bg='white',font=('Times New Roman',15))
code.place (x=88,y=160)
code.insert(0, 'Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=1,bg='black').place(x=85,y=185)

#-------------------------------------------signin Button-----------------------------------------------------------------------

Button(frame,width=50,pady=10,text=' Login ',bg='#57a1f8',fg='white',border=0, command=signin).place(x=60,y=300)
label=Label(frame,text="Don't have an account ?",fg='black',bg='white',font=('Times New Roman',13))
label.place(x=100,y=360)

signup=Button(frame,width=5,text='Sign Up',border=0,bg='white',cursor='hand2',fg='#47a1f8', command=signup)
signup.place(x=290,y=360)




root.mainloop()