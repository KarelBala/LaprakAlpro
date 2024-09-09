def enkripsi(pesan, kata_kunci):
    # Memeriksa validitas input
    if not (pesan.isalpha() and kata_kunci.isalpha()):
        return "Input harus hanya berisi huruf tanpa spasi atau angka."

    # Membuat kamus konversi huruf ke angka dan sebaliknya
    huruf_ke_angka = { 'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 
                        'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 
                        't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25 }
    angka_ke_huruf = { v: k for k, v in huruf_ke_angka.items() }

    # Mengulangi kata kunci hingga panjangnya sesuai dengan pesan
    panjang_pesan = len(pesan)
    panjang_kata_kunci = len(kata_kunci)
    kata_kunci_panjang = (kata_kunci * (panjang_pesan // panjang_kata_kunci + 1))[:panjang_pesan]

    hasil = []

    for i in range(panjang_pesan):
        nilai_pesan = huruf_ke_angka[pesan[i]]
        nilai_kunci = huruf_ke_angka[kata_kunci_panjang[i]]
        nilai_enkripsi = (nilai_pesan + nilai_kunci) % 26
        hasil.append(angka_ke_huruf[nilai_enkripsi])

    return ''.join(hasil)

# Contoh penggunaan
pesan = input("Masukkan pesan (hanya huruf kecil tanpa spasi): ").strip().lower()
kata_kunci = input("Masukkan kata kunci (hanya huruf kecil tanpa spasi): ").strip().lower()
print("Hasil enkripsi:", enkripsi(pesan, kata_kunci))
