import tkinter as tk

top = tk.Tk()
top.title("Aplikasi Prediksi Prodi Pilihan")
top.geometry("420x720")
top.configure(bg="#1a2560")

def hasil_prediksi():
    label_hasil.config(text="Prediksi Prodi: Teknologi Informasi")

label_judul = tk.Label(
    top,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 16, "bold"),
    bg="#1a2560",
    fg="white",
)
label_judul.pack(pady=(25, 20))

frame_input = tk.Frame(top, bg="#1a2560")
frame_input.pack()
