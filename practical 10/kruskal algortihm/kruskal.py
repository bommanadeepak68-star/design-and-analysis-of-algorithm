
def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])


def kruskal(edges, n):
    parent = [i for i in range(n)]
    cost = 0
    count = 0

    edges.sort(key=lambda x: x[2])

    print("Edges in Minimum Spanning Tree:")

    for u, v, w in edges:
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            print(u, "-", v, ":", w)
            cost += w
            parent[x] = y
            count += 1

        if count == n - 1:
            break

    if count == n - 1:
        print("Minimum cost:", cost)
    else:
        print("Graph is not connected")


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v weight):")

for i in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

kruskal(edges, n)
