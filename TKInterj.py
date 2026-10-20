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

label_jurusan = tk.Label(
    top,
    text="Pilihan Jurusan Anda:",
    font=("Arial", 11, "bold"),
    bg="#1a2560",
    fg="white",
)
label_jurusan.pack(pady=(25, 5))

daftar_jurusan = [
    "Teknologi Informasi",
    "Teknik Mesin",
    "Teknik Elektro",
    "Teknik Sipil",
    "Teknologi Rekayasa Otomotif",
    "Teknologi Elektro Medis",
    "Artificial Intellegence",
]
pilihan_jurusan = tk.StringVar(top)
pilihan_jurusan.set(daftar_jurusan[0])
menu_jurusan = tk.OptionMenu(top, pilihan_jurusan, *daftar_jurusan)
menu_jurusan.config(width=22, bg="white", fg="black")
menu_jurusan.pack()

tombol = tk.Button(
    top,
    text="Hasil Prediksi",
    font=("Arial", 11, "bold"),
    command=hasil_prediksi,
)
tombol.pack(pady=20)

label_hasil = tk.Label(
    top,
    text="",
    font=("Arial", 13, "bold"),
    bg="#1a2560",
    fg="cyan",
)
label_hasil.pack()
 
top.mainloop()