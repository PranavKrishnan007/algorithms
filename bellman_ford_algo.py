# Implementing Bellman Ford Algorithm

import numpy as np

s = [
    [999, 10 , 999, 999, 999, 8],
    [999, 999, 999, 2, 999, 999],
    [999, 1, 999, 999, 999, 999],
    [999, 999, -2, 999, 999, 999],
    [999, -4, 999, -1, 999, 999],
    [999, 999, 999, 999, 1, 999] 
    ]

def bellman_ford_algo(s, start, n):
    distance = [999 for i in range(n)]
    check_val = [999 for i in range(n)]
    distance[start] = 0
    while distance != check_val:
        check_val = [i for i in distance]
        for i in range(n):
            current_distance = distance[i]
            for j in range(n):
                if s[i][j] != 999:
                    if distance[j] > current_distance + s[i][j]:
                        distance[j] = current_distance + s[i][j]
        

    return distance

start = 0
n = 6
print(bellman_ford_algo(s, start, n))