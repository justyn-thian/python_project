import tkinter as tk
from tkinter import messagebox
windows=tk.Tk()
windows.title("konversi suhu")
windows.geometry("500x500")
def celciustofahrenheit():
    try:
        nilaicelcius=inputcelcius.get()
        nilaicelcius=int(nilaicelcius)
        print (nilaicelcius)
        nilaifahrenheit=(nilaicelcius*9/5)+32
        print (nilaifahrenheit)
        texttampil=str(nilaifahrenheit)+" fahrenheit"
        textkonversifahrenheit.config(text=texttampil)
    except:
        messagebox.showerror("error","mohon masukkan angka bukan teks")
def fahrenheitcelcius():
    try:
        nilaifahrenheit=inputfahrenheit.get()
        nilaifahrenheit=int(nilaifahrenheit)
        print (nilaifahrenheit)
        nilaicelcius=(nilaifahrenheit-32)*5/9
        print (nilaicelcius)
        texttampil2=str(nilaicelcius)+" celcius"
        textkonversicelcius.config(text=texttampil2)
    except:
        messagebox.showerror("error","mohon masukkan angka bukan teks")
judul=tk.Label(windows,text="aplikasi konversi suhu")
judul.grid(row=0,column=0,padx=10,pady=10)
textcelcius=tk.Label(windows,text="mohon masukkan teks celcius")
textcelcius.grid(row=1,column=0,padx=10,pady=10)
inputcelcius=tk.Entry(windows)
inputcelcius.grid(row=2,column=0,padx=10,pady=10)
textkonversifahrenheit=tk.Label(windows,text="hasil konversi")
textkonversifahrenheit.grid(row=3,column=0,padx=10,pady=10)
tombolkonversikefahrenheit=tk.Button(windows,text="hasil dari konversi",command=celciustofahrenheit)
tombolkonversikefahrenheit.grid(row=4,column=0,padx=10,pady=10)
textfahrenheit=tk.Label(windows,text="mohon masukkan suhu pada fahrenheit")
textfahrenheit.grid(row=1,column=1,padx=10,pady=10)
inputfahrenheit=tk.Entry(windows)
inputfahrenheit.grid(row=2,column=1,padx=10,pady=10)
textkonversicelcius=tk.Label(windows,text="hasil konversi")
textkonversicelcius.grid(row=3,column=1,padx=10,pady=10)
tombolkonversi2=tk.Button(windows,text="hasil dari konversi",command=fahrenheitcelcius)
tombolkonversi2.grid(row=4,column=1,padx=10,pady=10)
windows.mainloop()