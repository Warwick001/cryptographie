import rsa

# Génération de clés publique/privée
(public_key, private_key) = rsa.newkeys(2048)

# Message chiffrer
message = "Hello la cryptoo".encode()

# chiffrement avec la clé publique
chiffre = rsa.encrypt(message, public_key)

# Déchiffrement avec la clé privée
dechiffre = rsa.decrypt(chiffre, private_key)

print("Chiffré :", chiffre)
print("Déchiffré :", dechiffre.decode())
