#!/usr/bin/env python3

def merge(arr, start, mid, end):
    # nur den Teil kopieren, der gemischt werden soll
    left = arr[start:mid]
    right = arr[mid:end]

    i = 0  # Index für linke Teilhälfte
    j = 0  # Index für rechte Teilhälfte
    k = start # Schreib-Index für das Original-Array

    # füge immer den kleineren Wert aus beiden Listen neu hinzu
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


def mergesort_recursive(arr, start, end):
    # wenn Liste einzahlig, dann fertig
    if end - start <= 1:
        return

    # splitte Liste rekursiv
    mid = (start + end) // 2
    a1 = mergesort_recursive(arr, start, mid)
    a2 = mergesort_recursive(arr, mid, end)

    # verschmelze zwei Listen
    merge(arr, start, mid, end)

def mergesort(arr):
    # Wrapper-Funktion
    mergesort_recursive(arr, 0, len(arr))
    return arr

def main():
    array = [2, 4, 6, 1, 3, 3, 4, 5, 3, 99]
    print(mergesort(array))

if __name__ == '__main__':
    main()
