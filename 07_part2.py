from collections import Counter   

with open ("advent_of_code_2023\\07\\07.txt", encoding="utf-8") as soubor:
    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []
    soubor = soubor.readlines()

    for radek in soubor:
        radek = radek.strip()
        radek = radek.split(" ")        
        hand, bit = radek
        puvodni_hand = hand
        puvodni_hand = list(hand) # nahrad znaky za cisla
        for index, znak in enumerate(puvodni_hand[:]):
            if znak == "A":
                puvodni_hand[index]=14
            elif znak == "K":
                puvodni_hand[index]=13
            elif znak == "Q":
                puvodni_hand[index]=12
            elif znak == "J":
                puvodni_hand[index]=1
            elif znak == "T":
                puvodni_hand[index]=10
            else:
                puvodni_hand[index]=int(znak)
        puvodni_hand = tuple(puvodni_hand)
        
        if "J" in hand:             
            c = Counter(hand) 
            hand = list(hand)               
            s_most_common=c.most_common()   #Counter('T55JT').most_common()          
            if len(s_most_common)==1:       #[('5', 2), ('T', 2), ('J', 1)]
                    nejpocetnejsi="A" 
            else:         
                for key, value in s_most_common:         
                    if key=="J":
                        continue
                    else:
                        nejpocetnejsi=key
                        break

            for index, znak in enumerate(hand[:]): # nahrad J za nejpocetnejsi znak
                if znak == "J":
                    hand[index]=nejpocetnejsi
            hand = "".join(hand) 
            
        c = Counter(hand)        
        hand = list(hand) # nahrad znaky za cisla
        for index, znak in enumerate(hand[:]):
            if znak == "A":
                hand[index]=14
            elif znak == "K":
                hand[index]=13
            elif znak == "Q":
                hand[index]=12         
            elif znak == "T":
                hand[index]=10
            elif znak in "23456789":
                hand[index]=int(znak)                          

        hand = tuple(hand)
        bit = int(bit)            
        seznam_values = []     # pro zarazeni do kategorie   
        for key, value in c.most_common():
            seznam_values.append(value)                
        s_v_sorted = sorted(seznam_values, reverse=True)
        
        if s_v_sorted[0]==5:            
            five_of_a_kind.append((puvodni_hand, bit))            
        elif s_v_sorted[0]==4:            
            four_of_a_kind.append((puvodni_hand, bit))            
        elif s_v_sorted[0]==3 and s_v_sorted[1]==2:
            full_house.append((puvodni_hand, bit))            
        elif s_v_sorted[0]==3 and s_v_sorted[1]==1:
            three_of_a_kind.append((puvodni_hand, bit))           
        elif s_v_sorted[0]==2 and s_v_sorted[1]==2:
            two_pair.append((puvodni_hand, bit))            
        elif s_v_sorted[0]==2 and s_v_sorted[1]==1:
            one_pair.append((puvodni_hand, bit))            
        else:
            high_card.append((puvodni_hand, bit))           

    suma = 0
    rank = 1

    if high_card:
        high_card = sorted(high_card)   
        for karty, bit in high_card:
            suma += bit*rank
            rank += 1
            
    if one_pair:
        one_pair = sorted(one_pair)      
        for karty, bit in one_pair:
            suma += bit*rank
            rank += 1

    if two_pair:
        two_pair = sorted(two_pair)       
        for karty, bit in two_pair:
            suma += bit*rank
            rank += 1

    if three_of_a_kind:
        three_of_a_kind = sorted(three_of_a_kind)     
        for karty, bit in three_of_a_kind:
            suma += bit*rank
            rank += 1

    if full_house:
        full_house = sorted(full_house)    
        for karty, bit in full_house:
            suma += bit*rank
            rank += 1

    if four_of_a_kind:
        four_of_a_kind = sorted(four_of_a_kind)    
        for karty, bit in four_of_a_kind:
                suma += bit*rank
                rank += 1

    if five_of_a_kind:
        five_of_a_kind = sorted(five_of_a_kind)     
        for karty, bit in five_of_a_kind:
            suma += bit*rank
            rank += 1    

    print("suma", suma)   
        
        
