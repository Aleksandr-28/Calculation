from tkinter import *

tk = Tk()
tk.title('Калькулятор')

num = ''

def display(number):
    global num 
    num = num + str(number)
    scr_lbl['text'] = num
    

def clear_scr():
    global num
    num = ''
    scr_lbl['text'] = num


def equal_btn():
     global num
     add=str(eval(num))
     scr_lbl['text'] = add
     num=''
def equal_btn():
     global num
     sub=str(eval(num))
     scr_lbl['text'] = sub
     num=''     
def equal_btn():
     global num
     mul=str(eval(num))
     scr_lbl['text'] = mul
     num=''
def equal_btn():
     global num
     div=str(eval(num))
     scr_lbl['text'] = div
     num=''

def button_press():
     bl_1.configure(bg='white',fg='black')
     bl_2.configure(bg='white',fg='black')
     bl_3.configure(bg='white',fg='black')
     bl_4.configure(bg='white',fg='black')
     bl_5.configure(bg='white',fg='black')
     bl_6.configure(bg='white',fg='black')
     bl_7.configure(bg='white',fg='black')
     bl_8.configure(bg='white',fg='black')
     bl_9.configure(bg='white',fg='black')
     bl_0.configure(bg='white',fg='black')
     bl_sub.configure(bg='white',fg='black')
     bl_mul.configure(bg='white',fg='black')
     bl_clr.configure(bg='white',fg='black')
     bl_res.configure(bg='white',fg='black')
     bl_div.configure(bg='white',fg='black')
     bl_10.configure(bg='white',fg='black')
     bl_11.configure(bg='white',fg='black')
     bl_12.configure(bg='white',fg='black')
     bl_13.configure(bg='white',fg='black')
     bl_add.configure(bg='white',fg='black')
     bl_Light.configure(bg='white',fg='black')
     bl_Dark.configure(bg='white',fg='black')
     bl_Blue.configure(bg='white',fg='black')
     bl_Yellow.configure(bg='white',fg='black')
     scr_lbl.configure(bg='#2E2E2B',fg='white')
     return bl_1

def button_press1():
     bl_1.configure(bg='#2E2E2B',fg='white')
     bl_2.configure(bg='#2E2E2B',fg='white')
     bl_3.configure(bg='#2E2E2B',fg='white')
     bl_4.configure(bg='#2E2E2B',fg='white')
     bl_5.configure(bg='#2E2E2B',fg='white')
     bl_6.configure(bg='#2E2E2B',fg='white')
     bl_7.configure(bg='#2E2E2B',fg='white')
     bl_8.configure(bg='#2E2E2B',fg='white')
     bl_9.configure(bg='#2E2E2B',fg='white')
     bl_0.configure(bg='#2E2E2B',fg='white')
     bl_sub.configure(bg='#2E2E2B',fg='white')
     bl_mul.configure(bg='#2E2E2B',fg='white')
     bl_clr.configure(bg='#2E2E2B',fg='white')
     bl_res.configure(bg='#2E2E2B',fg='white')
     bl_div.configure(bg='#2E2E2B',fg='white')
     bl_10.configure(bg='#2E2E2B',fg='white')
     bl_11.configure(bg='#2E2E2B',fg='white')
     bl_12.configure(bg='#2E2E2B',fg='white')
     bl_13.configure(bg='#2E2E2B',fg='white')
     bl_Light.configure(bg='#2E2E2B',fg='white')
     bl_Dark.configure(bg='#2E2E2B',fg='white')
     bl_Blue.configure(bg='#2E2E2B',fg='white')
     bl_Yellow.configure(bg='#2E2E2B',fg='white')
     bl_add.configure(bg='#2E2E2B',fg='white')
     scr_lbl.configure(bg='black',fg='white')
     return bl_1

def button_press2():
     bl_1.configure(bg='blue',fg='white')
     bl_2.configure(bg='blue',fg='white')
     bl_3.configure(bg='blue',fg='white')
     bl_4.configure(bg='blue',fg='white')
     bl_5.configure(bg='blue',fg='white')
     bl_6.configure(bg='blue',fg='white')
     bl_7.configure(bg='blue',fg='white')
     bl_8.configure(bg='blue',fg='white')
     bl_9.configure(bg='blue',fg='white')
     bl_0.configure(bg='blue',fg='white')
     bl_sub.configure(bg='blue',fg='white')
     bl_mul.configure(bg='blue',fg='white')
     bl_clr.configure(bg='blue',fg='white')
     bl_res.configure(bg='blue',fg='white')
     bl_div.configure(bg='blue',fg='white')
     bl_10.configure(bg='blue',fg='white')
     bl_11.configure(bg='blue',fg='white')
     bl_12.configure(bg='blue',fg='white')
     bl_13.configure(bg='blue',fg='white')
     bl_add.configure(bg='blue',fg='white')
     bl_Light.configure(bg='blue',fg='white')
     bl_Dark.configure(bg='blue',fg='white')
     bl_Blue.configure(bg='blue',fg='white')
     bl_Yellow.configure(bg='blue',fg='white')
     scr_lbl.configure(bg='#00FFFF',fg='black')
     return bl_1

