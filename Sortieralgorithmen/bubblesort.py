"""
In Bubblesort werden immer zwei beachbarte Listenelemente verglichen und, wenn notwendig, das kleinere nach links
getauscht.

Bei bubblesort1 wird die Folge so oft durchlaufen, bis keine Vertauschungen mehr notwendig sind.

Bei bublesort2 laufen zwei ineinander geschachtelte for-Schleifen, wobei die innere bei jedem Durchlauf um ein Element
verringert wird.

Bei bubblessort3 werden beide Techniken kombiniert.
"""

def bubblesort1(liste):
    swap = True
    while swap:
        swap = False
        # von hinten zum vorne
        for i in range(1,len(liste)):
            # Vergleichen der Werte
            if liste[i] < liste[i - 1]:
                # Tausche die Werte
                liste[i], liste[i - 1] = liste[i - 1], liste[i]
                swap = True


def bubblesort2(liste):
    # von hinten zum vorne
    for i in range(len(liste) - 1, 0, -1):
        # von hinten zum vorne
        for j in range(i):
            # Vergleichen der Werte
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]



def bubblesort3(liste):
    swap = True
    while swap:
        swap = False
        # von hinten zum vorne
        for i in range(len(liste) - 1, 0, -1):
            # Vergleichen der Werte
            if liste[i] < liste[i - 1]:
                # Tausche die Werte
                liste[i], liste[i - 1] = liste[i - 1], liste[i]
                swap = True


liste1 = [7, 3, 6, 1, 8, 2, 5, 4]
bubblesort1(liste1)
print(liste1)

liste2 = [7, 3, 6, 1, 8, 2, 5, 4]
bubblesort2(liste2)
print(liste2)

liste3 = [7, 3, 6, 1, 8, 2, 5, 4]
bubblesort3(liste3)
print(liste3)
