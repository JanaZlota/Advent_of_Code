   
sum_IDs = 0



maximum_red = 12
maximum_green = 13
maximum_blue = 14
  


with open('advent_of_code_2023\\02\\02.txt', encoding='utf-8', mode="r") as soubor:
    for radek in soubor:
        radek = radek.strip()
        pozice_1 = radek.index(" ")
        pozice_2 = radek.index(":")
        ID = int(radek[pozice_1:pozice_2].strip())
        osekany_radek = radek[pozice_2+1:]
        jednotlive_sety = osekany_radek.split(";")
        vysledky = []
        for set in jednotlive_sety:
            sady_kostek = set.split(",")
            for sada in sady_kostek:
                sada = sada.strip()
                cislo_a_barva = sada.split(" ")
                cislo = int(cislo_a_barva[0])
                barva = cislo_a_barva[1]
                
                if barva == "red":
                    red = cislo
                    if red > maximum_red:
                        vysledky.append("chyba")
                elif barva == "blue":
                    blue = cislo
                    if blue > maximum_blue:
                        vysledky.append("chyba")
                elif barva == "green":
                    green = cislo
                    if green > maximum_green:
                        vysledky.append("chyba")
        if not vysledky:    
            sum_IDs += ID
    print(sum_IDs)    
        