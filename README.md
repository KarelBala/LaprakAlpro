import json

# Nama file JSON
filename = 'data_kuliah.json'

# Fungsi untuk menambahkan data ke file JSON
def tambah_data_ke_json(filename):
    # Membaca data yang ada
    with open(filename, 'r') as file:
        data_lama = json.load(file)

    # Mengambil input dari pengguna
    mata_kuliah = input("Masukkan nama mata kuliah: ")
    kode = input("Masukkan kode mata kuliah: ")
    dosen = input("Masukkan dosen (pisahkan dengan koma): ").split(',')
    grup = input("Masukkan grup (pisahkan dengan koma): ").split(',')

    # Membuat dictionary untuk data baru
    data_baru = {
        mata_kuliah: {
            "kode": kode,
            "dosen": [dosen.strip() for dosen in dosen],
            "grup": [grup.strip() for grup in grup]
        }
    }

    # Menambahkan data baru ke data lama
    data_lama.update(data_baru)

    # Menyimpan data yang telah diperbarui
    with open(filename, 'w') as file:
        json.dump(data_lama, file, indent=4)

    print("Data berhasil ditambahkan.")

# Memanggil fungsi untuk menambahkan data
tambah_data_ke_json(filename)
