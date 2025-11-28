Påsen del 1:
Man kan öppna påsen.
Man kan ta bort saker, antingen en sak (som man skriver) eller allt.
Man kan söka efter en sak i påsen.
Det kan max vara 10 saker.
Man kan spara saker tills att man skriver avbryt.
Om man ska spara eller ta bort något så kan man skriva "avbryt" om man vill gå tillbaka.
Man kan stänga programmet.

Jag använde några listmetoder: append, remove och clear.

--------------------------------------------------------------------------------------------

Påsen del 2:
Vad har du använt för layouten i ditt GUI? Dvs. har du använt pack eller grid för att placera innehållet. Vilka skillnader har dessa?

- Först testade jag pack och sen duplicerade jag den filen och testade grid. Skillnaden var att med pack kunde man bara ha allt under varandra, men med grid kunde man bestämma mer exakt var man ville ha allt.

........................................

Hur sparar vi innehållet i väskan? Hur fungerar datatypen och varför väljer vi att jobba med den i det här programmet?

- För att spara gjorde jag ett fält man kan skriva i och bredvid en "addbutton" som man klickar på för att spara. "addbutton" har ett kommando som gör att saken läggs till i listan "inventory" med .append. Sen ser man det man har lagt till i textboxen. Datatypen är "string" och är text. Det som man skriver blir till en "string". Eftersom det är text man ser i textboxen och inte bilder eller nummer så använder vi "string".

........................................

Hur fungerar kontroller i tkinter? Förklara tillexempel hur du lägger till en knapp och får den att fungera, vad krävs?

- kod: def add_to_bag(event=None):
            blablabla


    add_button = tkinter.Button(main,text="Spara i påsen", command=add_to_bag)

  Ett sätt att göra en knapp:
  Man väljer ett namn på knappen och skriver sen "tkinter.Button(namn på main window, text="Namn på knappen",   command=namn på kommandot)

  Kommando:
  def namn på kommandot():
      skriv vad som ska hända

..........................................

Finns det skillnader mellan ditt program som använder tkinter och terminalen? Vilka är det i så fall och varför skiljer det sig?

- Terminal (skriver vad man ska göra):
1. Programmet frågar vad du vill göra med print, 2. skriv det du väljar att göra, 3. beroende på vad du väljer kommer det stå vad du ska skriva härnäst, 4. Sen börjar det om att programmet frågar vad du vill göra.

Programmet loopar tills du väljer att abryta.

tkinter(knappar):
1. skriver in i fältet som hör till rätt knapp (spara eller ta bort), 2. klicka på knappen bredvid 3. ser vad som händer i textboxen (inventoryt)

Om man klickar på "abryt" stängs programmet.

Varför:
I terminalen kan det bara vara text. Det printas mer text efter varje "steg" man gör.

Med tkinter gör man ett fönster med ett gränsnitt (grafiskt).

.............................................

Jämför strukturen på programmen? Vad är det som driver programmet i terminal versionen och vad ersätts det med i tkinter?

- Terminal:
  En while-loop. När run = True körs programmet.

  Tkinter:
  Main window och mainloop.

  main = tkinter.Tk()
  blablabla

  main.mainloop()

  ...........................................

  Förbättringar:
  Att göra så att allt skalas efter fönstrets storlek. Det blir bättre för användaren.
