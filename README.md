class HashTable:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def _linear_probing(self, key, index):
        return (self._get_hash(key) + index) % self.size

    def _probing(self, key):
        for index in range(self.size):
            probeHash = self._linear_probing(key, index)
            if self.map[probeHash] is None or self.map[probeHash] == "deleted":
                return probeHash
        return None  # Jika semua slot penuh

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = [key_value]
        else:
            key_hash = self._probing(key)
            if key_hash is None:
                print("Buku Telpon Penuh")
                return False

            if self.map[key_hash] is None or self.map[key_hash] == "deleted":
                self.map[key_hash] = [key_value]
        return True

    def print_all(self):
        # Cetak elemen dalam urutan penyimpanan di hash table
        print("==== ISI HASH TABLE ====")
        for slot in self.map:
            if slot is not None and slot != "deleted":
                for key_value in slot:
                    print(f"NIM: {key_value[0]} NAMA: {key_value[1]}")

    def get_data(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for item in self.map[key_hash]:
                if item[0] == key:
                    return item[1]
        return None

    def resize(self, new_size):
        # Simpan elemen lama
        old_map = []
        for slot in self.map:
            if slot is not None and slot != "deleted":
                old_map.extend(slot)

        # Buat tabel baru
        self.size = new_size
        self.map = [None] * self.size

        # Masukkan elemen ke tabel baru dengan mempertahankan urutan asli
        for key_value in old_map:
            self.add(key_value[0], key_value[1])


def main():
    ht = HashTable()
    # isi hash table
    ht.add(71210699, "Andreas")
    ht.add(71210683, "Yandi")
    ht.add(71210689, "Gian")

    print("==== HASH TABLE SEBELUM DIRESIZE ====\n")
    ht.print_all()
    print(f"\nmahasiswa dengan NIM 71210683 adalah {ht.get_data(71210683)}\n")

    # resize hash table
    ht.resize(20)

    print("==== HASH TABLE SETELAH DIRESIZE ====\n")
    ht.print_all()
    print(f"\nmahasiswa dengan NIM 71210683 adalah {ht.get_data(71210683)}")


if __name__ == "__main__":
    main()
