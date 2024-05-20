def matematika(seznam):
    vysledek = []
    for kolo in seznam:
        cas = kolo[0]
        rekord = kolo[1]
        moznosti = 0
       # milisekundy = range(1, cas+1)
        milisekundy = list(range(1, cas+1))
        for rychlost in milisekundy:
            zbytek_casu = cas - rychlost
            draha = zbytek_casu * rychlost
            if draha > rekord:
                moznosti += 1
        vysledek.append(moznosti)
    return vysledek



with open ("advent_of_code_2023\\06\\06.txt", encoding = "utf-8") as soubor:
    for radek in soubor:        
        if "Time" in radek:
            radek = radek.strip() 
            radek = list(radek.split(" "))           
            seznam_time = []
            for i in radek[1:]:
                if i == "":
                    continue
                else:
                    i = int(i)
                    seznam_time.append(i)
        if "Distance" in radek:
            radek = radek.strip()
            radek = list(radek.split(" "))
            seznam_distance = []
            for i in radek[1:]:
                if i == "":
                    continue
                else:
                    i = int(i)
                    seznam_distance.append(i)
    print(seznam_time)
    print(seznam_distance)

    seznam = list(zip(seznam_time, seznam_distance))
    print(seznam)

    vysledek = matematika(seznam)
    mezisoucin = 1
    for i in vysledek:
        mezisoucin = mezisoucin * i
    print("vysledek")
    print(mezisoucin)


