import customtkinter
from customtkinter import *
import tkinter as tk
from tkinter import filedialog
import calculate_csv
from calculate_csv import *


#Fonksiyonlar
def calculate():
    cal_page = CTk()
    cal_page.geometry("500x300")

    def choose_pdf():
        file_path = filedialog.askopenfilename(title="Dosya ekle",
                                               filetypes=[("PDF files", 
                                                            "*.pdf")])

    #Butonlar
    pdf_button = CTkButton(master=cal_page, text = "PDF Yükle", font = btn_font, 
                           command = choose_pdf)
    pdf_button.configure(fg_color = "#30cc1f")
    pdf_button.place(relx = 0.5, rely= 0.5, anchor = "center")

    #Labellar
    pdf_label = CTkLabel(master = cal_page, text = "Dosya ekle", font = main_font)
    pdf_label.place(relx = 0.5, rely = 0.15, anchor = "center")

    cal_page.mainloop()


#Pencere
root = CTk()
root.title("Program")
root.geometry("500x300")

#Fontlar
main_font = CTkFont(family="Arial", size = 30)
btn_font = CTkFont(family="Arial", size = 20)

#Labellar
main_label = CTkLabel(master = root, text = "Kitap Metre", font = main_font)
main_label.place(relx = 0.5, rely = 0.15, anchor = "center")


#Switchler
switch_var = customtkinter.StringVar(value= "off")
def switch_event():
    if switch_var.get() == "on":
        set_appearance_mode("dark")
    elif switch_var.get() == "off":
        set_appearance_mode("light")


switch = CTkSwitch(root, text="Açık/Koyu Mod", command=switch_event,variable=switch_var, onvalue="on", offvalue="off", fg_color= "#30cc1f", progress_color= "#30cc1f")
switch.place(relx = 0.05, rely = 0.95, anchor = "sw")



#Butonlar
main_button = CTkButton(master = root, text = "Hesapla", font = btn_font, command = calculate)
main_button.configure(fg_color = "#30cc1f")
main_button.place(relx = 0.5, rely = 0.5, anchor = "center")

root.mainloop()