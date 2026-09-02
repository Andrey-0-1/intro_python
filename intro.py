import random

tall = random.randint(0, 1000)

for x in range(10):
    svar = int(input("Gjett tallet: "))

    if svar == tall:
        print("Riktig! Du fant tallet!")
        break
    elif svar < tall:
        print("Tallet er høyere.")
        print("Du har", 9 - x, "forsøk igjen.")
    else:
        print("Tallet er lavere.")
        print("Du har", 9 - x, "forsøk igjen.")

else:
    print("Du har brukt opp alle forsøkene. Du tapte!")

#dette er bare en test!!!!!!!!