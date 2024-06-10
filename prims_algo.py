# Prims algorithms.

def prims_algo(s, start, n, prim):
    visited = []
    visited.append(start)
    while len(visited) < n:
        min = 999
        for i in visited:
            for j in range(n):
                if s[i][j] < min and j not in visited:
                    min = s[i][j]
                    visited.append(j) 
                    prim[i][j] = s[i][j]
                    prim[j][i] = s[i][j]
    return prim

start = 0
end = 3


n = int(input("Enter the number of nodes : "))
s = []
for i in range(n):
    s.append(list(map(int, input("Enter the matrix elements separated by spaces : ").split())))
start = int(input())
prim = [[0 for i in range(n)] for j in range(n)]
print(prims_algo(s, start, n, prim))
