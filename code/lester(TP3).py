import numpy as np

def hill_encrypt(plaintext, key_matrix):

    # converti le text en valeur numérique
    plaintext = plaintext.upper().replace(" ", "")
    plaintext_vector = [ord(char) - ord('A') for char in plaintext]
    n = len(key_matrix)

    while len(plaintext_vector) % n != 0:
        plaintext_vector.append(25)  # Remplissage avec 'Z' (normalement = 25)
    
    # texte brut en forme de matrice
    plaintext_matrix = np.array(plaintext_vector).reshape(-1, n)
    
    # chiffrer en utilisant la multiplication de matrices (mod 26)
    encrypted_matrix = np.dot(plaintext_matrix, key_matrix) % 26
    encrypted_text = ''.join(chr(int(num) + ord('A')) for num in encrypted_matrix.flatten())
    
    return encrypted_text

key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  # matrice 3x3
plaintext = "Salutttt"
ciphertext = hill_encrypt(plaintext, key_matrix)
print("Encrypted text:", ciphertext)
print("Texte déchiffrer :", plaintext)
