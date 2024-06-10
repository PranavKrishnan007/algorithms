# Kruskal's algorithm.

def kruskals_algo(s, n):
    visited = []
    visited.append(0)
    while len(visited) < n:
        min = 999
        for i in visited:
            for j in range(n):
                if s[i][j] < min and j not in visited:
                    min = s[i][j]
                    visited.append(j)
                    prim[i][j] = s[i][j]
                    prim[j][i] = s[i][j]
    return (prim, visited)


n = int(input("Enter the number of nodes : "))

s = [[int(input("Enter the matrix elements separated by spaces : ").split()) for i in range(n)] for j in range(n)]
prim = [[0 for i in range(n)] for j in range(n)]
print(kruskals_algo(s, n))
