with open('advent_of_code_2023\\04\\04.txt', encoding='utf-8') as soubor:
    suma = 0
    for radek in soubor:
        radek = radek.strip()
        radek = radek.split(":")
        karta, numbers = radek
        numbers = numbers.split("|")
        winning_numbers, numbers_you_have = numbers
        winning_numbers = winning_numbers.replace("  ", " ")
        numbers_you_have = numbers_you_have.replace("  ", " ")
        winning_numbers = winning_numbers.split(" ")
        numbers_you_have = numbers_you_have.split(" ")
        match = []
        for number in winning_numbers:
            if number == "":
                continue
            if number in numbers_you_have:
                match.append(number)
                
        if match:
            prirustek = 1
            for i in range(len(match)):
                if i>0:
                    prirustek = prirustek * 2
            suma += prirustek
        print(karta)
        print(match)
    print(suma)