def button_press3():
     bl_1.configure(bg='yellow',fg='black')
     bl_2.configure(bg='yellow',fg='black')
     bl_3.configure(bg='yellow',fg='black')
     bl_4.configure(bg='yellow',fg='black')
     bl_5.configure(bg='yellow',fg='black')
     bl_6.configure(bg='yellow',fg='black')
     bl_7.configure(bg='yellow',fg='black')
     bl_8.configure(bg='yellow',fg='black')
     bl_9.configure(bg='yellow',fg='black')
     bl_0.configure(bg='yellow',fg='black')
     bl_sub.configure(bg='yellow',fg='black')
     bl_mul.configure(bg='yellow',fg='black')
     bl_clr.configure(bg='yellow',fg='black')
     bl_res.configure(bg='yellow',fg='black')
     bl_div.configure(bg='yellow',fg='black')
     bl_10.configure(bg='yellow',fg='black')
     bl_11.configure(bg='yellow',fg='black')
     bl_12.configure(bg='yellow',fg='black')
     bl_13.configure(bg='yellow',fg='black')
     bl_add.configure(bg='yellow',fg='black')
     bl_Light.configure(bg='yellow',fg='black')
     bl_Dark.configure(bg='yellow',fg='black')
     bl_Blue.configure(bg='yellow',fg='black')
     bl_Yellow.configure(bg='yellow',fg='black')
     scr_lbl.configure(bg='#FF7F50',fg='black')
     return bl_1

var = StringVar()

frame_1 = Frame(tk) 
frame_1.pack(expand=True, fill=BOTH)

frame_2 = Frame(tk)
frame_2.pack(expand=True, fill=BOTH)

frame_3 = Frame(tk)
frame_3.pack(expand=True, fill=BOTH)

frame_4 = Frame(tk)
frame_4.pack(expand=True, fill=BOTH)

scr_lbl = Label(
    frame_1,
    textvariable='',
    font=('Times', 20),
    anchor = SE,
    bg = 'black',
    fg = 'white' 
    )

scr_lbl.pack(expand=True, fill=BOTH)

bl_1 = Button(
    frame_1,
    text='1',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(1)
    )

bl_1.pack(expand=True, fill=BOTH, side=LEFT)

bl_2 = Button(
    frame_1,
    text='2',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(2)
    )

bl_2.pack(expand=True, fill=BOTH, side=LEFT)

bl_3 = Button(
    frame_1,
    text='3',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(3)
    )

bl_3.pack(expand=True, fill=BOTH, side=LEFT)

bl_add = Button(
    frame_1,
    text='+',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display('+')
    )

bl_add.pack(expand=True, fill=BOTH, side=LEFT)

bl_4 = Button(
    frame_2,
    text='4',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(4)
    )

bl_4.pack(expand=True, fill=BOTH, side=LEFT)

bl_5 = Button(
    frame_2,
    text='5',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(5)
    )

bl_5.pack(expand=True, fill=BOTH, side=LEFT)

bl_6 = Button(
    frame_2,
    text='6',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(6)
    )

bl_6.pack(expand=True, fill=BOTH, side=LEFT)

bl_sub = Button(
    frame_2,
    text='-',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display('-')
    )

bl_sub.pack(expand=True, fill=BOTH, side=LEFT)

bl_7 = Button(
    frame_3,
    text='7',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(7)
    )

bl_7.pack(expand=True, fill=BOTH, side=LEFT)

bl_8 = Button(
    frame_3,
    text='8',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(8)
    )

bl_8.pack(expand=True, fill=BOTH, side=LEFT)

bl_9 = Button(
    frame_3,
    text='9',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(9)
    )

bl_9.pack(expand=True, fill=BOTH, side=LEFT)

bl_mul = Button(
    frame_3,
    text='*',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display('*')
    )

bl_mul.pack(expand=True, fill=BOTH, side=LEFT)


bl_clr = Button(
    frame_4,
    text='C',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = clear_scr 
    )

bl_clr.pack(expand=True, fill=BOTH, side=LEFT)

bl_0 = Button(
    frame_4,
    text='0',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(0)
    )

bl_0.pack(expand=True, fill=BOTH, side=LEFT)

bl_res = Button(
    frame_4,
    text='=',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = equal_btn
    )

bl_res.pack(expand=True, fill=BOTH, side=LEFT)

bl_div = Button(
    frame_4,
    text='/',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display('/')
    )

bl_div.pack(expand=True, fill=BOTH, side=LEFT)

bl_10 = Button(
    frame_4,
    text='^',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display('**')
    )

bl_10.pack(expand=True, fill=BOTH, side=LEFT)

bl_11 = Button(
    frame_3,
    text='.',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display('.')
    )

bl_11.pack(expand=True, fill=BOTH, side=LEFT)

bl_12 = Button(
    frame_2,
    text='(',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display('(')
    )

bl_12.pack(expand=True, fill=BOTH, side=LEFT)

bl_13 = Button(
    frame_1,
    text=')',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(')')
    )

bl_13.pack(expand=True, fill=BOTH, side=LEFT)

bl_Light = Button(
    frame_1,
    text='Light',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = button_press
    )
    
bl_Light.pack(expand=True, fill=BOTH, side=LEFT)

bl_Dark = Button(
    frame_2,
    text='Dark',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = button_press1
    )

bl_Dark.pack(expand=True, fill=BOTH, side=LEFT)

bl_Blue = Button(
    frame_3,
    text='Blue',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = button_press2
    )


bl_Blue.pack(expand=True, fill=BOTH, side=LEFT)

bl_Yellow = Button(
    frame_4,
    text='Yellow',
    font=('Times', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command =button_press3
    )


bl_Yellow.pack(expand=True, fill=BOTH, side=LEFT)


tk.mainloop()
