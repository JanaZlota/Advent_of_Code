def najdi_nejmensi(seznam):
    nejmensi = seznam[0]
    for i in seznam[1:]:
        if i < nejmensi:
            nejmensi = i
    return nejmensi

def zpracuj_data(soubor):
    seznam = []
    data = soubor.read()
    data = data.split("seed-to-soil map:")
    seeds, retezec = data
    seeds = seeds.strip()
    seeds = seeds.split(":")
    seeds, cisla = seeds
    cisla = cisla.strip()
    seeds = cisla.split(" ")
    for index, i in enumerate(seeds[:]):
        seeds[index] = int(i)
    #print(seeds)
    retezec = retezec.split("soil-to-fertilizer map:")
    seed_to_soil, zbytek = retezec 
    seznam.append(seed_to_soil)    

    zbytek = zbytek.split("fertilizer-to-water map:")
    soil_to_fertilizer, zbytek = zbytek
    seznam.append(soil_to_fertilizer)

    zbytek = zbytek.split("water-to-light map:")
    fertilizer_to_water, zbytek = zbytek
    seznam.append(fertilizer_to_water)

    zbytek = zbytek.split("light-to-temperature map:")
    water_to_light, zbytek = zbytek
    seznam.append(water_to_light)

    zbytek = zbytek.split("temperature-to-humidity map:")
    light_to_temperature, zbytek = zbytek
    seznam.append(light_to_temperature)

    zbytek = zbytek.split("humidity-to-location map:")
    temperature_to_humidity, zbytek = zbytek
    seznam.append(temperature_to_humidity)
    
    humidity_to_location = zbytek
    seznam.append(humidity_to_location)

    return seeds, seznam


def zpracuj_souradnice(souradnice, seeds):

    for index, seed in enumerate(seeds[:]):
        for polozka in souradnice:
            destination_start = polozka[0]
            source_start = polozka[1]
            range_lenght = polozka[2]
            zmena_cisla = source_start - destination_start    
            if seed in range(source_start, source_start + range_lenght +1):
                seeds[index] = seed - zmena_cisla
        
    return seeds  

def vytvor_souradnice(radek):    
    radek = radek.split("\n")
    souradnice = []
    for polozka in radek[:][1:]:
        if polozka == "":
            continue
        polozka = polozka.split(" ")
        for index, i in enumerate(polozka[:]):
            polozka[index] = int(i)
        souradnice.append(tuple(polozka))
    return souradnice

with open('advent_of_code_2023\\05\\05.txt', encoding='utf-8') as soubor:

    seeds, seznam = zpracuj_data(soubor)
    for i in seznam:
        souradnice = vytvor_souradnice(i)
        seeds = zpracuj_souradnice(souradnice, seeds)
    nejmensi = najdi_nejmensi(seeds)
    
    print(nejmensi)