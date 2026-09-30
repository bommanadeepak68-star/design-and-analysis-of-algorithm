from collections import deque

n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):
    graph[i] = []

e = int(input("Enter number of edges: "))

for i in range(e):
    u = int(input("Enter first vertex: "))
    v = int(input("Enter second vertex: "))

    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))

visited = set()
queue = deque([start])
visited.add(start)

print("BFS:", end=" ")

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for x in graph[node]:
        if x not in visited:
            visited.add(x)
            queue.append(x)


