import tkinter as tk
from PIL import ImageTk
import pandas as pd
from tkinter import messagebox

class App:
    def __init__(self):
        window.title('My first Tk_project')
        window.geometry('800x600')
        window.resizable(0,0)   # 阻止窗口的大小调整
        window.mainloop()

window = tk.Tk()
canvas = tk.Canvas(window,height=250, width=1000)
image_file = ImageTk.PhotoImage(file='./9.jpg')
image = canvas.create_image(0,0,anchor='center',image=image_file)
tk.Label(canvas,text='本产品仅供学习使用',).place(x=650,y=0)
canvas.pack(side='top')

canvas2 = tk.Canvas(window,height=320,width=250)
image_file2 = ImageTk.PhotoImage(file='lufei4.jpg')
image2 = canvas2.create_image(0,0,anchor='nw',image=image_file2)
canvas2.place(x=570,y=300)

tk.Label(window,text='欢迎来到老汪的信息系统 !',font=('华文行楷',20),width=30).place(x=210,y=220)
tk.Label(window,text='账户',font=('黑体',15)).place(x=190,y=300)
tk.Label(window,text='密码',font=('黑体',15)).place(x=190,y=350)

var1 = tk.StringVar()
var2 = tk.StringVar()
reg_var1 = tk.StringVar()
reg_var2 = tk.StringVar()
reg_var3 = tk.StringVar()
e1 = tk.Entry(window,width=30,textvariable=var1).place(x=270,y=300)
e2 = tk.Entry(window,width=30,textvariable=var2,show='*').place(x=270,y=350)

def log_in():    # 用户登录验证
    name = var1.get()
    password= var2.get()
    file = pd.read_excel('registered.xlsx')
    data = pd.DataFrame(file)
    registered_name = data['账户']
    if name in registered_name.values:
        if password==str(data[registered_name==name]['密码'].values.tolist()[0]):
            messagebox.showinfo(title='success',message='登录成功 !')
        else:
            messagebox.showerror(title='error',message='密码错误！')
    else:
        messagebox.showerror(title='error',message='没有此账户，请注册！')

def confirmit():    # 确认两次密码是否一致，如果一致将注册信息写入Excel
    if reg_var2.get()==reg_var3.get():
        name = reg_var1.get()
        pw = reg_var2.get()
        data = pd.DataFrame({'账户':[name],'密码':[pw]})
        file = pd.read_excel('registered.xlsx')
        file = file.append(data,ignore_index=True)
        file.to_excel('registered.xlsx',index=False)
        messagebox.showinfo(title='register',message='注册成功！')
    else:
        messagebox.showerror(title='error',message='两次密码不一致！')

def register_():    # 用户注册
    window_reg = tk.Toplevel(window)    # 窗口上的窗口
    window_reg.geometry('500x300')
    window_reg.title('注册')

    name_label = tk.Label(window_reg,text='账户',font=('黑体',12)).place(x=100,y=30)
    name_entry = tk.Entry(window_reg,textvariable=reg_var1).place(x=190,y=30)
    pw_label = tk.Label(window_reg,text='密码',font=('黑体',12)).place(x=100,y=90)
    pw_entry = tk.Entry(window_reg,textvariable=reg_var2).place(x=190,y=90)
    con_pw_label = tk.Label(window_reg,text='确认密码',font=('黑体',12)).place(x=100,y=150)
    con_pw = tk.Entry(window_reg,textvariable=reg_var3,show='*').place(x=190,y=150)
    confirm = tk.Button(window_reg,text='确定',width=10,command=confirmit).place(x=200,y=190)


login = tk.Button(window,text='Log in',activebackground='red',command=log_in).place(x=270,y=400)
register = tk.Button(window,text='Register',activebackground='red',command=register_).place(x=390,y=400)
App()

