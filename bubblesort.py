#!/usr/bin/env python3

liste = [2, 4, 6, 1, 3]

for j in range(len(liste)):
	for i in range(len(liste) -j -1):
		# wenn i größer i+1 ist, dann tausche
		if liste[i] > liste[i+1]:
			liste[i], liste[i+1] = liste[i+1], liste[i]

print(liste)
