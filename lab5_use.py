import heapq

def find_time(n, m, k, c, cities, roads):
    dist = [float('inf')] * n
    dist[c-1] = 0
    
    pq = [(0, c-1)]
    
    graph = [[] for _ in range(n)]
    for u, v, t in roads:
        graph[u-1].append((v-1, t))
        graph[v-1].append((u-1, t))
        
    while pq:
        current_dist, node = heapq.heappop(pq)
        
        if current_dist > dist[node]:
            continue
            
        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
                
    result = []
    for city in cities:
        result.append((city, dist[city-1]))
        
    return sorted(result, key=lambda x: x[1])

print("Введите количество населённых пунктов, количество дорог, количество городов и номер столицы через пробел:")
n, m, k, c = map(int, input().split())
print("Введите номера городов через пробел:")
cities = list(map(int, input().split()))
print("Введите через пробел номера населённых пунктов, которые соединяет дорога, и время для проезда по ней:")
roads = [tuple(map(int, input().split())) for _ in range(m)]

result = find_time(n, m, k, c, cities, roads)
print("Номер города и минимальное время прибытия машины:")
for city, time in result:
    print(city, time)