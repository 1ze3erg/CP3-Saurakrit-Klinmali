from tkinter import *
import math

#ฟังก์ชันคำนวณค่า BMI
def leftClickButton(event):
    weight = float(textBoxWeight.get())
    height = float(textBoxHeight.get())
    result = weight/math.pow((height/100),2)
    lebelResult.configure(text=result)
    BMI_Meaning(result)

#ฟังก์ชันเทียบค่า BMI
def BMI_Meaning(x):
    if x >= 30:
        lebelBMI_Meaning.configure(text="อ้วนมาก")
    elif x >= 25 and x < 30:
        lebelBMI_Meaning.configure(text="อ้วน")
    elif x >= 23 and x < 25:
        lebelBMI_Meaning.configure(text="น้ำหนักเกิน")
    elif x > 18.5 and x < 23:
        lebelBMI_Meaning.configure(text="น้ำหนักปกติ เหมาะสม")
    else:
        lebelBMI_Meaning.configure(text="ผอมเกินไป")

MainWindow = Tk()

#ช่องรับค่าส่วนสูง
lebelHeight = Label(MainWindow,text="ส่วนสูง (cm)")
lebelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

#ช่องรับค่าน้ำหนัก
lebelWeight = Label(MainWindow,text="น้ำหนัก (kg)")
lebelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

#ปุ่มคำนวณ
calculateButton = Button(MainWindow,text="คำนวณ",width=20,bg="grey")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=1)

#แสดงค่า BMI
lebelBMI = Label(MainWindow,text="BMI",bg="yellow")
lebelBMI.grid(row=3,column=0)
lebelResult = Label(MainWindow,text="ผลลัพธ์")
lebelResult.grid(row=3,column=1)
lebelBMI_Meaning = Label(MainWindow,text="ความหมายค่า BMI",bg="yellow")
lebelBMI_Meaning.grid(row=4,column=1)

MainWindow.mainloop()