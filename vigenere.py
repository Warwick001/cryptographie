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
            ciphertext += char  #conserve caractères spéciaux
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
            plaintext += char  # Conserve caractères spéciaux
    return plaintext

print("*** CHIFFREMENT DE VIGENERE ***")
print("-----------------------------------")

while True:
    mode = input("Choisissez une option (1 = Chiffrer, 2 = Déchiffrer): ").strip()
    if mode not in ["1", "2"]:
        print("Veuillez entrer 1 pour chiffrer ou 2 pour déchiffrer")
        continue

    texte = input("Veuillez saisir le texte : ")
    cle = input("Veuillez saisir la clé (mot alphabétique) : ").strip()

    if not cle.isalpha():
        print("Erreur : La clé doit contenir uniquement des lettres.")
        continue

    if mode == "1":
        texte_resultat = vigenere_encrypt(texte, cle)
    else:
        texte_resultat = vigenere_decrypt(texte, cle)

    print(f"Texte transformé : {texte_resultat}")

    recommencer = input("Voulez-vous recommencer ? (oui/non) : ").strip().lower()
    if recommencer != "oui":
        print("Fin du programme.")
        break
