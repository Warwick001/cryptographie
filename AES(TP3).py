# tp3
from cryptography.fernet import Fernet

# Génération et affichage de la clé
cle = Fernet.generate_key()
fernet = Fernet(cle)

# message à chiffrer
message = "Hello world".encode()

# chiffrement
message_chiffre = fernet.encrypt(message)

# déchiffrement
message_dechiffre = fernet.decrypt(message_chiffre)

print("Clé :", cle.decode())
print("Chiffré :", message_chiffre)
print("Déchiffré :", message_dechiffre.decode())
