

import mariadb
import sys

toiminto = int(1)
maksukortit = []
tuotteet = []
kuitit = []
ostetutTuotteet = []



try:
    conn = mariadb.connect(
        user="root",
        password="T13t0k4!?t4",
        host="127.0.0.1",
        port=3306,
        database="kokeilutietokanta"

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
		
Päätoiminto 3: Seuranta
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

        print("\nPäätoiminto 3: Seuranta")


        
    elif toiminto == 4:
        print("Ohjelma sulkeutuu")

    elif toiminto == 5:
        print("Korttien tiedot\n")

        cur.execute("SELECT * FROM pankki")
        for(tunniste, nimi, saldo) in cur:

            print(str(tunniste)+ " " +nimi+ " " +str(saldo)+ "€")


        print("\n\nKuitit\n-----------------------------------------\n")
        cur.execute("SELECT * FROM tuote")

        for(tuotetunniste, tuotenimi, yksikköhinta) in cur:

            print(str(tuotetunniste)+ " " +tuotenimi+ " " +str(yksikköhinta)+ "€")

    else:
        print("Valikko toimii luvuilla 1-4")