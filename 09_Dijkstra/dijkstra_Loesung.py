import heapq

graph = {
    'A': [('B', 3), ('C', 6)],
    'B': [('A', 3), ('C', 2), ('D', 8)],
    'C': [('A', 6), ('B', 2), ('D', 3)],
    'D': [('B', 8), ('C', 3)],
 }

def dijkstra(graph, start):
    distances = {node: (float('inf'), None) for node in graph}
    distances[start] = (0, None)

    # Die Warteschlange enthält den Startknoten mit Distanz 0
    priority_queue = [(0, start)]

    while priority_queue:
        # Hole den Knoten mit der kürzesten Distanz aus der Warteschlange
        current_distance, current_node = heapq.heappop(priority_queue)

        # Überspringe den Knoten, falls die Distanz länger ist
        # als die bisherige Distanz der Tabelle
        old_distance, came_from = distances[current_node]
        if current_distance > old_distance:
            continue

        # Berechne für alle Nachbarn die neue Distanz zu A
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Falls die neue Distanz kürzer ist als die bisherige:
            # aktualisiere die Tabelle
            # und reihe die Nachbarn in der Warteschlange ein
            old_distance, _ = distances[neighbor]
            if distance < old_distance:
                distances[neighbor] = (distance, current_node)
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

print(dijkstra(graph, 'A'))