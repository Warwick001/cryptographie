# calcule l'inverse modulaire
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# fonction pour chiffrer un texte avec le chiffrement affine
def affine_encrypt(text, a, b):
    if mod_inverse(a, 26) is None:
        raise ValueError("La clé 'a' doit être coprime avec 26.")
    
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encrypted_char = chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
            encrypted_text += encrypted_char.upper() if is_upper else encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Déchiffrement du texte
def affine_decrypt(ciphertext, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("La clé 'a' doit être coprime avec 26.")
    
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((a_inv * ((ord(char) - ord('a')) - b)) % 26) + ord('a'))
            decrypted_text += decrypted_char.upper() if is_upper else decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

try:
    a, b = 5, 8  # clés chiffrement
    texte_clair = "Bonjour WORLDDD"
    texte_chiffre = affine_encrypt(texte_clair, a, b)
    texte_dechiffre = affine_decrypt(texte_chiffre, a, b)
    print ("-------------------Chiffrement affine----------------------------")
    print("Texte clair saisi :", texte_clair)
    print("Texte chiffré :", texte_chiffre)
    print("Texte déchiffré :", texte_dechiffre)
except ValueError as e:
    print(e)
