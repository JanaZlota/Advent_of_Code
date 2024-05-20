suma_power = 0
with open('advent_of_code_2023\\02\\02.txt', encoding='utf-8', mode="r") as soubor:
    for radek in soubor:
        radek = radek.strip()
        pozice_1 = radek.index(" ")
        pozice_2 = radek.index(":")
        ID = int(radek[pozice_1:pozice_2].strip())
        osekany_radek = radek[pozice_2+1:]
        jednotlive_sety = osekany_radek.split(";")
        minimum_red = 0
        minimum_blue = 0
        minimum_green = 0
        for set in jednotlive_sety:
            sady_kostek = set.split(",")
            for sada in sady_kostek:
                sada = sada.strip()
                cislo_a_barva = sada.split(" ")
                cislo = int(cislo_a_barva[0])
                barva = cislo_a_barva[1]
                
                if barva == "red":
                    red = cislo
                    if red > minimum_red:
                        minimum_red = red
                elif barva == "blue":
                    blue = cislo
                    if blue > minimum_blue:
                        minimum_blue = blue
                elif barva == "green":
                    green = cislo
                    if green > minimum_green:
                        minimum_green = green
        power = minimum_blue * minimum_green * minimum_red
        print(power)    
        suma_power += power
    print(f"suma {suma_power}")