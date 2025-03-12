import random
import ordlista_Hangman
import ordlista_frukter

# Välj ett slumpmässigt ord
svar = random.choice(ordlista_frukter.frukter)
svar = list(svar)
#print(svar)  # Avslöja ordet för testning (kan tas bort)

# Förbered tomt ord
ord = ["_" if bokstav != " " else " " for bokstav in svar]
gissade_bokstäver = []
game_over = False

while not game_over:
    # Visa gissade bokstäver
    if len(gissade_bokstäver) > 0:
        print("Gissade bokstäver: " + " ".join(gissade_bokstäver))

    # Rita hangman-grafik
    print("\n".join(ordlista_Hangman.hangmans[len(gissade_bokstäver)]))

    # Visa det aktuella ordet
    print(" ".join(ord))

    # Få en giltig gissning
    gissning = ""
    while not (len(gissning) == 1 and gissning.isalpha() and gissning not in gissade_bokstäver):
        gissning = input("Ange en ny bokstav: ").lower()

    # Kontrollera gissning
    if gissning in svar:
        for i, bokstav in enumerate(svar):
            if bokstav == gissning:
                ord[i] = bokstav
    else:
        gissade_bokstäver.append(gissning)

    # Kontrollera om spelet är över
    if "_" not in ord:
        game_over = True
        print("\nBra jobbat! Du vann!")
    elif len(gissade_bokstäver) == len(ordlista_Hangman.hangmans) - 1:
        game_over = True
        print("\nDu förlorade!")

# Visa slutgiltigt svar
print("Ordet var: " + "".join(svar))
