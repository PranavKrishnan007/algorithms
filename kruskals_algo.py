# Kruskal's Algorithm

def kruskals_algo(s, n):
    visited = []
    visited.append(0)
    while len(visited) < n:
        min_val = 999
        for i in visited:
            for j in range(n):
                if s[i][j] < min_val and j not in visited:
                    min_val = s[i][j]
                    visited.append(j)
                    prim[i][j] = s[i][j]
                    prim[j][i] = s[i][j]
    return (prim, visited)

n = int(input("Enter the number of nodes: "))

s = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    row = list(map(int, input(f"Enter the matrix elements separated by spaces for node {i}: ").split()))
    for j in range(n):
        s[i][j] = row[j]

prim = [[0 for i in range(n)] for j in range(n)]

result, visited = kruskals_algo(s, n)
print(result)
