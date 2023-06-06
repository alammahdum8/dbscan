from sklearn.cluster import DBSCAN

# Fungsi untuk melakukan proses clustering menggunakan metode DBSCAN
def perform_clustering(data):
    # Inisialisasi model DBSCAN
    dbscan = DBSCAN(eps=0.3, min_samples=5)  # Atur parameter sesuai kebutuhan

    # Melakukan clustering pada data
    clusters = dbscan.fit_predict(data)

    # Menampilkan hasil clustering
    print("Hasil Clustering:")
    print(clusters)

# Memanggil fungsi perform_clustering() dengan dataframe yang sudah dinormalisasi sebelumnya
perform_clustering(normalized_dataframe)
