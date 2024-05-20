from math import lcm
from math import gcd

with open("advent_of_code_2023\\08\\08.txt", encoding="utf-8") as soubor:
    data=soubor.readlines()
    instrukce=data[0].strip()
    mapa=data[2:]   
    instrukce=list(instrukce)
    s_start=[]
    slovnik={}
    for radek in mapa:
        radek=radek.strip()
        radek=radek.split(" = (")
        puvodni, novy = radek
        if puvodni[-1]=="A":
            s_start.append(puvodni)
        novy=novy[:-1]
        novy=novy.split(", ")        
        slovnik[puvodni]=novy
    print(slovnik)  
    s_step=[]
    for start in s_start[:]:
        step = 0
        dalsi = start
        while dalsi[-1] != "Z":
            i=instrukce[step%len(instrukce)]            
            if i == "L":
                dalsi = slovnik[dalsi][0]                 
                step += 1                       
            elif i == "R":
                dalsi = slovnik[dalsi][1]                 
                step += 1
        s_step.append(step)       
    print(s_step)
    lcm = 1
    for i in s_step:
        lcm = lcm*i//gcd(lcm, i)
    print(lcm)

   
            

