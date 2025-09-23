#1C
G = {
    0: [1, 2, 3],
    1: [0, 4, 5],
    2: [0, 6],
    3: [0, 7],
    4: [1],
    5: [1],
    6: [2],
    7: [3],
}
K = {
    0: [1,3,2],
    1: [0,3],
    2: [0,3],
    3: [0,4],
    4: [3],
}

def Breitensuche(Graph, start):
    besucht = [start]
    Warteschlange = []
    Warteschlange += Graph[start]
    for i in Warteschlange:
        if besucht.count(i) > 0:
            pass
        else:
            besucht.append(i)
            Warteschlange += Graph[i]
    print(besucht)



Breitensuche(K, 0)
