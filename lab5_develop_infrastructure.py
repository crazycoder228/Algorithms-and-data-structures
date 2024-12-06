def find_min_distance_center(N, edges):
    INF = float('inf')
    distance = [[INF] * N for _ in range(N)]
    
    for i in range(N):
        distance[i][i] = 0
    
    for u, v, w in edges:
        distance[u-1][v-1] = w
        distance[v-1][u-1] = w
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    min_sum = INF
    center = None
    for i in range(N):
        sum_distances = sum(distance[i])
        if sum_distances < min_sum:
            min_sum = sum_distances
            center = i + 1
    
    return center

print("Введите через пробел количество площадок и дорог:")
N, M = map(int, input().split())
print("Введите через пробел площадки начала и конца дороги, и её длину:")
edges = [tuple(map(int, input().split())) for _ in range(M)]
print("Лучшая площадка для строительства школы:\n", find_min_distance_center(N, edges))