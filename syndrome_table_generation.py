import numpy as np
import itertools

g = np.array([[1, 0, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1], [0, 0, 1, 1, 1, 0]])
r = np.array([[1, 1, 1, 1, 0, 1]])
# 1 1 1 1 0 1

# g = [i:p] then h = [pt:i]

def h_matrix(g):
    n = g.shape[1]
    k = g.shape[0]
    i = np.eye(k)
    p = g[:, k:]
    pt = p.T
    h = np.append(pt, i, axis=1)
    return h

k = g.shape[0]
n = g.shape[1]
s = [np.array(i) for i in itertools.product([0, 1], repeat=k)]

# for checking if the error exists or not.
def check_if_error(g, s, r):
    table = [[i.dot(g) for i in s]]
    # print(table)
    if any(np.allclose(i, r) for i in table):
        print("No Error")
    else:
        print("Error Exists")
    return

check_if_error(g, s, r)


# for making the syndromes
check_array = []
some = []
h = h_matrix(g)

for i in range(n):
    some.append(0)

check_array.append(some.copy())

for i in range(n):
    some[i] = 1
    check_array.append(some.copy()) 
    some[i] = 0

print("this is the check_array : ", check_array)

print(h.T)
something = []

for i in range(len(check_array)):
    # print(check_array[i])
    val = np.array(check_array[i]).dot(h.T)
    something.append(val)

print(something)


# final stint 
final = r.dot(h.T) %2

print(final)

index = 0

for i in range(len(something)):
    if np.allclose(something[i], final):
        index = i
        break

# print(something[index], index)
print("corresponding corset : ", check_array[index])
print("the received vector : ", r[0])
codeword = np.subtract(r[0], check_array[index])
print("The final codeword is : ", codeword)
