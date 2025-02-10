graph = {
    'S' : ['A','D'],
    'A' : ['C'],
    'D' : ['G'],
    'C' : ['G'],
    'G' : []
}

def BFS_with_goal(graph:dict, start, goal)->list[str]:
    queue = []
    res = []
    queue.append(start)
    while queue:
        elem = queue.pop(0)
        if elem not in res:
            res.append(elem)
            if elem == goal: return res
            for vertex in graph[elem]:
                queue.append(vertex)
    
    return goal + " not found"




def DFS_with_goal(graph: dict, start: str, goal: str) -> list[str]:
    res = []
    found = False 

    def dfs_helper(node):
        nonlocal found
        if found:
            return
        if node == goal:
            res.append(node)
            print(node)
            found = True
            return

        if node not in res:
            res.append(node)
            print(node,end=" ")
            for vertex in graph[node]:
                dfs_helper(vertex)

    dfs_helper(start)
    
    if not found:
        print("\ngoal :", goal , " Not found")
    else:
        print("goal : ",goal," found")



def DFS_without_recursion(graph:dict,start:str,goal:str)->list[str]:
    stack = []
    visited = []
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == goal:
                return visited
        
            for vertex in graph[node]:
                if vertex not in visited:
                    stack.append(vertex) 
        

        
    
    return goal + " not found"


#print("BFS_with_goal: ", BFS_with_goal(graph,"S","G"))
#print("DFS_with_goal: ", DFS_with_goal(graph,"S","C"))
#print("DFS_without_recursion : ", DFS_without_recursion(graph,"S","G"))
DFS_with_goal(graph,"S","G")
                
    
        



