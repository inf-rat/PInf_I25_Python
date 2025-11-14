G1 = {
    0: [1, 2, 3],
    1: [0, 4, 5],
    2: [0, 6],
    3: [0, 7],
    4: [1],
    5: [1],
    6: [2],
    7: [3],
}

G2 = {
    0: [1, 2, 3],
    1: [0, 3],
    2: [0, 3],
    3: [0, 1, 2, 4],
    4: [3],
}

G3 = {
    "DK":     ["D"],
    "D":      ["DK", "NL", "B", "L", "F", "CH", "A", "CZ"],
    "NL":     ["D", "B"],
    "B":      ["D", "NL", "F", "L"],
    "L":      ["D", "B", "F"],
    "F":      ["D", "B", "L", "CH"],
    "CH":     ["D", "F", "FL", "A"],
    "FL":     ["CH", "A"],
    "SLO":    ["A"],
    "A":      ["D", "FL", "SLO", "CZ"],
    "CZ":     ["D", "A"],
    "IRL":    ["UK"],
    "UK":     ["IRL"],
}

def BFS(G, v):
    visited = set()
    queue = [v]
    while len(queue) > 0:
        v = queue.pop(0)
        if not v in visited:
            print(v)
            visited.add(v)
            for w in G[v]:
                if not w in visited:
                    queue.append(w)

def breitensuche(graph, start):
    visited = set()
    queue = [start]
    while queue != []:
        start = queue.pop(0)
        if not start in visited:
            print(start)
            visited.add(start)
            for neibor in graph[start]:
                queue.append(neibor)


breitensuche(G3, "D")