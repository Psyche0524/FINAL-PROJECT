def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_value = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift_value - shift) % 26 + shift_value)
        else:
            decrypted_text += char
    return decrypted_text

ciphertext = "QOSGOF QWDVSFG OFS EIWHS SOGM HC QFOYQ"
shift = 3
print(decrypt_caesar_cipher(ciphertext, shift))
