from collections import deque

G1 = {
    0: [1, 2, 3],
    1: [0, 3],
    2: [0, 3],
    3: [0, 1, 2, 4],
    4: [3],
}

G2 = {
    0: [1, 2, 3],
    1: [0, 4, 5],
    2: [0, 6],
    3: [0, 7],
    4: [1],
    5: [1],
    6: [2],
    7: [3],
}

eur_small = {
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

eur_full = {
    "A":   ["D", "CH", "I", "SLO", "H", "CZ", "SK"],              # Österreich
    "AL":  ["MNE", "XK", "MK", "GR"],                             # Albanien
    "AND": ["F", "E"],                                            # Andorra
    "B":   ["F", "L", "D", "NL"],                                 # Belgien
    "BIH": ["HR", "MNE", "SRB"],                                  # Bosnien und Herzegowina
    "BG":  ["RO", "SRB", "MK", "GR", "TR"],                       # Bulgarien
    "BY":  ["LT", "LV", "PL", "RUS", "UA"],                       # Weißrussland
    "CH":  ["F", "D", "I", "A", "FL"],                            # Schweiz
    "CZ":  ["D", "PL", "SK", "A"],                                # Tschechien
    "D":   ["DK", "NL", "B", "L", "F", "CH", "A", "CZ", "PL"],    # Deutschland
    "DK":  ["D"],                                                 # Dänemark
    "E":   ["P", "F", "AND"],                                     # Spanien
    "EST": ["LV", "RUS"],                                         # Estland
    "F":   ["B", "L", "D", "CH", "I", "AND", "E", "MC"],          # Frankreich
    "FIN": ["S", "N", "RUS"],                                     # Finnland
    "FL":  ["CH", "A"],                                           # Liechtenstein
    "GB":  ["IRL"],                                               # Vereinigtes Königreich
    "GR":  ["AL", "MK", "BG", "TR"],                              # Griechenland
    "H":   ["A", "SK", "UA", "RO", "SRB", "HR", "SLO"],           # Ungarn
    "HR":  ["SLO", "H", "SRB", "BIH", "MNE"],                     # Kroatien
    "I":   ["F", "CH", "A", "SLO", "SM", "V"],                    # Italien
    "IRL": ["GB"],                                                # Irland
    "IS":  [],                                                    # Island
    "KZ":  [],                                                    # Kasachstan (kein Nachbar innerhalb Europas)
    "LT":  ["LV", "BY", "PL", "RUS"],                             # Litauen
    "L":   ["B", "F", "D"],                                       # Luxemburg
    "LV":  ["EST", "RUS", "BY", "LT"],                            # Lettland
    "M":   [],                                                    # Malta
    "MC":  ["F"],                                                 # Monaco
    "MD":  ["UA", "RO"],                                          # Moldau
    "MK":  ["SRB", "XK", "AL", "GR", "BG"],                       # Nordmazedonien
    "MNE": ["HR", "BIH", "SRB", "XK", "AL"],                      # Montenegro
    "N":   ["S", "FIN", "RUS"],                                   # Norwegen
    "NL":  ["B", "D"],                                            # Niederlande
    "P":   ["E"],                                                 # Portugal
    "PL":  ["D", "CZ", "SK", "UA", "BY", "LT", "RUS"],            # Polen
    "RO":  ["UA", "MD", "BG", "SRB", "H"],                        # Rumänien
    "RUS": ["FIN", "EST", "LV", "LT", "PL", "BY", "UA"],          # Russland
    "S":   ["N", "FIN"],                                          # Schweden
    "SK":  ["CZ", "PL", "UA", "H", "A"],                          # Slowakei
    "SLO": ["I", "A", "H", "HR"],                                 # Slowenien
    "SM":  ["I"],                                                 # San Marino
    "SRB": ["H", "RO", "BG", "MK", "XK", "MNE", "BIH", "HR"],     # Serbien
    "TR":  ["GR", "BG"],                                          # Türkei (nur europ. Teil)
    "UA":  ["PL", "SK", "H", "RO", "MD", "RUS", "BY"],            # Ukraine
    "V":   ["I"],                                                 # Vatikanstadt
    "XK":  ["MNE", "AL", "MK", "SRB"]                             # Kosovo
}


def finde_weg(graph, start, end):
    queue = deque([(start, None)])
    visited = {}
    while queue:
        node, came_from = queue.popleft()
        if node not in visited:
            visited[node] = came_from
            if node == end:
                path = deque([])
                cur = end
                while cur is not None:
                    path.appendleft(cur)
                    cur = visited[cur]
                return list(path)
            for nb in graph[node]:
                if nb not in visited:
                    queue.append((nb, node))
    return None

print(finde_weg(G1, 0, 4))
print(finde_weg(eur_small, "D", "SLO"))
print(finde_weg(eur_full, "EST", "P"))