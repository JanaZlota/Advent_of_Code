with open("advent_of_code_2023\\08\\08.txt", encoding="utf-8") as soubor:
    data=soubor.readlines()
    instrukce=data[0].strip()
    mapa=data[2:]   
    instrukce=list(instrukce)

    slovnik={}
    for radek in mapa:
        radek=radek.strip()
        radek=radek.split(" = (")
        puvodni, novy = radek
        novy=novy[:-1]
        novy=novy.split(", ")
        
        slovnik[puvodni]=novy
    print(slovnik)
    
    step = 0
    dalsi = "AAA"
    while dalsi != "ZZZ":
        for i in instrukce:            
            if i == "L":
                dalsi = slovnik[dalsi][0]                 
                step += 1    
            elif i == "R":
                dalsi = slovnik[dalsi][1]                 
                step += 1

    print("step", step)
            

