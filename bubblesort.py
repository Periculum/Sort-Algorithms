#!/usr/bin/env python3

liste = [2, 4, 6, 1, 3] 

for j in range(len(liste)): 
    for i in range(len(liste) - j - 1): 
        # tausche, wenn i größer i+1 ist 
        if liste[i] > liste[i+1]: 
            buffer = liste[i] 
            liste[i] = liste[i+1] 
            liste[i+1] = buffer 
        
print(liste)
