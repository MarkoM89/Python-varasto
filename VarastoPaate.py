import mariadb
import sys

toiminto = int(1)
kuittinumero = int(0)
maksukortit = []
tuotteet = []
kuitit = []
ostetutTuotteet = []



try:
    conn = mariadb.connect(
        user="tietokannan kayttaja",
        password="tietokannan salasana",
        host="ip-osoite tietokannalle",
        port="tietokannan portti",
        database="tietokannan nimi"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


cur = conn.cursor()


'''

Päätoiminto 1: Varastohallinta
		Toiminto 1: Varastosaldo
		Toiminto 2: Osta lisää tuotetta varastoon


Päätoiminto 2: Tuotehallinta
		Toiminto 1: Lisää tuote
		Toiminto 2: Poista tuote
		Toiminto 3: Tulosta tuotteet
		
Päätoiminto 3: Ostoseuranta
		Toiminto 1: Selaa kuitteja
		Toiminto 2: Etsi kuitti

		
Päätoiminto 4: Poistu ohjelmasta
'''

while toiminto != 4:
    
    toiminto = int(input("\nPäätoiminto 1: Varaston hallinta\nPäätoiminto 2: Tuotehallinta\nPäätoiminto 3: Seuranta\n"
        			+ "Päätoiminto 4: Poista ohjelmasta\n"))

    if toiminto == 1:
        print("Päätoiminto 1: Varastohallinta")


    elif toiminto == 2:
        print("Päätoiminto 2: Tuotehallinta")

        while toiminto != 4:

				
            toiminto = int(input("\nToiminto 1: Lisää tuote\nToiminto 2: Poista tuote\nToiminto 3: Tulosta tuotteet\n"
				    		+ "Toiminto 4: Poistu tuotehallinnasta\n"))
        
            if toiminto == 1:
                nimi = (input("Tuotenimi: "))
                hinta = input("Tuotteen yksikköhinta: ")

                cur.execute("INSERT INTO tuote (tuotenimi, yksikköhinta) VALUES (?, ?)",
                        (nimi, float(hinta)))

                conn.commit()
            
            elif toiminto == 2:
                tuotetunnus = input("Tuotetunnus? Tyhjä kenttä ei poista mitään: ")
                tuoteloytyi = False

                if (tuotetunnus != ""):

                    cur.execute("DELETE FROM tuote where tuotetunniste = ?",
                        ((tuotetunnus,)))


                conn.commit()

            elif toiminto == 3:
                print("Tuotelista\n-----------------------")

                cur.execute("SELECT * FROM tuote")

                for(tuotetunniste, tuotenimi, yksikköhinta) in cur:

                    print(str(tuotetunniste)+ " " +tuotenimi+ " " +str(yksikköhinta)+ "€")

        toiminto = 0

    elif toiminto == 3:

        print("\nPäätoiminto 3: Ostoseuranta\n")

        toiminto = 0

        while toiminto != 3:


            toiminto = int(input("Toiminto 1: Selaa kuitteja\nToiminto 2: Etsi kuitti\nToiminto 3: Poistu ostoseurannasta\n"))
                               


            if toiminto == 1:


                print("\n\nKuitit\n-----------------------------------------\n")

                cur.execute("select * from kuitti")

                for (kuittitunnus, osto_aika, kokonaishinta) in cur:
                    print(str(kuittitunnus)+ " " +str(osto_aika)+ " " +str(kokonaishinta)+ "€")

                print("\n")


            if toiminto == 2:
                kuittinumero = int(input("Anna kuittinumero\n"))
                
                print("\nKuitit\n-----------------------------------------\n")

                cur.execute("select * from kuitti where kuittitunnus=?", (kuittinumero,))

                for (kuittitunnus, osto_aika, kokonaishinta) in cur:
                    print(str(kuittitunnus)+ " " +str(osto_aika)+ " " +str(kokonaishinta)+ "€")

                print("\n")


        toiminto = 0


        
    elif toiminto == 4:
        print("Ohjelma sulkeutuu")



    else:
        print("Valikko toimii luvuilla 1-4")