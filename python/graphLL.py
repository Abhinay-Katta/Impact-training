from Linkedlist import Node
class GraphLL:
    def __init__(self,no_of_vertices) -> None:
        self.no_of_vertices=no_of_vertices
        self.graph=[None]*self.no_of_vertices
        
    def add_edge(self,s,d):
        '''Adds edge between given nodes (source and destination).'''
        node=Node(d)
        node.next=self.graph[s]
        self.graph[s]=node
        node=Node(s)
        node.next=self.graph[d]
        self.graph[d]=node
        return
    
    def traverse_graph(self):
        '''Traverse the graph.'''
        for i in range(self.no_of_vertices):
            temp=self.graph[i]
            print(i,end='')
            while temp:
                print('->'+str(temp.data),end=' ')
                temp=temp.next
            print()
            
    def DFS(self,start,visited):
        '''Explore the graph in depth.'''
        current=self.graph[start]
        print(start,end=' ') 
        visited[start]=True
        while current:
            if not visited[current.data]:
                self.DFS(start=current.data,visited=visited)
            current=current.next
      
    def cycle_detection(self):
        pass
    

size=5
graph=GraphLL(size)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.traverse_graph()
visited=[False]*size
graph.DFS(start=3,visited=visited)