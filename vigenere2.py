from itertools import cycle

def vigenere_encrypt(plaintext, key):
    key_cycle = cycle(key)
    ciphertext = ""
    for char in plaintext:
        shift = ord(next(key_cycle)) % 256  # Décalage basé sur le code ASCII
        ciphertext += chr((ord(char) + shift) % 256)  # Assurer que le caractère reste dans l'intervalle ASCII
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    key_cycle = cycle(key)
    plaintext = ""
    for char in ciphertext:
        shift = ord(next(key_cycle)) % 256
        plaintext += chr((ord(char) - shift) % 256)  # Décalage inverse
    return plaintext

print("*** CHIFFREMENT DE VIGENERE ***")
print("-----------------------------------")

# Saisie utilisateur
texte_clair = input("Veuillez saisir le texte à chiffrer : ")
cle = input("Veuillez saisir la clé : ")

# Chiffrement et affichage
texte_chiffre = vigenere_encrypt(texte_clair, cle)
print("Texte chiffré :", texte_chiffre)

# Déchiffrement et affichage
texte_dechiffre = vigenere_decrypt(texte_chiffre, cle)
print("Texte déchiffré :", texte_dechiffre)
