import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from clustering import perform_clustering

# Fungsi untuk mengupload file CSV
def upload_csv():
    try:
        file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
        if file_path:
            data = pd.read_csv(file_path)
            messagebox.showinfo("Informasi", "File CSV berhasil diupload.")
            normalize_data(data)
    except FileNotFoundError:
        messagebox.showerror("Error", "File tidak ditemukan.")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat membaca file: {e}")

# Fungsi untuk melakukan normalisasi pada dataset
def normalize_data(data):
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)
    normalized_df = pd.DataFrame(normalized_data, columns=data.columns)
    messagebox.showinfo("Informasi", "Data berhasil dinormalisasi.")
    perform_clustering(normalized_df)

# Membuat jendela utama
window = tk.Tk()

# Membuat tombol untuk mengupload file CSV
upload_button = tk.Button(window, text="Upload CSV", command=upload_csv)
upload_button.pack(pady=10)

# Menjalankan jendela utama
window.mainloop()
