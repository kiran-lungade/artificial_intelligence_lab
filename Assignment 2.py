'''
	NAME:: LUNGADE KIRAN SANJAY
	TITLE:: BREADTH FIRST SEARCH
'''

graph= {
    'A': ['B','C'],
    'B':['D','E'],
    'C': ['F','G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
visited = []
queue = []
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m,end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print("Following is BFS:: ")
bfs(visited, graph, 'A')


'''
****************     OUTPUT     ******************

Following is BFS:: 
A B C D E F G 


'''
