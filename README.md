class Stack:
    def __init__(self):
        self._size = 0
        self._data = []
    def getLen(self):
        return self._size
    def top(self):
        if self._size == 0 :
            return None
        return self._data[-1]
    def pop(self):
        if self._size == 0:
            return None
        self._size-=1
        return self._data.pop()
    def push(self, data):
        self._data.append(data)
        self._size+= 1
    def printData(self):
        for i in range(1, self._size+1):
            print(self._data[-i])


# Jika stack ganjil, maka dibulatkan ke bawah.
# contoh: ada stack dengan anggota 67. maka, fungsi ini akan menghapus 
# 33 elemen stack paling bawah (karena 67/2 = 33.5, dibulatkan ke bawah = 33).
def hapusSetengahBawah(stack): 
    pass
             
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
    print("Tampilkan Stack Sebelum Di Hapus : ")
    s.printData()
    print()
    print("Melakukan Penghapusan Stack")
    print()
    # Hapus setengahnya
    hapusSetengahBawah(s)
    # Tampilkan data setelahnya
    print("Tampilan Stack Setelah Di Hapus : ")
    s.printData()
