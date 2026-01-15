#!/usr/bin/env python3


def quicksort(a, l, r):
	# rufe quicksort rekursiv auf, bis a sortiert ist
	if l < r:
		pos = partition(a, l, r)
		# linke Hälfte rekursiv lösen
		quicksort(a, l, pos - 1)
		# rechte Hälfte rekursiv lösen
		quicksort(a, pos + 1, r)


def partition(a, l, r):
	# Pivot-Element ganz rechts setzen
	pivot = a[r]

	# Zeiger i ganz links
	# Zeiger j links neben Pivot
	i = l
	j = r - 1

	# loop, bis i und j sich treffen
	# i läuft von links nach rechts, j von rechts nach links
	while i < j:
		# suche von links eine Zahl, die größer als pivot ist
		while i < r and a[i] < pivot:
			i += 1

		# suche von rechts eine Zahl, die wirklich kleiner als pivot ist
		while j > l and a[j] >= pivot:
			j -= 1

		# tausche i mit j
		if i < j:
			a[i], a[j] = a[j], a[i]

	# Sicherung: tausche nur, wenn pivot tatsächlich kleiner ist
	if a[i] > pivot:
		# setze Pivot von ganz rechts an seinen neuen Platz
		a[i], a[r] = a[r], a[i]

	# gebe neue Trennungsposition zurück
	return i
	

def main():
	a = [2, 4, 6, 1, 3]
	quicksort(a, 0, len(a) - 1)
	print(a)


if __name__ == "__main__":
    main()
