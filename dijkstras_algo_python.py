n = input("Enter the number of nodes in the graph :")

n = int(n)

dijTable = {}

def initiate_dijTable(n, dijTable): 
    for x in range(n):
        dijTable[x] = {"visited": False, "distance": 9999, "prev": None}

def makeLookupTable(n):
    lookupTable = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                lookupTable[i][j] = 9999
            else:
                if lookupTable[i][j] != 0:
                    continue
                lookupTable[i][j] = int(input("Enter the distance between node " + str(i) + " and node " + str(j) + " :"))
                lookupTable[j][i] = lookupTable[i][j]

    print("The lookup table is :")
    for i in range(n):
        print(lookupTable[i])

    return lookupTable

count = 0

lookupTable = makeLookupTable(n)
initiate_dijTable(n=n, dijTable=dijTable)


start = input("Enter the starting node :")
end = input("Enter the ending node :")
start = int(start)
end = int(end)

path_distance = 0

dijTable[start]["distance"] = 0
dijTable[start]["visited"] = True

last_node = start
current_node = start

distance_tally = []

while (current_node != end):
    print("list of the nodes that are there : ", current_node, start, end, "\n")

    # minimum_value = min(lookupTable[current_node][:])
    # index_minimum_value = lookupTable[current_node][:].index(minimum_value)

    # dijTable[current_node]["distance"] = distance + minimum_value
    # dijTable[current_node]["prev"] = last_node
    # dijTable[current_node]["visited"] = True

    # last_node = current_node
    # print(minimum_value, index_minimum_value, distance, dijTable[current_node])
    # current_node = index_minimum_value
    distance_tally = []
    for x in range(len(lookupTable[current_node])):
        if lookupTable[current_node][x] == 9999:
            distance_tally.append(9999)
            continue 
        else: 
            distance = dijTable[x]["distance"]
            visited = dijTable[x]["visited"]
            print("hello", distance, visited, x, dijTable[x])
            if visited: 
                distance_tally.append(9999)
                continue
            # if distance == 9999: 
            #     distance = 0
            individual_path_distance = path_distance + lookupTable[current_node][x]
            print(individual_path_distance, path_distance, lookupTable[current_node][x])
            if individual_path_distance < distance:
                dijTable[x]["distance"] = path_distance + lookupTable[current_node][x]
                dijTable[x]["prev"] = current_node
            
            distance_tally.append(path_distance + lookupTable[current_node][x])
            print("dijTable", dijTable, "\n")

    best_distance = min(distance_tally)
    best_index = distance_tally.index(best_distance)
    print("stats", best_distance, best_index, distance_tally)

    path_distance = best_distance

    last_node = current_node
    current_node = best_index
    
    dijTable[current_node]["visited"] = True

    print("something", last_node, current_node)


# print(current_node, last_node, end, start)

while (current_node != start):
    print("The path is :", current_node)
    current_node = dijTable[current_node]["prev"]

print("The path is : " + str(start))
print("The total cost of traversing is : " + str(dijTable[end]["distance"]))