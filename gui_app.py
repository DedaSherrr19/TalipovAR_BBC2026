import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
window=tk.Tk()
window.geometry("250x250")
window.title("Перевод длин")
frame=ttk.Frame(window)
frame.grid()


ttk.Label(frame,text="Длина").grid()

length=tk.Entry(frame, bg="#e3f2fd", fg="black")
length.grid()

ttk.Label(text="Перевод").grid()

direction=ttk.Combobox(frame,values=("м -> см","см -> м"),state="readonly")
direction.grid()

result=tk.StringVar(value="Результат")

def convert():
    try:
        value=float(length.get().strip().replace(", ","."))
        # raise ValueError
    except ValueError:
        result.set("Результат:")
        messagebox.showerror("Ошибка","Введите числовое значение")
        return
    if direction.current()==0:
        converted=value*100
    else:
        converted=value/100
    result.set(converted)
buttons=ttk.Frame(frame)
buttons.grid()
ttk.Button(buttons, text="Перевести",command=convert).grid()
ttk.Label(frame, textvariable=result).grid()



window.mainloop()