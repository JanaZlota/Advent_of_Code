def extract_numbers(radek):
    extracted = ""
    i = 0
    for symbol in radek:
        if symbol in "123456789":
            extracted += symbol
        elif symbol == "o":            
            if radek[i:i+3] == "one":
                extracted += "1"
        elif symbol == "t":
            if radek[i:i+3] == "two":
                extracted += "2"
            elif radek[i:i+5] == "three":
                extracted += "3"
        elif symbol == "f":
            if radek[i:i+4] == "four":
                extracted += "4"
            elif radek[i:i+4] == "five":
                extracted += "5"
        elif symbol == "s":
            if radek[i:i+3] == "six":
                extracted += "6"
            elif radek[i:i+5] == "seven":
                extracted += "7"
        elif symbol == "e":
            if radek[i:i+5] == "eight":
                extracted += "8"
        elif symbol == "n":
            if radek[i:i+4] == "nine":
                extracted += "9"
        i += 1
        
    return extracted

soucet = 0
with open('advent_of_code_2023\\01\\01.txt', encoding='utf-8') as soubor:
    
    for radek in soubor: 
        extracted = extract_numbers(radek)            
        dvojcifra = int(extracted[0] + extracted[-1])            
        soucet += dvojcifra

    print(soucet)
        

