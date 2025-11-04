run = True

antal = 0

bag = []

while run:

    print("Visa innehållet i påsen [V]")
    print("Spara i påsen [S]")
    print("Avsluta programmet [Q]")
    print("Ta bort något från påsen [R]")
    print()
    choice = input("Välj: ")

    if choice.lower() == "v":
        print("*Öppnar påsen*")
        print("[", end='')

        for thing in bag:
            print(f" {thing} ", end='')
        print("]")

    elif choice.lower() == "s":
        if antal <= 10:
            bag.append(input("Skriv vad du vill spara: "))
            antal += 1
        else:
            print("För många saker :(")

    elif choice.lower() == "r":
        print("Påsens innehåll: ")
        print("[", end='')
        for thing in bag:
            print(f" {thing} ", end='')
        print("]")
 
        bag.pop(int(input("Ta bort saken på plats nr (första är 0): ")))

    elif choice.lower() == "q":
        run = False
    else:
        print("Felaktigt kommando, försök igen.")