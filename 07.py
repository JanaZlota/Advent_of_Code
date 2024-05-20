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
        hand = list(hand) # nahrad znaky za cisla
        for index, znak in enumerate(hand[:]):
            if znak == "A":
                hand[index]=14
            elif znak == "K":
                hand[index]=13
            elif znak == "Q":
                hand[index]=12
            elif znak == "J":
                hand[index]=11
            elif znak == "T":
                hand[index]=10
            else:
                hand[index]=int(znak)

        hand = tuple(hand)
        bit = int(bit)
        c = Counter(hand)
        seznam_values = []
     
        for key, value in c.most_common():
            seznam_values.append(value)
            
        s_v_sorted = sorted(seznam_values, reverse=True)
        
        if s_v_sorted[0]==5:            
            five_of_a_kind.append((hand, bit))            
        elif s_v_sorted[0]==4:            
            four_of_a_kind.append((hand, bit))            
        elif s_v_sorted[0]==3 and s_v_sorted[1]==2:
            full_house.append((hand, bit))            
        elif s_v_sorted[0]==3 and s_v_sorted[1]==1:
            three_of_a_kind.append((hand, bit))           
        elif s_v_sorted[0]==2 and s_v_sorted[1]==2:
            two_pair.append((hand, bit))            
        elif s_v_sorted[0]==2 and s_v_sorted[1]==1:
            one_pair.append((hand, bit))            
        else:
            high_card.append((hand, bit))           

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
        
        
        
