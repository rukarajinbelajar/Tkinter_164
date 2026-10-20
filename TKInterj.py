import tkinter as tk

top = tk.Tk()
top.title("Aplikasi Prediksi Prodi Pilihan")
top.geometry("420x720")
top.configure(bg="#1a2560")

def hasil_prediksi():
    label_hasil.config(text="Prediksi Prodi: Teknologi Informasi")