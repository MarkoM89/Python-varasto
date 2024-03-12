from MaksuKortti import *
from Tuote import *
from kuitti import *

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

# Get Cursor
cur = conn.cursor()

cur.execute("select * from pankki")

for (tunniste, nimi, saldo) in cur:
    print(f"tunniste: {tunniste}, nimi: {nimi}, saldo: {saldo}")
    maksukortit.append(MaksuKortti(nimi, float(saldo)))


print("\n\n\n")

cur.execute("select * from tuote")

for (tuotetunnste, tuoteNimi, yksikköhinta) in cur:
    print(f"tuotetunnste: {tuotetunnste}, tuoteNimi: {tuoteNimi}, yksikköhinta: {yksikköhinta}")
    tuotteet.append(Tuote(tuoteNimi, float(yksikköhinta)))


print("\n\n\n")

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
                hinta = float(input("Tuotteen yksikköhinta: "))
                tuotteet.append(Tuote(nimi, hinta))
            
            elif toiminto == 2:
                nimi = input("Tuotenimi? Tyhjä kenttä ei poista mitään: ")
                for tuote in tuotteet:
                    if tuote.haeNimi() == nimi:
                        tuotteet.remove(tuote)
                    else:
                        #Tuotetta ei löytynyt tulostuu, joka kierroksella, virhe
                        print("Tuotetta ei löytynyt")

            elif toiminto == 3:
                print("Tuotelista")
                for tuote in tuotteet:
                    tuote.tulostaTuote()

        toiminto = 0

    elif toiminto == 3:

        print("\nPäätoiminto 3: Seuranta")


        
    elif toiminto == 4:
        print("Ohjelma sulkeutuu")

    elif toiminto == 5:
        print("Korttien tiedot")
        for tieto in maksukortit:
            tieto.tulostaSaldo()

        print("\n\nKuitit\n-----------------------------------------\n")
        for kuitti in kuitit:
            kuitti.tulostaKuitti()

    else:
        print("Valikko toimii luvuilla 1-4")