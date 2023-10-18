def encrypt_caesar(plaintext, shift):
  ciphertext = ''
  
  for char in plaintext:
    if not char.isalpha():
      ciphertext += char
    elif char.isupper():
      ciphertext += chr((ord(char) + shift - 65) % 26 + 65)
    else:
      ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
          
  return ciphertext



def decrypt_caesar(ciphertext, shift):
  plaintext = ''
  
  for char in ciphertext:
    if not char.isalpha():
      plaintext += char
    elif char.isupper():
      plaintext += chr((ord(char) - shift - 65) % 26 + 65)
    else:
      plaintext += chr((ord(char) - shift - 97) % 26 + 97)
          
  return plaintext


# Пример использования:

text = "Hello, World!"
shift = 3

ciphertext = encrypt_caesar(text, shift)
print("Зашифрованный текст:", ciphertext)

plaintext = decrypt_caesar(ciphertext, shift)
print("Расшифрованный текст:", plaintext)


'''

Результат выполнения:

Зашифрованный текст: Khoor, Zruog!
Расшифрованный текст: Hello, World!

В данном примере мы зашифровали строку "Hello, World!" с помощью шифра Цезаря с сдвигом на 3 позиции вперед. Затем мы расшифровали полученный шифр обратно и получили исходную строку.

'''
