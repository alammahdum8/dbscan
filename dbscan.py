import pandas as pd

# Fungsi untuk mengupload file CSV
def upload_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan saat membaca file:", e)

# Memasukkan path file CSV yang ingin diupload
file_path = input("Masukkan path file CSV: ")

# Memanggil fungsi upload_csv()
dataframe = upload_csv(file_path)

# Jika data berhasil diupload, tampilkan informasi dataset
if dataframe is not None:
    print("Dataset berhasil diupload. Informasi dataset:")
    print(dataframe.head())  # Menampilkan beberapa baris pertama dataset
