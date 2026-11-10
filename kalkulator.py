import tkinter as tk
window=tk.Tk()
window.geometry("500x500")
window.title("kalkulator")
print("1237")
def hitungkalkulator():
    print("123")
    angka1=input1.get()
    angka2=input2.get()
    angka1=int(angka1)
    angka2=int(angka2)
    operasi=input3.get()
    print (angka1)
    print (angka2)
    print (operasi)
    if operasi=="+":
        hasil=angka1+angka2
        print(hasil)
    elif operasi=="-":
        hasil2=angka1-angka2
        print(hasil2)
    elif operasi=="*":
        hasil3=angka1*angka2
        print(hasil3)
    elif operasi=="/":
        hasil4=angka1/angka2
        print(hasil4)
judul=tk.Label(window,text="aplikasi kalkulator")
judul.grid(row=0,column=0,padx=10,pady=10)
text1=tk.Label(window,text="mohon masukkan angka pertama")
text1.grid(row=1,column=0,padx=10,pady=10)
input1=tk.Entry(window)
input1.grid(row=1,column=1,padx=10,pady=10)
text2=tk.Label(window,text="mohon masukkan angka kedua")
text2.grid(row=2,column=0,padx=10,pady=10)
input2=tk.Entry(window)
input2.grid(row=2,column=1,padx=10,pady=10)
text3=tk.Label(window,text="mohon masukkan operasi dari kalkulator")
text3.grid(row=3,column=0,padx=10,pady=10)
input3=tk.Entry(window)
input3.grid(row=3,column=1,padx=10,pady=10)
tombolhitung=tk.Button(window,text="hitung kalkulator",command=hitungkalkulator)
tombolhitung.grid(row=4,column=0,padx=10,pady=10)
text4=tk.Label(window,text="hasil kalkulasi")
text4.grid(row=4,column=1,padx=10,pady=10)
window.mainloop()
