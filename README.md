def encrypt_message(message, keyword):
    # Fungsi untuk mengonversi huruf menjadi nilai (0-25)
    def char_to_index(c):
        return ord(c) - ord('a')

    # Fungsi untuk mengonversi nilai (0-25) menjadi huruf
        return chr(i + ord('a'))

    # Validasi input
    if any(not c.islower() for c in message) or any(not c.islower() for c in keyword):
        raise ValueError("Input harus berupa huruf kecil tanpa spasi atau angka")

    # Mengubah pesan dan kata kunci menjadi nilai numerik
    message_values = [char_to_index(c) for c in message]
    keyword_values = [char_to_index(c) for c in keyword]

    # Enkripsi pesan
    encrypted_values = []
    keyword_length = len(keyword_values)

    for i in range(len(message_values)):
        m_value = message_values[i]
        k_value = keyword_values[i % keyword_length]
        new_value = (m_value + k_value) % 26
        encrypted_values.append(new_value)

    # Mengubah nilai kembali menjadi huruf
    encrypted_message = ''.join(chr(v + ord('a')) for v in encrypted_values)
    
    return encrypted_message

# Minta input dari pengguna
message = input("Masukkan pesan (huruf kecil tanpa spasi/angka): ")
keyword = input("Masukkan kata kunci (huruf kecil tanpa spasi/angka): ")

try:
    encrypted_message = encrypt_message(message, keyword)
    print("Hasil enkripsi:", encrypted_message)
except ValueError as e:
    print(e)
