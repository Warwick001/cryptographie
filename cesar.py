def cesar_chiffrement(texte, cle):
    resultat = ""
    for char in texte:
        if char.isalpha():
            decale = ord(char) + cle
            if char.islower():
                if decale > ord('z'):
                    decale -= 26
            elif char.isupper():
                if decale > ord('Z'):
                    decale -= 26
            resultat += chr(decale)
        else:
            resultat += char
    return resultat

def cesar_dechiffrement(texte, cle):
    return cesar_chiffrement(texte, -cle)

# Exemple d'utilisation
texte_original = input("Saisir le texte à chiffrer: ")
cle = int(input("Saisir un chiffre pour le chiffrement: "))
texte_chiffre = cesar_chiffrement(texte_original, cle)
texte_dechiffre = cesar_dechiffrement(texte_chiffre, cle)

print("Texte chiffré:", texte_chiffre)
print("Texte déchiffré:", texte_dechiffre)