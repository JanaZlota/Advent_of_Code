def extract_numbers(radek):
    extracted = ""
    i = 0
    for symbol in radek:
        if symbol in "123456789":
            extracted += symbol
        
    return extracted

soucet = 0
with open('advent_of_code_2023\\01\\01.txt', encoding='utf-8') as soubor:
    
    for radek in soubor: 
        extracted = extract_numbers(radek)            
        dvojcifra = int(extracted[0] + extracted[-1])            
        soucet += dvojcifra

    print(soucet)
        

