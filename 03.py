def zkontroluj(cislo):
    if radek[prvni_X - 1] not in ".0123456789":             
        return "pricti" 
    # if prvni_X >0:
    #     if radek[prvni_X - 1] not in ".0123456789":             
    #         return cislo                    
    # if posledni_X+1 < delka_radku:
    #     if radek[posledni_X + 1] not in ".0123456789":         
    #         return cislo 
    if radek[posledni_X + 1] not in ".0123456789":         
        return "pricti"          
    if aktualni_Y > 0:
        usek = predchozi_radek[prvni_X-1 : posledni_X+2]
        for c in usek:
            if c not in ".0123456789":                
                return "pricti" 
    
    return "nevalidni" 

with open('advent_of_code_2023\\03\\03.txt', encoding='utf-8') as soubor:
    # Y... cisla radku od 0
    # X... pozice na radku od 0
    aktualni_Y = 0
    ulozene = []
    seznam_suma = []
    predchozi_radek = ""
    for radek in soubor:
        radek = radek.strip()
        radek = "." + radek + "."       
        aktualni_X = 0
        cislo = ""

        if ulozene:
            for j in ulozene[:]:                
                cislo, prvni_X, posledni_X, cislo_radku = j
                usek = radek[prvni_X-1:posledni_X+2]
                for c in usek:
                    if c not in ".0123456789":
                        if j not in seznam_suma:
                            seznam_suma.append(j)
                            print(f"prictu cislo: {cislo}")
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
                vysledek = zkontroluj(cislo)
                if vysledek == "pricti":
                    cislo_radku = aktualni_Y
                    souradnice = (cislo, prvni_X, posledni_X, cislo_radku)
                    seznam_suma.append(souradnice)  
                    print(f"prictu cislo: {cislo}")
                    cislo = ""                    
                else:                    
                    cislo_radku = aktualni_Y
                    hodnoty = (cislo, prvni_X, posledni_X, cislo_radku)
                    ulozene.append(hodnoty)
                    cislo = ""
            aktualni_X += 1
    
        predchozi_radek = radek
        aktualni_Y += 1
    seznam_cisel = []
    for k in seznam_suma:
        seznam_cisel.append(k[0])
    for index, i in enumerate(seznam_cisel[:]):
        seznam_cisel[index] = int(i)
    soucet = sum(seznam_cisel)
    print(soucet)

