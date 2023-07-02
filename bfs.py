graph = {
    '5': ['3', '7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}

visited = []
que = []

def bfs(visited, graph, node):
    visited.append(node)
    que.append(node)
    
    while que:
        m=que.pop(0)
        print(m, end=',')
        for neighbour in graph:
            if neighbour not in visited:
                visited.append(neighbour)
                que.append(neighbour)

print("All the nodes are there")
bfs(visited,graph,'5')


