import heapq

def duongdingannhat(dothi, start, end):
   
    distances = {vertex: float('inf') for vertex in dothi}
    distances[start] = 0

   
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

       
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in dothi[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))


    duongngannhat = []
    current_vertex = end
    while current_vertex != start:
        duongngannhat.insert(0, current_vertex)
        current_vertex = min(dothi[current_vertex], key=lambda vertex: distances[vertex] + dothi[current_vertex][vertex])
    
    duongngannhat.insert(0, start)
    return duongngannhat, distances[end]

# Ví dụ sử dụng
dothi = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
end_vertex = 'D'

duongngannhat = duongdingannhat(dothi, start_vertex, end_vertex)
print("Đường đi ngắn nhất:", duongngannhat)


