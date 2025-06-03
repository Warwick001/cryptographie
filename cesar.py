def cesar_chiffrement_complet(texte, cle):
    resultat = ""
    for char in texte:
        decale = ord(char) + cle
        resultat += chr(decale)
    return resultat

def cesar_dechiffrement_complet(texte, cle):
    return cesar_chiffrement_complet(texte, -cle)

texte_original = input("Saisir le texte à chiffrer: ")
cle = int(input("Saisir un chiffre pour le chiffrement: "))

texte_chiffre = cesar_chiffrement_complet(texte_original, cle)
texte_dechiffre = cesar_dechiffrement_complet(texte_chiffre, cle)

print("Texte chiffré:", texte_chiffre)
print("Texte déchiffré:", texte_dechiffre)
