from itertools import combinations

def zkontroluj(cislo):
    if radek[prvni_X - 1] == "*":            
        return prvni_X - 1, "nic"          # X-ova souradnice *
    if radek[posledni_X + 1] == "*":         
        return posledni_X + 1, "nic"       # X-ova souradnice *      
    if aktualni_Y > 0:
        usek = predchozi_radek[prvni_X-1 : posledni_X+2]
        for c in usek:
            if c == "*":
                pozice_c_v_useku = usek.index(c)
                radek_do_c = predchozi_radek[:prvni_X-1+pozice_c_v_useku+1]
                index_c = len(radek_do_c)-1                
                return index_c, "zmena"      # X-ova souradnice *
    
    return "nevalidni", "nic" 

with open('advent_of_code_2023\\03\\03.txt', encoding='utf-8') as soubor:
    
    aktualni_Y = 0
    ulozene = []
    seznam_star = []
    seznam_suma = []
    predchozi_radek = ""
    for radek in soubor:
        radek = radek.strip()
        radek = "." + radek + "."       
        aktualni_X = 0
        cislo = ""

        if ulozene:
            for j in ulozene[:]:                
                star_Y, cislo, prvni_X, posledni_X = j
                usek = radek[prvni_X-1:posledni_X+2]
                for c in usek:
                    if c == "*":
                        pozice_c_v_useku = usek.index(c)
                        radek_do_c = predchozi_radek[:prvni_X-1+pozice_c_v_useku+1]
                        index_c = len(radek_do_c)-1
                        star_X = index_c
                        star_Y += 1
                        cislo = int(cislo)
                        souradnice = (star_X, star_Y, cislo, prvni_X, posledni_X)
                        if souradnice not in seznam_star:
                            seznam_star.append(souradnice)
                            #print(f"prictu cislo: {cislo}")
                ulozene.remove(j)
                cislo = ""

        for i in radek:                        
            if i in "0123456789":                
                znak = radek[aktualni_X]
                cislo += znak
                if radek[aktualni_X-1] not in "0123456789":
                    prvni_X = aktualni_X
            elif i not in "0123456789" and radek[aktualni_X - 1] in "0123456789":
                posledni_X = aktualni_X-1
                vysledek, zmena_Y = zkontroluj(cislo)
                if vysledek != "nevalidni":
                    star_X = vysledek
                    if zmena_Y == "nic":
                        star_Y = aktualni_Y
                    elif zmena_Y == "zmena":
                        star_Y = aktualni_Y-1
                    cislo = int(cislo)
                    souradnice = (star_X, star_Y, cislo, prvni_X, posledni_X)
                    seznam_star.append(souradnice)  
                    #print(f"prictu cislo: {cislo}")
                    cislo = ""                    
                else:                    
                    star_Y = aktualni_Y
                    cislo = int(cislo)
                    hodnoty = (star_Y, cislo, prvni_X, posledni_X)
                    ulozene.append(hodnoty)
                    cislo = ""
            aktualni_X += 1

        predchozi_radek = radek
        aktualni_Y += 1

   
    dvojice = combinations(seznam_star, 2)
    dvojice = tuple(dvojice)        
    dvojice_seznam = list(dvojice)
    #print(dvojice)
    #print(dvojice_seznam)

    

    for prvni, druha in dvojice_seznam:
        if prvni[0] == druha[0] and prvni[1] == druha[1]:
            soucin = prvni[2]*druha[2]
            print(soucin)
            seznam_suma.append(soucin)

    
    soucet = sum(seznam_suma)
    print(soucet)
