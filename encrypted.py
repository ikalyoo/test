import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation 
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"Chars: {chars}")
print(f"Key  : {key}")


plaintext = input("Enter plaintext: ")
ciphertext = ""

for words in plaintext:
    index = plaintext.index(words)
    ciphertext += key[chars.index(words)]

print(f"Ciphertext: {ciphertext}")

ciphertext = input("Enter ciphertext: ")
plaintext = ""

for words in ciphertext:
    index = ciphertext.index(words)
    plaintext += chars[key.index(words)]

print(f"Plaintext: {plaintext}")