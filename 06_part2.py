def matematika(time, distance):
  
    moznosti = 0
    milisekundy = list(range(1, time+1))
    for rychlost in milisekundy:
        zbytek_casu = time - rychlost
        draha = zbytek_casu * rychlost
        if draha > distance:
            moznosti += 1
   
    return moznosti


with open ("advent_of_code_2023\\06\\06.txt", encoding="utf-8") as soubor:
    for radek in soubor:
        radek = radek.split(":")
        cisla = radek[1]
        cisla = cisla.strip()
        cislo = ""
        for i in cisla:
            if i == " ":
                continue
            else:
                cislo += i
        cislo = int(cislo)
        if radek[0]=="Time":
            time = cislo
        else:
            distance = cislo
    print(time)
    print(distance) 

moznosti = matematika(time, distance)
print(moznosti)