#!/usr/bin/env python3

liste = [1, 2, 3, 4, 5, 6]

for j in range(len(liste)):
	swap = False
	for i in range(len(liste) -j -1):
		# wenn i größer i+1 ist, dann tausche
		if liste[i] > liste[i+1]:
			liste[i], liste[i+1] = liste[i+1], liste[i]
			swap = True
	if not swap:
		break

print(liste)
