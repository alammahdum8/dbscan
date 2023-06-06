import matplotlib.pyplot as plt
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

    # Visualisasi hasil clustering
    plt.scatter(data[:, 0], data[:, 1], c=clusters, cmap='viridis')
    plt.title('Hasil Clustering dengan DBSCAN')
    plt.xlabel('Fitur 1')
    plt.ylabel('Fitur 2')
    plt.show()

    # Model kurva
    core_samples_mask = np.zeros_like(dbscan.labels_, dtype=bool)
    core_samples_mask[dbscan.core_sample_indices_] = True
    n_clusters_ = len(set(dbscan.labels_)) - (1 if -1 in dbscan.labels_ else 0)
    n_noise_ = list(dbscan.labels_).count(-1)
    print('Jumlah Cluster:', n_clusters_)
    print('Jumlah Noise:', n_noise_)

