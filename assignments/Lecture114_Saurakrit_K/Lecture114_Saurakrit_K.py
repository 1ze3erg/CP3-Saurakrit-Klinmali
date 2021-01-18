import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates
from tkcalendar import Calendar
import datetime

cur_rate = CurrencyRates()

# แปลงค่าเงิน
def convert_currency():
    # รับสกุลเงินมาจากการพิมพ์แล้วแปลงเป็นตัวพิมพ์ใหญ่
    cur1_cal = str(cur1_entry.get()).upper()
    cur2_cal = str(cur2_entry.get()).upper()
    date_obj = calendar.selection_get()

    radio_value_get()

    # เช็คว่ามีการใส่าจำนวนเงินที่ช่องไหนและใส่ผลลัพธ์ของการแปลงในอีกช่อง
    if money1_entry.get() != "":
        money_cal = float(money1_entry.get())
        result = cur_rate.convert(cur1_cal, cur2_cal, money_cal, date_obj)
        money2_entry.insert(0, result)
    else:
        money_cal = float(money2_entry.get())
        result = cur_rate.convert(cur2_cal, cur1_cal, money_cal, date_obj)
        money1_entry.insert(0, result)

    grab_date()


# รับค่าจาก radio button
def radio_value_get():
    if var.get() == 1:
        money1_entry.delete(0, 'end')
    elif var.get() == 2:
        money2_entry.delete(0, 'end')
    else:
        money1_entry.delete(0, 'end')
        money2_entry.delete(0, 'end')


# clear ช่องที่ใส่ค่าเงิน
def clear_money():
    money1_entry.delete(0, 'end')
    money2_entry.delete(0, 'end')


# แสดงวันที่
def grab_date():
    if calendar.selection_get() != None:
        calendar_label.config(text=calendar.selection_get())
    else:
        calendar_label.config(text=datetime.date.today())


# clear วันที่
def clear_date():
    calendar.selection_clear()
    calendar_label.configure(text="")


main_windows = tk.Tk()
main_windows.title("โปรแกรมแปลงค่าเงิน")
main_windows.geometry('300x700')


# money1
money1_label = tk.Label(main_windows, text="money1")
money1_label.pack(expand=True)
money1_entry = tk.Entry(main_windows)
money1_entry.pack(expand=True)


# สกุลเงิน1
cur1_label = tk.Label(main_windows, text="currency1")
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


# ให้เลือกว่าจะแปลงขึ้นหรือลง
var = tk.IntVar()
filename1 = tk.PhotoImage(file='arrow-up.png').subsample(x=70, y=70)
filename2 = tk.PhotoImage(file='arrow-down.png').subsample(x=70, y=70)
R1 = tk.Radiobutton(main_windows, variable=var, value=1, image=filename1)
R1.pack()
R2 = tk.Radiobutton(main_windows, variable=var, value=2, image=filename2)
R2.pack()


# money2
money2_label = tk.Label(main_windows, text="money2")
money2_label.pack(expand=True)
money2_entry = tk.Entry(main_windows)
money2_entry.pack(expand=True)


# สกุลเงิน2
cur2_label = tk.Label(main_windows, text="currency2")
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
convert_button = tk.Button(main_windows, text="แปลงค่าเงิน",
                        width=20, bg="grey", command=convert_currency)
convert_button.pack(fill=tk.Y, expand=True)


# ปุ่ม clear จำนวนเงิน
clear_button = tk.Button(main_windows, text="clear money",
                      width=20, bg="red", command=clear_money)
clear_button.pack(fill=tk.Y, expand=True, pady=5)

# ช่องแสดงวันที่และปุ่มclearวันที่
calendar_date_pattern = tk.Label(main_windows, text="Date(y-mm-dd)", bg='cyan')
calendar_date_pattern.pack(fill='both', expand=True)
calendar_label = tk.Label(main_windows, text="", bg='cyan')
calendar_label.pack(fill=tk.Y, expand=True)
calendar_clear_date = tk.Button(
    main_windows, text="Clear Date", command=clear_date)
calendar_clear_date.pack(expand=True, pady=5)

# ช่อง calendar หลัก
mindate = datetime.date(year=1999, month=1, day=10)
maxdate = datetime.date.today()
calendar = Calendar(main_windows, selectmode="day", date_pattern='y-mm-dd',
                    firstweekday='sunday', disableddaybackground='grey', cursor="hand2",
                    mindate=mindate, maxdate=maxdate)
calendar.pack(side='right', expand=True, pady=5)

main_windows.mainloop()
