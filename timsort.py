#!/usr/bin/env python3
import random

def binary_search(a, l, r, num):
    while l <= r:
        m = (l + r) // 2
        if  a[m] == num:
            return m # Position gefunden

        if a[m] > num:
            # in linke Teilhälfte weitersuchen
            r = m - 1
        else:
            # in rechte Teilhälfte weitersuchen
            l = m + 1

    return l # Einfügeposition


def insertionsort(a, l, r):
    for i in range(l, r):
        num = a[i]

        # Einfügeposition finden
        pos = binary_search(a, l, i - 1, num)

        # Elemente nach rechts verschieben
        j = i
        while j > pos:
            a[j] = a[j - 1]
            j -= 1
    
        # `num` an korrekte Stelle einsetzen
        a[pos] = num


def merge(arr, start, mid, end):
    # nur den Teil kopieren, der gemischt werden soll
    left = arr[start:mid]
    right = arr[mid:end]

    i = 0  # Index für linke Teilhälfte
    j = 0  # Index für rechte Teilhälfte
    k = start # Schreib-Index für das Original-Array

    # immer den kleineren Wert aus beiden Listen hinzufügen
    # solange beide Listen nicht leer sind
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Reste kopieren (falls vorhanden)
    arr[k:end] = left[i:] or right[j:]


def calc_minrun(n):
    # von pypy übernommen
    # berechnet die beste Größe von minrun für Timsort
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r


def find_run(a, l):
    n = len(a)
    descending = False
    # der Run wird beendet,
    # falls letztes Element erreicht ist
    if l == n - 1:
        return 1, False

    # True, wenn Liste absteigend
    if a[l + 1] < a[l]:
        descending = True

    # Elemente zählen
    i = l # Startindex
    if descending:
        while i + 1 < n and a[i] > a[i + 1]:
            i += 1 # absteigend
    else:
        while i + 1 < n and a[i] <= a[i + 1]:
            i += 1 # aufsteigend

    return i - l + 1, descending


def timsort(a):
    n = len(a)

    # wenn array kleiner als 64, 
    # dann nur Binary-Insertionsort verwenden
    if n < 64:
        insertionsort(a, 0, n)
        return a

    # minimale Länge eines Runs festlegen
    min_run_length = calc_minrun(n)

    # Run durchführen
    runs = []
    i = 0 # Startindex
    while i < n:
        # Länge und Orientierung des nächsten Runs abfragen
        run_len, descending = find_run(a, i)

        # absteigenden Run umdrehen
        if descending:
            a[i:i + run_len] = reversed(a[i:i + run_len])

        # Run auf Länge von minrun verlängern
        if run_len < min_run_length:
            elements_left = min(min_run_length, n - i)
            insertionsort(a, i, i + elements_left)
            run_len = elements_left

        runs.append((i, run_len))
        i += run_len

    # Runs zusammenführen
    while len(runs) > 1:
        new_runs = []

        # run[i] mit run[i+1] mergen
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                l1, len1 = runs[i]      # erster Run
                l2, len2 = runs[i + 1]  # zweiter Run

                # benachbarte Runs mergen
                merge(a, l1, l2, l2 + len2)

                # neuen Run festlegen
                new_runs.append((l1, len1 + len2))
            else:
                # ungerader Run bleibt übrig
                new_runs.append(runs[i])

        # alten Run durch neu zusammengeführte ersetzen
        runs = new_runs

    return a


def main():
    # teste timsort für kleine Listen unter 64
    # test1 = [2, 4, 6, 1, 3, 3, 4, 5, 3, 99, 12, 13, 14, 18, 33, 32, 31, 30, 29, 28]
    # print(timsort(test1))

    # teste Timsort
    test2 = zahlen = [random.randint(0, 10000) for _ in range(2112)]
    print(timsort(test2))

if __name__ == '__main__':
    main()
