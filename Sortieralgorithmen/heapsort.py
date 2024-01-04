def heapsort(liste):
    createheap(liste)
    for i in range(len(liste) - 1, 0, -1):
        liste[0], liste[i] = liste[i], liste[0]
        shiftdown(liste, i, 0)


def shiftdown(liste, size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < size and liste[largest] < liste[left]:
        largest = left
    if right < size and liste[largest] < liste[right]:
        largest = right
    if largest != i:
        liste[i], liste[largest] = liste[largest], liste[i]
        shiftdown(liste, size, largest)


def createheap(liste):
    for i in range(len(liste) // 2 - 1, -1, -1):
        shiftdown(liste, len(liste), i)


liste = [5, 3, 7, 9, 1, 4, 2, 8, 6]
heapsort(liste)
print(liste)
