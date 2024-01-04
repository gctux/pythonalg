# Aufruf von mergesort für eine Teilliste
def mergesort(liste,l,r):
    if l < r:
        # Finde den mittleren Index
        m = (l+r)//2
        # Rufe Mergesort für die untere Teilliste auf
        mergesort(liste,l,m)
        # Rufe Mergesort für die obere Teilliste auf
        mergesort(liste,m+1,r)
        # Mische die
        merge(liste,l,m,r)
    return liste


def merge(liste,l,m,r):
    temp = []
    i = l
    j = m+1
    # Mischen der Teillisten
    while i <= m and j <= r:
        if liste[i] < liste[j]:
            temp.append(liste[i])
            i += 1
        else:
            temp.append(liste[j])
            j += 1
    while i <= m:
        temp.append(liste[i])
        i += 1
    while j <= r:
        temp.append(liste[j])
        j += 1
    for i in range(l,r+1):
        liste[i] = temp[i-l]


liste = [12, 11, 13, 5, 6, 7]
mergesort(liste,0,len(liste)-1)
print(liste)