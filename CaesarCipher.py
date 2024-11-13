def enkripsi(plain_text, shift):
    cipher_text =""
    for char in plain_text:
        # Huruf Besar
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Huruf Kecil
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            #karakter selain huruf tetap
            cipher_text += char
    return cipher_text

def deskripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        # huruf besar
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 +65)
        # huruf kecil
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 +97)
        else:
            #karakter selain huruf tetap
            plain_text += char
    return plain_text

#interface pengguna

def main():
    print("Selamat datang di Program Kriptografi Caesar")
    plain_text = input("Masukkan teks asli (plaintext): ")
    shift = int(input("Masukkan Nilai Pergeseran (1- 25): "))

    #panggil fungsi enkripsi
    cipher_text = enkripsi(plain_text, shift)
    print("Teks Terenkripsi: ", cipher_text)

    #panggil fungsi deskripsi
    deskripsi_text = deskripsi(cipher_text, shift)
    print("Teks Terdeskripsi: ", deskripsi_text)

if __name__ == "__main__":
    main()