from tkinter import *
from tkinter import ttk
from forex_python.converter import *
import tkinter as tk

cur_rate = CurrencyRates()


def convert_currency(event):
    # รับสกุลเงินมาจากการพิมพ์แล้วแปลงเป็นตัวพิมพ์ใหญ่
    cur1_cal = str(cur1_entry.get()).upper()
    cur2_cal = str(cur2_entry.get()).upper()

    # เช็คว่ามีการใส่าจำนวนเงินที่ช่องไหนและใส่ผลลัพธ์ของการแปลงในอีกช่อง
    if money1_entry.get() != "":
        money_cal = float(money1_entry.get())
        result = cur_rate.convert(cur1_cal, cur2_cal, money_cal)
        money2_entry.insert(0, result)
    else:
        money_cal = float(money2_entry.get())
        result = cur_rate.convert(cur2_cal, cur1_cal, money_cal)
        money1_entry.insert(0, result)


def clear_money(event):
    money1_entry.delete(0, 'end')
    money2_entry.delete(0, 'end')


main_windows = tk.Tk()
main_windows.title("โปรแกรมแปลงค่าเงิน")
main_windows.geometry('300x500')


# money1
money1_label = Label(main_windows, text="money1")
money1_label.pack(expand=True)
money1_entry = Entry(main_windows)
money1_entry.pack(expand=True)


# สกุลเงิน1
cur1_label = Label(main_windows, text="currency1")
cur1_label.pack(expand=True)
cur1_entry = ttk.Combobox(main_windows,
                          values=['AUD',
                                  'BGN',
                                  'BRL',
                                  'CAD',
                                  'CHF',
                                  'CNY',
                                  'CZK',
                                  'DKK',
                                  'EUR',
                                  'GBP',
                                  'HKD',
                                  'HRK',
                                  'HUF',
                                  'IDR',
                                  'ILS',
                                  'INR',
                                  'ISK',
                                  'JPY',
                                  'KRW',
                                  'MXN',
                                  'MYR',
                                  'NOK',
                                  'NZD',
                                  'PHP',
                                  'PLN',
                                  'RON',
                                  'RUB',
                                  'SEK',
                                  'SGD',
                                  'THB',
                                  'TRY',
                                  'USD',
                                  'ZAR'])
cur1_entry.pack(expand=True)


# ลูกศรขึ้นลงเป็นสัญลักษณ์เพื่อแสดงว่าสามารถแปลงค่าเงินไปมาได้
filename = PhotoImage(file="sorting-arrows.png").subsample(x=10, y=10)
arrow = Label(main_windows, image=filename)
arrow.pack(expand=True)


# money2
money2_label = Label(main_windows, text="money2")
money2_label.pack(expand=True)
money2_entry = Entry(main_windows)
money2_entry.pack(expand=True)


# สกุลเงิน2
cur2_label = Label(main_windows, text="currency2")
cur2_label.pack(expand=True)
cur2_entry = ttk.Combobox(main_windows,
                          values=['AUD',
                                  'BGN',
                                  'BRL',
                                  'CAD',
                                  'CHF',
                                  'CNY',
                                  'CZK',
                                  'DKK',
                                  'EUR',
                                  'GBP',
                                  'HKD',
                                  'HRK',
                                  'HUF',
                                  'IDR',
                                  'ILS',
                                  'INR',
                                  'ISK',
                                  'JPY',
                                  'KRW',
                                  'MXN',
                                  'MYR',
                                  'NOK',
                                  'NZD',
                                  'PHP',
                                  'PLN',
                                  'RON',
                                  'RUB',
                                  'SEK',
                                  'SGD',
                                  'THB',
                                  'TRY',
                                  'USD',
                                  'ZAR'])
cur2_entry.pack(expand=True)


# ปุ่มคำนวณ
convert_button = Button(main_windows, text="แปลงค่าเงิน", width=20, bg="grey")
convert_button.bind('<Button-1>', convert_currency)
convert_button.pack(fill=tk.Y, expand=True)


# ปุ่ม clear จำนวนเงิน
clear_button = Button(main_windows, text="clear money", width=20, bg="red")
clear_button.bind('<Button-1>', clear_money)
clear_button.pack(fill=tk.Y, expand=True)


main_windows.mainloop()
