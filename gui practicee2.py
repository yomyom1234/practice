from tkinter import *
import tkinter
from tkinter import font
from click import command
from sqlalchemy import column, null 
from tkmacosx import Button
win = Tk()
win.title("계산기")
win.config(bg="#ececec")
win.geometry("245x350")

#연산
if True:
    numList = []
    calList = []
    str_value = tkinter.StringVar()
    if len(numList) == 0:
        numnum = 0
    else :
        numnum = numList[-1]
    str_value.set(str(numnum))
    def plus():
        global numList, calList, numnum
        numList.append(float(ent.get()))
        ent.delete(0, len(str(ent.get)))
        calList.append("+")
    def minus():
        global numList, calList, numnum
        numList.append(float(ent.get()))
        ent.delete(0, len(str(ent.get)))
        calList.append("-")
    def multiply():
        global numList, calList, numnum
        numList.append(float(ent.get()))
        ent.delete(0, len(str(ent.get)))
        calList.append("*")
    def divide():
        global numList, calList, numnum
        numList.append(float(ent.get()))
        ent.delete(0, len(str(ent.get)))
        calList.append("/") 
    def calculate():
        global numList, calList, numnum
        numList.append(float(ent.get()))
        ent.delete(0, len(str(ent.get)))
        numnumcal()
        ent.insert(0, numnum)
    def numnumcal():
        global numList, calList, numnum
        for i in range(len(calList)):
            if calList[i] == "+":
                numList[i+1] += numList[i]
            elif calList[i] == "-":
                numList[i+1] -= numList[i]
            elif calList[i] == "*":
                numList[i+1] *= numList[i]
            elif calList[i] == "/":
                numList[i+1] = numList[i] / numList[i+1]
        numnum = numList[-1]
        return numnum
    def AllClear():
        ent.delete(0, len(ent.get()))
        ent.insert(0,0) 
        global numList, calList, numnum
        numnum = 0 
        numList = []
        calList = []
    def clear(event):
        ent.delete(0, len(ent.get()))
    def insertNum1():
        if ent.get() == "0":
            ent.delete(0, len(ent.get()))
        ent.insert(len(ent.get()),1)
    def insertNum2():
        if ent.get() == "0":
            ent.delete(0, len(ent.get()))
        ent.insert(len(ent.get()),2)
    def insertNum3():
        if ent.get() == "0":
            ent.delete(0, len(ent.get()))
        ent.insert(len(ent.get()),3)
    def insertNum4():
        if ent.get() == "0":
            ent.delete(0, len(ent.get()))
        ent.insert(len(ent.get()),4)
    def insertNum5():
        if ent.get() == "0":
            ent.delete(0, len(ent.get()))
        ent.insert(len(ent.get()),5)
    def insertNum6():
        if ent.get() == "0":
            ent.delete(0, len(ent.get()))
        ent.insert(len(ent.get()),6)
    def insertNum7():
        if ent.get() == "0":
            ent.delete(0, len(ent.get()))
        ent.insert(len(ent.get()),7)
    def insertNum8():
        if ent.get() == "0":
            ent.delete(0, len(ent.get()))
        ent.insert(len(ent.get()),8)
    def insertNum9():
        if ent.get() == "0":
            ent.delete(0, len(ent.get()))
        ent.insert(len(ent.get()),9)
    def insertNum0():
        if ent.get() == "0":
            ent.delete(0, len(ent.get()))
        ent.insert(len(ent.get()),0)
    def insertDot():
        if ent.get() == "0":
            return
        ent.insert(len(ent.get()),".")
    def percent():
        percentNum = float(ent.get())*(0.01)
        ent.delete(0, len(ent.get()))
        ent.insert(len(ent.get()),percentNum)
    def reverse():
        reverseNum = 0 - float(ent.get())
        ent.delete(0, len(ent.get()))
        ent.insert(len(ent.get()),reverseNum)

#입력창
ent = Entry(win)
ent.config(bg="#ececec", fg="#505251", justify="right", font=("Arial", 40), width=8)
ent.config(textvariable=str_value)
ent.bind("<Button-1>", clear)
ent.grid(row = "0", column="0",columnspan=4, sticky="NEWS", ipady=20)

#버튼 생성
BL = []
for i in range(19):
    globals()["btn{}".format(i)] = Button(win)
    BL.append(globals()["btn{}".format(i)])
    BL[i].config(width=60, height=50, font=("Arial", 23))

#버튼 배치
for i in range(len(BL)):
    BL[i].grid(row=i%5+1, column=i%4, sticky="NEWS")
BL[4].grid(columnspan="2")
BL[9].grid(row=5, column=2)
BL[14].grid(row=5, column=3)

#버튼 내용
if True:
    BL[0].config(text = "AC", bg ="#444641" , fg="#e3e3e3")
    BL[1].config(text = "8", bg ="#656660", fg="#e3e3e3")
    BL[2].config(text = "9", bg ="#656660", fg="#e3e3e3")
    BL[3].config(text = "+", bg ="#f2a33c", fg="#e3e3e3",width=65)
    BL[4].config(text = "0", bg ="#656660", fg="#e3e3e3")
    BL[5].config(text = "+/-", bg ="#444641" , fg="#e3e3e3")
    BL[6].config(text = "6", bg ="#656660", fg="#e3e3e3")
    BL[7].config(text = "-", bg ="#f2a33c", fg="#e3e3e3",width=65)
    BL[8].config(text = "1", bg ="#656660", fg="#e3e3e3")
    BL[9].config(text = ".", bg ="#656660", fg="#e3e3e3")
    BL[10].config(text = "%", bg ="#444641" , fg="#e3e3e3")
    BL[11].config(text = "X", bg ="#f2a33c", fg="#e3e3e3",width=65)
    BL[12].config(text = "4", bg ="#656660", fg="#e3e3e3")
    BL[13].config(text = "2", bg ="#656660", fg="#e3e3e3")
    BL[14].config(text = "=", bg ="#f2a33c", fg="#e3e3e3",width=65)
    BL[15].config(text = "÷", bg ="#f2a33c", fg="#e3e3e3",width=65)
    BL[16].config(text = "7", bg ="#656660", fg="#e3e3e3")
    BL[17].config(text = "5", bg ="#656660", fg="#e3e3e3")
    BL[18].config(text = "3", bg ="#656660", fg="#e3e3e3")

#버튼 함수
if True:
    BL[3].config(command=plus)
    BL[7].config(command=minus)
    BL[11].config(command=multiply)
    BL[15].config(command=divide)
    BL[14].config(command=calculate)
    BL[0].config(command=AllClear)
    BL[8].config(command=insertNum1)
    BL[13].config(command=insertNum2)
    BL[18].config(command=insertNum3)
    BL[12].config(command=insertNum4)
    BL[17].config(command=insertNum5)
    BL[6].config(command=insertNum6)
    BL[16].config(command=insertNum7)
    BL[1].config(command=insertNum8)
    BL[2].config(command=insertNum9)
    BL[4].config(command=insertNum0)
    BL[9].config(command=insertDot)
    BL[10].config(command=percent)
    BL[5].config(command=reverse)

#실행 
win.mainloop()