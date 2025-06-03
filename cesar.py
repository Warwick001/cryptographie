def cesar(texte, cle, mode):
    if mode == 2:  #déchiffrement
        cle = -cle  #inversion de la clé

    resultat = ""
    for char in texte:
        if char.isalpha():
            decale = ord(char) + cle
            if char.islower():
                if decale > ord('z'):
                    decale -= 26
                elif decale < ord('a'):
                    decale += 26
            elif char.isupper():
                if decale > ord('Z'):
                    decale -= 26
                elif decale < ord('A'):
                    decale += 26
            resultat += chr(decale)
        else:
            resultat += char

    return resultat

print("*** CHIFFREMENT DE CESAR ***")
print("-----------------------------------")

while True: #Boucle de répétition
    mode = input("Choisissez une option (1 = Chiffrer, 2 = Déchiffrer): ").strip()
    if mode not in ["1", "2"]:
        print("Veuillez entrer 1 pour chiffrer ou 2 pour déchiffrer")
        continue
    
    texte = input("Saisir le texte: ")
    while True:#boucle chiffre entier
        try:
            cle = int(input("Saisir la clé (nombre entier): "))
            break  #Fin boucle chiffre entier
        except ValueError:
            print("Erreur : Veuillez saisir un nombre entier valide !")
            
    texte_resultat = cesar(texte, cle, int(mode))
    print(f"Texte transformé : {texte_resultat}")

    recommencer = input("Voulez-vous recommencer ? (oui/non) : ").strip().lower()
    if recommencer != "oui":
        print("end")
        break 
#Fin boucle de répétition
