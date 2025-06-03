from itertools import cycle

def vigenere_encrypt(plaintext, key):
    key_cycle = cycle(key)
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = ord(next(key_cycle).lower()) - ord('a')
            if char.islower():
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    key_cycle = cycle(key)
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = ord(next(key_cycle).lower()) - ord('a')
            if char.islower():
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            plaintext += char
    return plaintext

texte_clair = input("Veuillez saisir le mot à chiffrer: ")
cle = input("Veuillez saisir la cle: ")

texte_chiffre = vigenere_encrypt(texte_clair, cle)
print("Texte chiffre :", texte_chiffre)