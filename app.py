run = True

antal = 0

bag = ["godis", "kebab", "burgare"]

while run:

    print()
    spara = False

    #Meny
    print("Visa innehållet i påsen [V]")
    print("Spara i påsen [S]")
    print("Avsluta programmet [Q]")
    print("Ta bort något från påsen [R]")
    print("Sök efter nåt i påsen [F]")
    print()
    choice = input("Välj: ")

    #Öppna
    if choice.lower() == "v":
        print("*Öppnar påsen*")
        print("[", end='')

        for thing in bag:
            print(f" {thing} ", end='')
        print("]")

    #Spara
    elif choice.lower() == "s":
        spara = True
        if antal <= 10:
            while spara:
                x = input("Skriv vad du vill spara (max 10 saker), skriv [avbryt] för att avbryta:")
                if x.lower() != "avbryt": #Om inte avbryt, så ska den spara
                    bag.append(x)
                    antal += 1
                else:
                    spara = False
                
        else:
            print("För många saker :(")

    #Ta bort
    elif choice.lower() == "r":
        print("Påsens innehåll: ")
        print("[", end='')
        for thing in bag:
            print(f" {thing} ", end='')
        print("]")

        #Vad ta bort
        what_remove = input("Vad vill du ta bort från påsen [en sak] eller [allt], skriv [avbryt] för att gå tillbaka:")

        if what_remove.lower() == "en sak": #en sak
            search_remove = input("Skriv vad du vill ta bort: ")
            if search_remove.lower() in bag:
                bag.remove(search_remove)
                print(f"Du tog bort {search_remove} från påsen.")
            else:
                print(f"{search_remove} finns inte i påsen.")

        elif what_remove.lower() == "allt": #allt
            bag.clear()
            print("Du tog bort allt från påsen.")
        elif what_remove.lower() == "inget": #inget
            continue
        else:
            print("Felaktigt kommando") #fel

    #Avsluta
    elif choice.lower() == "q":
        run = False
    
    #Söka
    elif choice.lower() == "f":
        query = input("Vad vill du söka efter: ")
        if query.lower() in bag:
            print(f"Hittade: {query}")
        else:
            print(f"Du sökte efter {query}, men det finns inte i påsen.")

    #Fel kommando
    else:
        print("Felaktigt kommando, försök igen.")
    
    print()