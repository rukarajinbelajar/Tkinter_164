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

entries = []
for i in range(10):
    lbl = tk.Label(
        frame_input,
        text="Nilai Mata Pelajaran " + str(i + 1) + ":",
        font=("Arial", 11, "bold"),
        bg="#1a2560",
        fg="white",
        anchor="e",
        width=22,
    )
    lbl.grid(row=i, column=0, padx=5, pady=5)
 
    ent = tk.Entry(frame_input, bd=3, width=15)
    ent.grid(row=i, column=1, padx=5, pady=5)
    entries.append(ent)