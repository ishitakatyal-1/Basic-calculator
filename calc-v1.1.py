# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 17:49:21 2019

@author: Ishita
"""
x = 0

def add_one():
    if(x == 0):
            entry1.insert(0, "1")
    elif(x == 1):
        entry2.insert(0, "1")
        
def add_two():
    if(x == 0):
        entry1.insert(0, "2")
    elif(x == 1):
        entry2.insert(0, "2")
    
def add_three():
    if(x == 0):
        entry1.insert(0, "3")
    elif(x == 1):
        entry2.insert(0, "3")
    
def add_four():
    if(x == 0):
        entry1.insert(0, "4")
    elif(x == 1):
        entry2.insert(0, "4")
    
def add_five():
    if(x == 0):
        entry1.insert(0, "5")
    elif(x == 1):
        entry2.insert(0, "5")
    
def add_six():
    if(x == 0):
        entry1.insert(0, "6")
    elif(x == 1):
        entry2.insert(0, "6")
    
def add_seven():
    if(x == 0):
        entry1.insert(0, "7")
    elif(x == 1):
        entry2.insert(0, "7")
    
def add_eight():
    if(x == 0):
        entry1.insert(0, "8")
    elif(x == 1):
        entry2.insert(0, "8")
    
def add_nine():
    if(x == 0):
        entry1.insert(0, "9")
    elif(x == 1):
        entry2.insert(0, "9")
    
def add_zero():
    if(x == 0):
        entry1.insert(0, "0")
    elif(x == 1):
        entry2.insert(0, "0")
    
def add_neg():
    if(x == 0):
        entry1.insert(0, "-")
    elif(x == 1):
        entry2.insert(0, "-")
    
def add_decimal():
    if(x == 0):
        entry1.insert(0, ".")
    elif(x == 1):
        entry2.insert(0, ".")
    
def next_num():
    global x
    x = 1
    
def add_num():
    result["text"] = ""
    num1 = entry1.get()
    num2 = entry2.get()
    output = float(num1) + float(num2)
    result["text"] = str(output)
    
def subtract_num():
    result["text"] = ""
    num1 = entry1.get()
    num2 = entry2.get()
    output = float(num1) - float(num2)
    ans = round(output, 4)
    result["text"] = str(ans)    

def mult_num():
    result["text"] = ""
    num1 = entry1.get()
    num2 = entry2.get()
    output = float(num1) * float(num2)
    result["text"] = str(output)
    
def quot_num():
    result["text"] = ""
    num1 = (entry1.get())
    num2 = (entry2.get())
    if(num2 == 0):
        print("Division by 0 is anot allowed.")
    else:
        output = float(num1) / float(num2)
        ans = round(output, 4)
        result["text"] = str(ans)
        
def reciprocal():
    result["text"] =""
    num1 = entry1.get()
    output = float(1)/float(num1)
    ans = round(output, 4)
    result["text"] = str(ans)
    
def power():
    result["text"] = ""
    num1 = entry1.get()
    num2 = entry2.get()
    output = math.pow(float(num1), float(num2))
    ans = round(output, 4)
    result["text"] = str(ans)
    
def clear_nums():
    entry1.delete(0, "end")
    entry2.delete(0, "end")
    result["text"] = ""
    global x
    x = 0
    
import tkinter as tk
import math
from tkinter import *

calc = tk.Tk()
calc.title("Basic Calculator")
calc.geometry("300x600")
calc.config(background="white")

mainframe1 = tk.Frame(calc)
mainframe1.pack()

label00 = tk.Label(mainframe1, background="white", text="BASIC CALCULATOR", font="Times 20")
entry1 = tk.Entry(mainframe1, width=3, background="white", font="Times 20")
entry1.insert("end", " ")
entry1.configure(justify="right")
entry2 = tk.Entry(mainframe1, width=3, background="white", font="TImes 20")
entry2.insert("end", " ")
entry2.configure(justify="right")
result = tk.Label(mainframe1, width=3, font="Times 20")


button1 = tk.Button(mainframe1, height=2, width=4, background="white", text="1", font="Times 20", command=add_one)
button2 = tk.Button(mainframe1, height=2, width=4, background="white", text="2", font="Times 20", command=add_two)
button3 = tk.Button(mainframe1, height=2, width=4, background="white", text="3", font="Times 20", command=add_three)
button4 = tk.Button(mainframe1, height=2, width=4, background="white", text="4", font="Times 20", command=add_four)
button5 = tk.Button(mainframe1, height=2, width=4, background="white", text="5", font="Times 20", command=add_five)
button6 = tk.Button(mainframe1, height=2, width=4, background="white", text="6", font="Times 20", command=add_six)
button7 = tk.Button(mainframe1, height=2, width=4, background="white", text="7", font="Times 20", command=add_seven)
button8 = tk.Button(mainframe1, height=2, width=4, background="white", text="8", font="Times 20", command=add_eight)
button9 = tk.Button(mainframe1, height=2, width=4, background="white", text="9", font="Times 20", command=add_nine)
#button_neg = tk.Button(mainframe1, height=2, width=4, background="white", text="-", font="Times 20", command=add_minusSign)
button0 = tk.Button(mainframe1, height=2, width=4, background="white", text="0", font="Times 20", command=add_zero)
button_dec = tk.Button(mainframe1, height=2, width=4, background="white", text=".", font="Times 20", command=add_decimal)
button_next = tk.Button(mainframe1, height=2, width=4, background="white", text="Next", font="Times 20", command=next_num)

button_clear = tk.Button(mainframe1, height=1, width=4, background="white", text="Clear", font="Times 20", command=clear_nums)
button_rec = tk.Button(mainframe1, height=1, width=4, background="white", text="1/x", font="Times 20", command=reciprocal)
button_pow = tk.Button(mainframe1, height=1, width=4, background="white", text="power", font="Times 20", command=power)
button_close = tk.Button(mainframe1, height=1, width=4, background="white", text="Close", font="Times 20", command=calc.destroy)

button_add = tk.Button(mainframe1, height=2, width=4, background="white", text="+", font="Times 20", command=lambda:add_num())
button_sub = tk.Button(mainframe1, height=2, width=4, background="white", text="-", font="Times 20", command=lambda:subtract_num())
button_mult = tk.Button(mainframe1, height=2, width=4, background="white", text="x", font="Times 20", command=lambda:mult_num())
button_quot = tk.Button(mainframe1, height=2, width=4, background="white", text="/", font="Times 20", command=lambda:quot_num())

label0 = tk.Label(mainframe1, text="Copyright\n@Myra-IK")


label00.grid(row=0, column=0, columnspan=4, sticky=tk.EW, pady=4)

entry1.grid(row=1, column=0, sticky=tk.EW, pady=5)
entry2.grid(row=1, column=1, sticky=tk.EW, pady=5)
result.grid(row=1, column=2, columnspan=2, sticky=tk.EW, pady=5)

button1.grid(row=2, column=0, sticky=tk.W, pady=4)
button2.grid(row=2, column=1, sticky=tk.W, pady=4)
button3.grid(row=2, column=2, sticky=tk.W, pady=4)
button_add.grid(row=2, column=3, sticky=tk.W, pady=4)

button4.grid(row=3, column=0, sticky=tk.W, pady=4)
button5.grid(row=3, column=1, sticky=tk.W, pady=4)
button6.grid(row=3, column=2, sticky=tk.W, pady=4)
button_sub.grid(row=3, column=3, sticky=tk.W, pady=4)

button7.grid(row=4, column=0, sticky=tk.W, pady=4)
button8.grid(row=4, column=1, sticky=tk.W, pady=4)
button9.grid(row=4, column=2, sticky=tk.W, pady=4)
button_mult.grid(row=4, column=3, sticky=tk.W, pady=4)

#button_neg.grid(row=5, column=0, sticky=tk.W, pady=4)
button_next.grid(row=5, column=0, sticky=tk.W, pady=4)

button0.grid(row=5, column=1, sticky=tk.W, pady=4)
button_dec.grid(row=5, column=2, sticky=tk.W, pady=4)
button_quot.grid(row=5, column=3, sticky=tk.W, pady=4)
button_clear.grid(row=6, column=0, sticky=tk.W, pady=4)
button_rec.grid(row=6, column=1, sticky=tk.W, pady=4)
button_pow.grid(row=6, column=2, sticky=tk.W, pady=4)
button_close.grid(row=6, column=3, sticky=tk.W, pady=4)
label0.grid(row=7, column=0, sticky=tk.W, pady=5)

calc.mainloop()
