graph = {
    'S' : ['A','D'],
    'A' : ['C'],
    'D' : ['G'],
    'C' : ['G'],
    'G' : []
}

def BFS(graph:dict, start)->list[str]:
    queue = []
    res = []
    queue.append(start)
    while queue:
        elem = queue.pop(0)
        if elem not in res:
            res.append(elem)
            for vertex in graph[elem]:
                queue.append(vertex)
    
    return res

def DFS(graph:dict,start:str)->list[str]:
    res = []
    def dfs_helper(node):
        if node not in res:
            res.append(node)
            for vertex in graph[node]:
                dfs_helper(vertex)
    
    dfs_helper(start)

    return res




print("BFS : ",BFS(graph,'S'))
print("DFS : ",DFS(graph,'S'))