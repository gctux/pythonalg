def quicksort(liste, l, r):
    if l < r:
        # Wähle ein Pivotelement aus der Liste und ordne die Elemente am Pivotelement
        p = partition(liste, l, r)
        # Rufe Quicksort für die untere und obere Teilliste auf
        quicksort(liste, l, p - 1)
        quicksort(liste, p + 1, r)


def partition(liste, l, r):
    # Wähle
    pivot = liste[r]
    i = l
    # Ordne die Elemente am Pivotelement 
    for j in range(l, r):
        if liste[j] <= pivot:
            liste[i], liste[j] = liste[j], liste[i]
            i += 1
    liste[i], liste[r] = liste[r], liste[i]
    return i


liste = [3, 2, 1, 5, 4, 6, 9, 8, 7]
quicksort(liste, 0, len(liste) - 1)
print(liste)