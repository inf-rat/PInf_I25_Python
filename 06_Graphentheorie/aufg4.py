adj = {
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

print(adj)
