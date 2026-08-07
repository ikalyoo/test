import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation 
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"Chars: {chars}")
print(f"Key  : {key}")


plaintext = input("Enter the plaintext: ")
ciphertext = ""

for word in plaintext:
    index = chars.index(word)
    ciphertext += key[index]

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")


#decryption
ciphertext = input("Enter the ciphertext: ")
decrypted_text = ""

for word in ciphertext:
    index = key.index(word)
    decrypted_text += chars[index]

print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
