import customtkinter
from customtkinter import *
import tkinter as tk
from tkinter import filedialog
import predict_result
from predict_result import *


# Fonksiyonlar
def calculate():
    cal_page = CTk()
    cal_page.geometry("500x300")
    cal_page.minsize(400,250)
    cal_page.title("Dosya Seçiniz")

    def choose_pdf():
        file_path = filedialog.askopenfilename(title="Dosya ekle",
                                               filetypes=[("PDF files", "*.pdf")])
        if file_path:
            cal_page.destroy()
            predict_ans(file_path)

    # Butonlar
    pdf_button = CTkButton(master=cal_page, hover_color="#0ceb95",text="PDF Yükle", font=btn_font,
                           command=choose_pdf)
    pdf_button.configure(fg_color="#1fb87d")
    pdf_button.place(relx=0.5, rely=0.5, anchor="center")

    # Labellar
    pdf_label = CTkLabel(master=cal_page, text="Dosya ekle", font=main_font)
    pdf_label.place(relx=0.5, rely=0.15, anchor="center")

    cal_page.mainloop()
info_var = 0
def info_page():
    global info_var
    if info_var == 0:
        info_var = 1
        page = CTk()
        page.geometry("500x400")
        page.minsize(500,400)
        page.title("Bilgilendirme")
        top_label = CTkLabel(master = page, text = "KitapMetre'ye Hoşgeldiniz", font = CTkFont(family="Arial", size=25))
        top_label.place(relx = 0.5, rely = 0.2, anchor = "center")

        label = CTkLabel(master = page, text = "\nBu proje, kullanıcıların sisteme yükledikleri\nTürkçe kitapların PDF dosyalarını analiz ederek\nkitapların uygun yaş aralığı, kitap içerisinde kaç\nuygunsuz cümle ve kelime geçtiği vb. bilgileri\nbelirlemeyi ve bunları kullanıcıya bildirmeyi\namaçlayan bir uygulamadır.", 
                         font = CTkFont(family="Arial", size=20))
        label.place(relx = 0.5, rely = 0.5, anchor = "center")

        last_label = CTkLabel(master = page, text = "Yapımcılar:\nŞuayp Talha Kocabay\nMehmet Kağan Albayrak\nTakım adı: Abra Muhara", font = CTkFont(family="Arial", size=20))
        last_label.place(relx = 0.9, rely = 0.95, anchor = "se")

        def on_close():
            global info_var
            info_var = 0
            page.destroy()
        page.protocol("WM_DELETE_WINDOW", on_close)
        page.mainloop()


# Pencere
root = CTk()
root.title("KitapMetre")
root.geometry("600x400")
root.minsize(600, 400)
set_appearance_mode("dark")
# Fontlar
main_font = CTkFont(family="Arial", size=30)
btn_font = CTkFont(family="Arial", size=20)

# Labellar
main_label = CTkLabel(master=root, text="KitapMetre", font=main_font)
main_label.place(relx=0.5, rely=0.15, anchor="center")


# Switchler
switch_var = customtkinter.StringVar(value="on")


def switch_event():
    if switch_var.get() == "on":
        set_appearance_mode("dark")
    elif switch_var.get() == "off":
        set_appearance_mode("light")


switch = CTkSwitch(root, text="Açık/Koyu Mod", command=switch_event, variable=switch_var,
                   onvalue="on", offvalue="off", fg_color="#1fb87d", progress_color="#1fb87d")
switch.place(relx=0.05, rely=0.95, anchor="sw")

# Butonlar
main_button = CTkButton(master=root, text="Hesapla", hover_color="#0ceb95",font=btn_font, command=calculate)
main_button.configure(fg_color="#1fb87d")
main_button.place(relx=0.5, rely=0.5, anchor="center")

info_button = CTkButton(master = root, text = "?", hover_color="#0ceb95",
                        border_width=2, border_color="#0ceb95", corner_radius=30, 
                        fg_color="transparent", font = CTkFont(family="Arial", size=20), width=20,
                        command=info_page)
info_button.place(relx = 0.95, rely = 0.95, anchor = "se")

root.mainloop()
