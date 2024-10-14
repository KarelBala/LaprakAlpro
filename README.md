def hapusSetengahBawah(stack): 
    half_size = stack.getLen() // 2  # Hitung setengah ukuran, dibulatkan ke bawah
    temp = []  # List sementara untuk menyimpan elemen stack

    # Simpan semua elemen ke dalam list sementara
    while stack.getLen() > 0:
        temp.append(stack.pop())

    # Push kembali elemen yang tersisa ke dalam stack
    for i in range(len(temp) - half_size):
        stack.push(temp.pop())

# Contoh penggunaan
if __name__ == "__main__":
    s = Stack()
    # Isi Stack
    s.push(1)
    s.push(1.5)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    # Tampilkan stack sebelum dihapus
    print("Tampilkan Stack Sebelum Di Hapus:")
    s.printData()
    print()
    print("Melakukan Penghapusan Stack")
    print()
    # Hapus setengahnya
    hapusSetengahBawah(s)
    # Tampilkan data setelahnya
    print("Tampilan Stack Setelah Di Hapus:")
    s.printData()
