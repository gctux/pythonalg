def selectionsort(liste):
    # vom 1. Listenelement bis zum letzten
    for i in range(len(liste)):
        # Finde die Position des kleinsten Listenelements
        minpos = i
        # vom i+1. Listenelement bis zum letzten
        for j in range(i + 1, len(liste)):
            # Vergleichen der Werte
            if liste[j] < liste[minpos]:
                minpos = j  # Position merken
        # Tausche das minimale Listenelement mit dem untersten noch nicht sortierten Listenelement
        if minpos > i:
            liste[minpos], liste[i] = liste[i], liste[minpos]


liste = [5, 2, 4, 6, 1, 3]
selectionsort(liste)
print(liste)