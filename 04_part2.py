def uprava_radku(numbers):
    numbers = numbers.split("|")
    winning_numbers, numbers_you_have = numbers
    winning_numbers = winning_numbers.replace("  ", " ")
    numbers_you_have = numbers_you_have.replace("  ", " ")
    winning_numbers = winning_numbers.split(" ")
    numbers_you_have = numbers_you_have.split(" ")
    match = []      
    """kolik nasledujicich radku se ma zkopirovat"""
    for number in winning_numbers:
        if number == "":
            continue
        if number in numbers_you_have:
            match.append(number)
        number_of_copies = len(match) 
    return number_of_copies

def vytvor_kopie(seznam_original, seznam_kopii, number_of_copies, cislo_karty):    
    kolikrat_karta = seznam_kopii.count(cislo_karty)
    kolikrat_karta += 1 #original
    #print(f"kolikrat mam tu kartu i s originalem: {kolikrat_karta}")
    for i in range(kolikrat_karta):
        for i in range(number_of_copies):            
                dalsi_karta = cislo_karty + 1 + i                   
                seznam_kopii.append(dalsi_karta)              
                #print(f"do seznamu kopii: {dalsi_karta}")
    return seznam_original, seznam_kopii

with open('advent_of_code_2023\\04\\04.txt', encoding='utf-8') as soubor:
    seznam_original = []
    seznam_kopii = []    
    for radek in soubor:        
        radek = radek.strip()
        radek = radek.split(":")
        karta, numbers = radek
        karta = karta.split(" ")     
        cislo_karty = karta[-1]
        cislo_karty = int(cislo_karty)
        print(cislo_karty) 

        number_of_copies = uprava_radku(numbers)
        
        #print(f"pocet nasledujicich radku: {number_of_copies}")
        seznam_original, seznam_kopii = vytvor_kopie(seznam_original, seznam_kopii, number_of_copies, cislo_karty)           
        seznam_original.append(cislo_karty) 
        #print(f"seznam original: {seznam_original}")        
        #print(f"seznam kopii {seznam_kopii}")      
        #print(50*"-")

    seznam = seznam_kopii + seznam_original
    print(len(seznam))               
