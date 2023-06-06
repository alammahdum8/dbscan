import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Fungsi untuk mengupload file CSV
def upload_csv():
    try:
        file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
        if file_path:
            data = pd.read_csv(file_path)
            messagebox.showinfo("Informasi", "File CSV berhasil diupload.")
            process_data(data)
    except FileNotFoundError:
        messagebox.showerror("Error", "File tidak ditemukan.")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat membaca file: {e}")

# Fungsi untuk melakukan prosesing data setelah file CSV diupload
def process_data(data):
    # Kode prosesing data yang ingin dilakukan
    # ...
    messagebox.showinfo("Informasi", "Prosesing data selesai.")

# Membuat jendela utama
window = tk.Tk()

# Membuat tombol untuk mengupload file CSV
upload_button = tk.Button(window, text="Upload CSV", command=upload_csv)
upload_button.pack(pady=10)

# Menjalankan jendela utama
window.mainloop()
