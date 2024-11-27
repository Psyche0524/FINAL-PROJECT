import math

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if mode == 'encrypt':
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                result += char
        elif mode == 'decrypt':
            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - shift - 97) % 26 + 97)
            else:
                result += char
    return result

def atbash_cipher(text):
    result = ""
    for char in text:
        if char.isupper():
            result += chr(90 - (ord(char) - 65))
        elif char.islower():
            result += chr(122 - (ord(char) - 97))
        else:
            result += char
    return result

def rot13_cipher(text):
    return caesar_cipher(text, 13, mode='encrypt')

def affine_cipher(text, a, b, mode='encrypt'):
    result = ""
    for char in text:
        if mode == 'encrypt':
            if char.isupper():
                result += chr(((a * (ord(char) - 65) + b) % 26) + 65)
            elif char.islower():
                result += chr(((a * (ord(char) - 97) + b) % 26) + 97)
            else:
                result += char
        elif mode == 'decrypt':
            a_inv = pow(a, -1, 26)  # Modular multiplicative inverse of a under modulo 26
            if char.isupper():
                result += chr((a_inv * ((ord(char) - 65) - b) % 26) + 65)
            elif char.islower():
                result += chr((a_inv * ((ord(char) - 97) - b) % 26) + 97)
            else:
                result += char
    return result

def caesars_box_cipher(text, mode='encrypt'):
    length = len(text)
    side = math.ceil(math.sqrt(length))
    grid = [['' for _ in range(side)] for _ in range(side)]
    
    if mode == 'encrypt':
        index = 0
        for r in range(side):
            for c in range(side):
                if index < length:
                    grid[r][c] = text[index]
                    index += 1
        
        result = ''
        for c in range(side):
            for r in range(side):
                if grid[r][c] != '':
                    result += grid[r][c]
    elif mode == 'decrypt':
        index = 0
        for c in range(side):
            for r in range(side):
                if index < length:
                    grid[r][c] = text[index]
                    index += 1
        
        result = ''
        for r in range(side):
            for c in range(side):
                if grid[r][c] != '':
                    result += grid[r][c]
    
    return result

def columnar_transposition_cipher(text, key, mode='encrypt'):
    k_len = len(key)
    text_len = len(text)
    cols = sorted(range(k_len), key=lambda x: key[x])
    
    if mode == 'encrypt':
        extra_chars = (k_len - text_len % k_len) % k_len
        text += ' ' * extra_chars
        rows = math.ceil(text_len / k_len)
        
        grid = [['' for _ in range(k_len)] for _ in range(rows)]
        index = 0
        for r in range(rows):
            for c in range(k_len):
                if index < text_len:
                    grid[r][c] = text[index]
                    index += 1
        
        result = ''
        for c in cols:
            for r in range(rows):
                if grid[r][c] != '':
                    result += grid[r][c]
    else:
        rows = math.ceil(text_len / k_len)
        full_cols = text_len % k_len
        col_lengths = [rows] * full_cols + [rows - 1] * (k_len - full_cols)
        
        grid = [''] * k_len
        index = 0
        for c in range(k_len):
            length = col_lengths[cols.index(c)]
            grid[cols[c]] = text[index:index + length]
            index += length
        
        result = ''
        for r in range(rows):
            for c in range(k_len):
                if r < len(grid[c]):
                    result += grid[c][r]
    
    return result

def main():
    while True:
        print("\nOptions:")
        print("1. Encrypt a word using Caesar Cipher")
        print("2. Decrypt a word using Caesar Cipher")
        print("3. Encrypt/Decrypt a word using ATBASH Cipher")
        print("4. Encrypt a word using ROT13 Cipher")
        print("5. Decrypt a word using ROT13 Cipher")
        print("6. Encrypt a word using Affine Cipher")
        print("7. Decrypt a word using Affine Cipher")
        print("8. Encrypt a word using Caesar's Box Cipher")
        print("9. Decrypt a word using Caesar's Box Cipher")
        print("10. Encrypt a word using Columnar Transposition Cipher")
        print("11. Decrypt a word using Columnar Transposition Cipher")
        print("12. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter a word to encrypt: ")
            shift = int(input("Enter shift number: "))
            encrypted_text = caesar_cipher(text, shift, mode='encrypt')
            print(f"Encrypted word: {encrypted_text}")
        elif choice == "2":
            text = input("Enter a word to decrypt: ")
            shift = int(input("Enter shift number: "))
            decrypted_text = caesar_cipher(text, shift, mode='decrypt')
            print(f"Decrypted word: {decrypted_text}")
        elif choice == "3":
            text = input("Enter a word to encrypt/decrypt using ATBASH Cipher: ")
            result = atbash_cipher(text)
            print(f"Result: {result}")
        elif choice == "4":
            text = input("Enter a word to encrypt using ROT13 Cipher: ")
            encrypted_text = rot13_cipher(text)
            print(f"Encrypted word: {encrypted_text}")
        elif choice == "5":
            text = input("Enter a word to decrypt using ROT13 Cipher: ")
            decrypted_text = rot13_cipher(text)
            print(f"Decrypted word: {decrypted_text}")
        elif choice == "6":
            text = input("Enter a word to encrypt: ")
            a = int(input("Enter a value (must be coprime with 26): "))
            b = int(input("Enter b value: "))
            encrypted_text = affine_cipher(text, a, b, mode='encrypt')
            print(f"Encrypted word: {encrypted_text}")
        elif choice == "7":
            text = input("Enter a word to decrypt: ")
            a = int(input("Enter a value (must be coprime with 26): "))
            b = int(input("Enter b value: "))
            decrypted_text = affine_cipher(text, a, b, mode='decrypt')
            print(f"Decrypted word: {decrypted_text}")
        elif choice == "8":
            text = input("Enter a word to encrypt using Caesar's Box Cipher: ")
            encrypted_text = caesars_box_cipher(text, mode='encrypt')
            print(f"Encrypted word: {encrypted_text}")
        elif choice == "9":
            text = input("Enter a word to decrypt using Caesar's Box Cipher: ")
            decrypted_text = caesars_box_cipher(text, mode='decrypt')
            print(f"Decrypted word: {decrypted_text}")
        elif choice == "10":
            text = input("Enter a word to encrypt using Columnar Transposition Cipher: ")
            key = input("Enter the key: ")
            encrypted_text = columnar_transposition_cipher(text, key, mode='encrypt')
            print(f"Encrypted word: {encrypted_text}")
        elif choice == "11":
            text = input("Enter a word to decrypt using Columnar Transposition Cipher: ")
            key = input("Enter the key: ")
            decrypted_text = columnar_transposition_cipher(text, key, mode='decrypt')
            print(f"Decrypted word: {decrypted_text}")
            
            # Explanation of Decryption
            print("\nDecryption Explanation:")
            print(f"1. Keyword: {key}")
            cols = sorted(range(len(key)), key=lambda x: key[x])
            col_order = ''.join([str(cols.index(i) + 1) for i in range(len(key))])
            print(f"2. Column Order: {col_order}")
            
            grid = [decrypted_text[i:i+len(key)] for i in range(0, len(decrypted_text), len(key))]
            
            # Display the grid
            print("\nGrid:")
            for row in grid:
                print(' '.join(row))
            
        elif choice == "12":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose")