"""
Insertionsort

Bei insertionsort1 wird die Zahl an die richtige Stelle getauscht.

Bei insertionsort2 wird die werden alle zu großen Zahlen nach "rechts" verschoben.
Wenn die Einfügeposition gefunden wird, wird die Zahl angefügt.

"""
def insertionsort1(liste):
    # vom 2. Listenelement bis zum letzten
    for i in range(1, len(liste)):
        # j ergibt sich aus dem aktuellen Index
        j = i
        # solange j > 0 und der Wert von j - 1 kleiner als der Wert von j ist
        while j > 0 and liste[j - 1] > liste[j]:
            # Tausche die Werte
            liste[j - 1], liste[j] = liste[j], liste[j - 1]
            # Vermindere j um 1
            j -= 1

def insertionsort2(liste):
    # vom 2. Listenelement bis zum letzten: Füge die i-te Zahl ei
    for i in range(1, len(liste)):
        # Zwischenspeichern der einzufügenden Zahl
        key = liste[i]
        j = i
        # Suchen der Einfügeposition
        while j > 0 and liste[j - 1] > key:
            # Verschieben der zu großen Zahl nach rechts
            liste[j] = liste[j - 1]
            j -= 1
        # neue Zahl einfügen
        liste[j] = key


liste1 = [5, 2, 4, 6, 1, 3]
insertionsort1(liste1)
print(liste1)

liste2 = [5, 2, 4, 6, 1, 3]
insertionsort2(liste2)
print(liste2)