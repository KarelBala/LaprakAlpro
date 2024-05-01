def baca_file_teks(nama_file):
    try:
        with open(nama_file, 'r') as file:
            # Membaca seluruh isi file
            isi_file = file.read()
            # Memecah isi file menjadi kata-kata
            kata_kata = isi_file.split()
            # Menggunakan set untuk menyimpan kata-kata unik
            kata_unik = list(kata_kata)
            return list(kata_unik)
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
        return []

# Contoh penggunaan
nama_file_berita = "artikel.txt"  # Ganti dengan nama file berita yang sesuai
kata_unik_berita = baca_file_teks(nama_file_berita)

if kata_unik_berita:
    print("Kata-kata unik dalam berita:")
    for kata in kata_unik_berita:
        print(kata)
else:
    print("Tidak ada kata dalam berita atau file tidak ditemukan.")
